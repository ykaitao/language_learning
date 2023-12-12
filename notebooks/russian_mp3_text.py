#%%
from pydub import AudioSegment

input_file = "/Users/ktyang/Documents/repo/language_learning/sample_data/RussianChapter17.mp3"
output_file = input_file.replace(".mp3", ".wav")

# Load the MP3 audio file
audio = AudioSegment.from_mp3(input_file)

# Export it to WAV format
audio.export(output_file, format="wav")

#%%
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Specify the path to your MP3 audio file
audio_file = "/Users/ktyang/Documents/repo/language_learning/sample_data/RussianChapter17.mp3"

# Use the recognizer to transcribe the audio
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)  # Record the entire audio file
    try:
        # Use the Google Web Speech API for speech recognition (requires an internet connection)
        text = recognizer.recognize_google(audio_data, language="ru-RU")
        print("Extracted Russian text:")
        print(text)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results: {e}")

#%%
#%%
#%%
