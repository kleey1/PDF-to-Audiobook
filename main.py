import pyttsx3
import PyPDF2
from gtts import gTTS

book = open('An_Ember_in_the_Ashes.pdf', 'rb')
pdfReader = PyPDF2.PdfReader(book)
pages = len(pdfReader.pages)
print(pages)

# Initialize the TTS engine
language = 'en'

speaker = pyttsx3.init()
# Set properties
rate = 150  # Speed of speech
volume = 0.9  # Volume (0.0 to 1.0)
speaker.setProperty('rate', rate)
speaker.setProperty('volume', volume)
# Get available voices and set to a female voice if available
voices = speaker.getProperty('voices')
for voice in voices:
    if 'female' in voice.name.lower():
        speaker.setProperty('voice', voice.id)
        break

# Function to read and speak each page from the PDF
def read_pdf(start_page, end_page):
    for num in range(start_page, end_page):
        page = pdfReader.pages[num]
        text = page.extract_text()
        
        speaker.say(text)
        speaker.runAndWait()


# Start reading the PDF in a separate thread
start_page = 9
read_pdf(start_page, pages)