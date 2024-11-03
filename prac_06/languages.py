"""
CP1404 - Practical
Languages (Client Code)
"""

from programming_language import ProgrammingLanguage


def main():
    """Create and display programming language objects."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)
    print(ruby)
    print(visual_basic)

    languages = [python, ruby, visual_basic]
    for language in languages:
        print(language)


main()
