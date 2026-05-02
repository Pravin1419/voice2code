import subprocess
import speech_recognition as sr
from code_generator import generate_code

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("\n🎤 Speak your command (say 'stop' to exit)...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("🧠 You said:", text)

        if "stop" in text.lower():
            print("👋 Exiting...")
            break

        code = generate_code(text)

        print("\n💻 Generated Python Code:\n")
        print(code)

        with open("generated_code.py", "w") as f:
            f.write(code)

        print("Code saved to generated_code.py")
       
        print("\n🚀 Running your code:\n")
        try:
            subprocess.run(["python", "generated_code.py"])
        except:
            print("⚠️ Error while running generated code")

    except sr.UnknownValueError:
        print("❌ Could not understand audio")

    except sr.RequestError:
        print("❌ API error")