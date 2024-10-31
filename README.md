# PDF-to-Audio-Convertor

This project is a PDF reader with text-to-speech functionality built using Python. It allows users to open a PDF file, extract its text, and read the text aloud using the `pyttsx3` library. The GUI is created using the `customtkinter` library.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [What I Learned](#what-i-learned)
- [Difficulties Encountered](#difficulties-encountered)
- [Screenshots](#screenshots)

## Features

- Open and read PDF files.
- Extract text from PDF files.
- Read the extracted text aloud using text-to-speech.
- Stop the text-to-speech reading.
- Reset the application to open a new PDF file.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/pdf-reader-tts.git
   cd pdf-reader-tts
   ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux  
    ```

3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```


## Technologies Used
- Python
- PyPDF2
- pyttsx3
- customtkinter
- threading

## What I Learned:
- How to use the PyPDF2 library to read and extract text from PDF files.
- How to use the pyttsx3 library for text-to-speech conversion.
- How to create a GUI using the customtkinter library.
- How to manage threading in Python to keep the GUI responsive.

## Difficulties Encountered
- Managing the text-to-speech thread to ensure it stops correctly when the stop button is pressed.
- Ensuring the GUI remains responsive while performing text-to-speech operations.
- Properly resetting the application state to allow for opening new PDF files.


## Screenshots

1. **Main Screen**:
   ![Main Screen](\Images\MainScreenshot.PNG)

2. **Reading Text**:
   ![Reading Text](\Images\Capture.PNG)
