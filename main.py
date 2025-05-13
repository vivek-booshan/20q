import question_parser as qp
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # browser = playwright.chromium.launch(headless=True)
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()
    # ---------------------
    page = context.new_page()
    page.goto("http://www.20q.net/")
    page.locator("frame[name=\"mainFrame\"]").content_frame.get_by_role("link", name="Think in American english").click()
    page.locator("frame[name=\"mainFrame\"]").content_frame.get_by_role("button", name="Play").click()
    # ---------------------
    for i in range(25):
        question = page.locator("frame[name=\"mainFrame\"]").content_frame.get_by_text(f"Q{i+1}").inner_text()
        choice = qp.parse_question_inner_text(question)
        # TODO (vivek): sometimes errors with a Call log: -waiting for locator(), need to identify issue
        page.locator("frame[name=\"mainFrame\"]").content_frame.get_by_role("link", name=choice, exact=True).click()
    # ---------------------
    context.close()
    browser.close()
    return

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
