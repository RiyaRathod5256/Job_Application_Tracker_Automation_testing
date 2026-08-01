import pytest
from playwright.sync_api import sync_playwright



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    print(">>> Hook Started")

    outcome = yield
    report = outcome.get_result()

    setattr(item, "rep_" + report.when, report)

    print(">>> Hook Finished")

@pytest.fixture
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            slow_mo=1000
        )

        context=browser.new_context()

        context.tracing.start(
        screenshots=True,
        snapshots=True)

        page = context.new_page()
        
        yield page
        print(request.node.rep_call.failed)
        if request.node.rep_call.failed:

            context.tracing.stop(
                path=f"traces/{request.node.name}.zip"
            )

        else:
            context.tracing.stop()
        
        

        context.close()
        browser.close()

@pytest.fixture
def login_page(page):

    page.goto("http://127.0.0.1:8000/login")

    return page



