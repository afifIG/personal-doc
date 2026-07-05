import pyttsx3
engine = pyttsx3.init()

# For Mac, If you face error related to "pyobjc" when running the `init()` method :
# Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

engine.say("I am Ahmad Afif. And i am a running student In UIU. of CSE department. good to see you.")
engine.runAndWait()
