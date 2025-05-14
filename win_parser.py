import typing

def parse_youwin_options(youwon_options: typing.List["Locator"]) -> typing.Union[str, None]:
    print("Is it one of these ...")
    options = [option.__name__ for option in youwon_options if option.__name__]
    options.append("Other")
    for option in youwon_options:
        print(f"  - {option.__name__}")

    while True:
        # TODO : handle look deeper inside the parse function and maybe use
        # multiple return to determine if the choice is on the main page or the look
        # deeper page
        choice = input("Choose one of the options above: ").strip()
        if choice in options:
            return choice
        else:
            print(f"'{choice}' is not a valid option. Please try again.")
    return None
    
