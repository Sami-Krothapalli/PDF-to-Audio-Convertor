import PyPDF2
import pyttsx3
from tkinter.filedialog import askopenfilename
from customtkinter import CTk, CTkButton, CTkLabel, CTkTextbox
import threading

# Initialize the pyttsx3 player globally
player = pyttsx3.init()
reading_thread = None
stop_event = threading.Event()

def open_file():
    book = askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if book:
        pdfreader = PyPDF2.PdfReader(book)
        pages = len(pdfreader.pages)
        text = ""
        for num in range(0, pages):
            page = pdfreader.pages[num]
            text += page.extract_text()
        text_area.insert("1.0", text)

def read_text():
    global reading_thread, stop_event
    stop_event.clear()
    text = text_area.get("1.0", "end-1c")
    reading_thread = threading.Thread(target=speak_text, args=(text,))
    reading_thread.start()

def speak_text(text):
    global stop_event
    player.connect('started-word', on_word)
    player.say(text)
    player.runAndWait()

def on_word(name, location, length):
    if stop_event.is_set():
        player.stop()

def stop_reading():
    global reading_thread, stop_event
    stop_event.set()
    if reading_thread and reading_thread.is_alive():
        reading_thread.join()
    reading_thread = None

def reset():
    global reading_thread, stop_event
    stop_event.set()
    if reading_thread and reading_thread.is_alive():
        reading_thread.join()
    reading_thread = None
    text_area.delete("1.0", "end")

# Initialize the main window
app = CTk()
app.title("PDF Reader")
app.geometry("700x700")

# Add a button to open the PDF file
open_button = CTkButton(app, text="Open PDF", command=open_file)
open_button.pack(pady=10)

# Add a text area to display the extracted text
text_area = CTkTextbox(app, width=600, height=400)
text_area.pack(pady=10)

# Add a button to read the text aloud
read_button = CTkButton(app, text="Read", command=read_text)
read_button.pack(pady=10)

# Add a button to stop reading the text
stop_button = CTkButton(app, text="Stop", command=stop_reading)
stop_button.pack(pady=10)

# Add a button to reset the application
reset_button = CTkButton(app, text="Reset", command=reset)
reset_button.pack(pady=10)

# Run the application
app.mainloop()