# Commit Message Generator

A simple Python script that helps you generate commit messages with appropriate prefixes and copies them to your clipboard. This script runs in the console and provides several predefined commit scopes with emojis.

## Features

- Prompts the user to select a commit scope.
- Asks for a description of the update.
- Generates a commit message with a prefix and the update description.
- Copies the commit message to the clipboard.

## Requirements

- Python 3.x
- `pyperclip` library

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/commit-message-generator.git
    cd commit-message-generator
    ```

2. **Set Up Virtual Environment**:
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Script**:
    ```bash
    python commit_message_generator.py
    ```

2. **Follow the Prompts**:
    - Select a commit scope by entering a number (1-8).
    - Enter the description of your update.

3. **The Generated Commit Message**:
    - The script will generate the commit message and copy it to your clipboard.
    - Paste the commit message in your Git commit.

## Example

```bash
Which one of these scopes fits better into your update?
1. Add new feature
2. Submit a fix to a bug
3. Improve performance
4. Refactor code
5. Add or update documentation
6. Add or update tests
7. Add or update build scripts
8. Another scope
Pick a number (1-8): 2
What's the description of your update? Fixed a critical bug in the payment processing
Commit message copied to clipboard: 🐛 fix: Fixed a critical bug in the payment processing
