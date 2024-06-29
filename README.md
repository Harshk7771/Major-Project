# Major-Project
# Language Translator

This is a Python-based language translator application built using the Tkinter library for the GUI, TextBlob for text processing, and Googletrans for language translation. The application allows users to translate text from one language to another, with the option to swap languages.

## Features

- Translate text between multiple languages.
- Swap languages with a single click.
- Simple and user-friendly interface.

## Requirements

- Python 3.x
- Tkinter
- Googletrans
- TextBlob
- Pillow

## Installation

1. **Clone the repository:**

   git clone https://github.com/Harshk7771/Major-Project
   cd language-translator

    Install the required packages:

    pip install googletrans==4.0.0-rc1 textblob pillow

Run the application:

    python translator.py

Usage

    Enter the text you want to translate in the left text box.
    Select the source and target languages from the dropdown menus.
    Click the "Translate" button to get the translated text in the right text box.
    Use the swap button to swap the source and target languages.

Code Overview
translator.py

This is the main file of the application. It includes the following key sections:

    Importing necessary libraries and extracting language options.
    Defining functions for translation and swapping languages.
    Setting up the Tkinter window and its components (labels, text boxes, combo boxes, buttons).

Functions

    trans_late(): Translates the text from the source language to the target language.
    swap_languages(): Swaps the source and target languages.

Components

    Labels: Display the title of the application.
    Frames: Organize the layout of text boxes.
    Text Boxes: Allow users to input and view translated text.
    Combo Boxes: Provide a dropdown menu for language selection.
    Buttons: Trigger the translation and swap actions.

Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request.
License

This project is open source and available under the MIT License.
Contact

For any questions or suggestions, please contact the author.
