import speech_recognition as sr

# Create recognizer object
r = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("🎤 Speak now...")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

# Try converting speech to text
try:
    text = r.recognize_google(audio)
    print("🧠 You said:", text)

except sr.UnknownValueError:
    print("❌ Could not understand audio")

except sr.RequestError:
    print("❌ Could not connect to Google API")