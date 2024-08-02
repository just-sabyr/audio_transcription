import os
from utils import speech_to_text, translate_text, realtime_recognize

scripts_dir = 'scripts'
script_name = 'sample.txt'

# Create the folder for scripts
if not os.path.exists(scripts_dir):
    os.makedirs(scripts_dir)

# Define full file path
file_path = os.path.join(scripts_dir, script_name)

# Record audio from microphone
text = realtime_recognize(duration=5, language='en-EN')
# text = speech_to_text('recordings/audio.wav')

# Write the text to the file
with open(file_path, 'w') as file:
    file.write(text)

print(f'Audio script has been saved to {file_path}')