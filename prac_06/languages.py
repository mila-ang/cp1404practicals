"""
CP1404 - Practical
Languages (Client Code)
Estimate: 10 minutes
Actual: 15 minutes
"""

from programming_language import ProgrammingLanguage


def main():
    """Create and display programming language objects."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]
    for language in languages:
        print(language)

    print("\nThe dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
