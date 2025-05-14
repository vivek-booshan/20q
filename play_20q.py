import question_parser as qp
import win_parser as wp
from playwright.sync_api import Playwright, sync_playwright, Locator

def run():
    with sync_playwright() as playwright:
        _run(playwright)

def _run(playwright: Playwright):
    
    # --------------------- launch
    # browser = playwright.chromium.launch(headless=True)
    browser = playwright.firefox.launch(headless=True)
    context = browser.new_context()

    # --------------------- start game
    page = context.new_page()
    page.goto("http://www.20q.net/")
    frame = page.locator("frame[name=\"mainFrame\"]").content_frame
    frame.get_by_role("link", name="Think in American english").click()
    frame.get_by_role("button", name="Play").click()

    play_again = True
    while play_again:
    # --------------------- play game
        guessed = _questions(frame)
    # --------------------- handle win condition
        _win_condition(guessed, frame)
    # --------------------- score game
    # --------------------- log score
    # --------------------- play again
        play_again_choice = input("Do you want to play again?: <y/n>").strip()
        if play_again_choice == "n":
            play_again = False
        else:
            frame.get_by_role("link", name="Play Again").first.click()

    # --------------------- clean up
    context.close()
    browser.close()
    return

def _questions(frame: Locator.content_frame) -> bool:
    """
    Handles running through the questions
    Returns true if 20q won, false else
    """
    MAX_QUESTIONS = 30
    for i in range(MAX_QUESTIONS): # max possible questions
        question: str = frame.get_by_text(f"Q{i+1}").inner_text()
        choice = qp.parse_question_inner_text(question)
        frame.locator("nobr").get_by_role("link", name=choice, exact=True).click()
        if choice == "Right":
            return True
    return False

def _win_condition(guessed: bool, frame: Locator.content_frame):
    if guessed:
        return

    # TODO (vivek): see if chaining get_by_text and get_by_role isolates option links
    # youwon_options = frame.get_by_text("You won! Is it one of these").get_by_role("cell") 

    # TODO (vivek): see if get_by_role("link").all()[:-1] isolates the option links
    youwin_options = frame.get_by_role("link").all()[:-1]
    choice = wp.parse_youwin_options(youwin_options)
    if choice != "Other":
        frame.get_by_role("link", name=choice, exact=True).click()
    elif choice == "Other":
        subject = input("What were you thinking of?: ").strip()
        frame.get_by_role("textbox").fill(subject)
        frame.get_by_role("button", name="Search").click()
        # TODO: handle look deeper and what not
        pass
    return

if __name__ == "__main__":
    run()
