import re
def parse_question_aria(aria_text):
    
    lines = aria_text.splitlines()
    print(lines)
    question = lines[1][len("- text:"):].strip()

    link_labels = []
    for line in lines:
        line = line.strip()
        if line.startswith("- link"):
            # Extract the link label in quotes
            match = re.search(r'"(.+?)"', line)
            if match:
                label = match.group(1)
                link_labels.append(label)

    print(question)
    print("Options:")
    for label in link_labels:
        print(f"  - {label}")

    while True:
        choice = input("Choose one of the options above: ").strip()
        if choice in link_labels:
            print(f"You selected: {choice}")
            return choice
        else:
            print(f"'{choice}' is not a valid option. Please try again.")

    return

def parse_question_inner_text(inner_text): 
    """
    Extracts the question and options from the inner_text of a locator. 
    """
    lines = [line.strip() for line in inner_text.strip().splitlines() if line.strip()]
    question = lines[0]

    if len(lines) == 2:
        options = [opt.strip() for opt in lines[1].split(",") if opt.strip()]
    elif len(lines) == 3:
        options = [opt.strip() for opt in lines[1].split(",")[:-1] if opt.strip()]
        options.extend(opt.strip() for opt in lines[2].split(",") if opt.strip())
    else:
        raise ValueError("Invalid question")

    print(question)
    print("Options:")
    for opt in options:
        print(f"  - {opt}")

    while True:
        choice = input("Choose one of the options above: ").strip()
        if choice in options:
            return choice
        else:
            print(f"'{choice}' is not a valid option. Please try again.")
    return

if __name__ == "__main__":
    inner_text_input = """
    Q1.  Is it classified as Animal, Vegetable or Mineral?
    Animal, Vegetable, Mineral, Concept, Unknown
    """
    aria_input = """
    - text: Q1. Is it classified as Animal, Vegetable or Mineral?
    - link "Animal":
      - /url: /gsq-en?Rx9SWSWC!NaI8w65S3v3NMLUR4HXGzGQUEaIYCufC
    - text: ","
    - link "Vegetable":
      - /url: /gsq-en?n55oJ-JoURTIOcAN-X_XRgWd7uPaskvqhX_Gmfkst
    - text: ","
    - link "Mineral":
      - /url: /gsq-en?nye4VzVbj2rRtlNhzS8S2KGp6a.93kOghDTZBwEMx
    - text: ","
    - link "Concept":
      - /url: /gsq-en?NcK9GZG91UVyvw_LZ3J3UdpjQ7MCBfDa9Hl6vSsLK
    - text: ","
    - link "Unknown":
      - /url: /gsq-en?a3tzwzwYuBKJLZ0tzGUGBr3Cj5n8NvR!vuwzQVjG!
    """
    parse_question_inner_text(inner_text_input)
    # parse_question_aria(aria_text)
