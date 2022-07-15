# first import gTTs
# gTTS module for text to speech conversion
from gtts import gTTS
# next import playsound using pip
# This module helps to play the converted audio
from playsound import playsound

# It is a text value that we want to convert to audio
text_val = 'The best and most beautiful things in the world cannot be seen or even touched — they must be felt with the heart.'
# Language in which you want to convert
language = 'en'
# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should have a high speed
obj = gTTS(text=text_val, lang=language, slow=False)
obj.save("Quote.mp3")
# Play the Quote.mp3 file
playsound('Quote.mp3')
