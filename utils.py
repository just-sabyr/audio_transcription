import speech_recognition as sr
from googletrans import Translator 
import sounddevice as sd
from scipy.io.wavfile import write

# initialize the recognizer
r = sr.Recognizer()

def speech_to_text(filename, language='en-EN'):
    # Open the file
    with sr.AudioFile(filename) as source:

        # Load audio to memory
        audio_data = r.record(source)

        # Recognize (convert from speech to text)
        text = r.recognize_google(audio_data, language=language)

    return text
 

def realtime_recognize(duration=5, language='en-EN', fs=44100):
    print('\nRecording started\n-------------------------')
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    # Ensure that recording is a 1-dimensional array for a mono file
    recording = recording.reshape(-1)
    print('Recording Finished')

    write('recordings/audio.wav', fs, recording)

    # Audio to text
    text = speech_to_text('recordings/audio.wav')
    
    return text

def translate_text(text):
    translator = Translator()
    translation = translator.translate(text, dest='en')
    return translation.text
