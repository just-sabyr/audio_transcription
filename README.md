# Audio Transcription Project
Transcribe saved audio files or save audios and transcribe them
This project provides a tool to record and transcribe audio files using Python. The recording is done using the `sounddevice` library, and the transcription is performed using the `speech_recognition` library with the (unofficial) Google Web Speech API.

## Features

- Record audio from the microphone
- Save recorded audio to a WAV file
- Transcribe the recorded audio to text using the Google Web Speech API

## Requirements

- Python 3.10.x
- Libraries listed in requirements.txt

## Installation

1. Clone the repository
 
   ```sh
   git clone https://github.com/just-sabyr/audio_transcription.git
   cd audio_transcription
   ```
   
2. Create a venv

   ```sh
   python3 -m venv .venv
   ```
   
3. Activate the venv
    
   ```sh
   source .venv/bin/activate
   ```
   
4. Install the required libraries
   
   ```sh
   pip install -r requirements.txt
   ```
   
5. Run the script
   
   ```sh
   python main.py
   ```
   
