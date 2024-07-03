import pyperclip



commitTypes = {
    1: ("Add a new feature", "🆕 feat: "),
    2: ("Submit a fix to a bug", "🐛 feat: "),
    3: ("Improve performance", "⚡️ perf: "),
    4: ("Refactor code", "🛠 refactor: "),
    5: ("Add or update documentation", "📚 docs: "),
    6: ("Add or update tests", "🧪 test: "),
    7: ("Add or update build scripts", "🏗️ build: "),
    8: ("Another scope", None)
}

def selectScope():
    while True:
        try: 
            selectedScope = int(input("Pick a number (1-8): "))
            if selectedScope in commitTypes:
                return selectedScope
            else:
                print("Invalid choice, please pick a number from 1 to 8.")
        except ValueError: 
            print("Invalid choice, please pick a number from 1 to 8.")

print("Which one of this scopes fits better into your update?")
for key, (description, _) in commitTypes.items():
    print(f"{key}. {description}")

selectedScope = selectScope()

if selectedScope == 8:
    customScope = input("Enter your custom scope: ")
    prefix = f"{customScope}: "
else:
    _, prefix = commitTypes[selectedScope]

description = input("What's the description of your update? ")
commitMessage = f"{prefix}{description}"

pyperclip.copy(commitMessage)
print(f"Commit message copied to clipboard: {commitMessage}")

