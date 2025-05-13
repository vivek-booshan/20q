import question_parser as qp
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    # browser = playwright.chromium.launch(headless=True)
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()
    # ---------------------
    page = context.new_page()
    page.goto("http://www.20q.net/")
    frame = page.locator("frame[name=\"mainFrame\"]").content_frame
    frame.get_by_role("link", name="Think in American english").click()
    frame.get_by_role("button", name="Play").click()
    # ---------------------
    MAX_QUESTIONS = 30 # 25 + the final question to validate guess
    for i in range(MAX_QUESTIONS):
        question = frame.get_by_text(f"Q{i+1}").inner_text()
        choice = qp.parse_question_inner_text(question)
        # nth(0) used because every answer will print a log of answers on the
        # website causing a resolve conflict between multiple matches
        frame.get_by_role("link", name=choice, exact=True).nth(0).click()
        if choice == "Right":
            break

    # ---------------------

    who_won = frame.get_by_role("heading", name="won!").inner_text()
    if who_won == "You won!":
        # TODO (vivek): see if get_by_role("link").all()[:-1] isolates the option links
        # youwon_options = frame.get_by_role("link").all()[:-1] # exclude the play again link
        
        # TODO (vivek): see if chaining get_by_text and get_by_role isolates option links
        # youwon_options = frame.get_by_text("You won! Is it one of these").get_by_role("cell") 
        # qp.parse_youwon_options(youwon_options)

        # TODO (vivek): handle textbox
        # page.locator("frame[name=\"mainFrame\"]").content_frame.get_by_role("textbox")
    elif who_won == "20Q won!":
        # TODO (vivek): Handle if 20q wins
        pass

    
    play_again_choice = input("Do you want to play again?: <y/n>").strip()
    if play_again_choice == "y":
        play_again = frame.get_by_role("link", name="Play Again").first.click()

    context.close()
    browser.close()
    return

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)
