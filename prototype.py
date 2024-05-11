import speech_recognition as sr
import RPi.GPIO as GPIO
from gtts import gTTS
import time
import subprocess

def speak(text):
    tts = gTTS(text=text, lang='es', slow=False)  
    filename = "output.mp3"  
    tts.save(filename)
    subprocess.run(["mpg123", "-q", filename]) 

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW)

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ajustando el ruido de fondo... Por favor espera...")
        recognizer.adjust_for_ambient_noise(source)
        
        while True:  

            print("Di algo:")
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=4)

            try:
                print("Reconociendo...")
                text = recognizer.recognize_google(audio, language='es-ES')
                print(f"Creo que dijiste: '{text}'")

                if 'diego' in text.lower():  
                    speak("Hola, en que te puedo ayudar?") 
                    print()
                    print("\nActivado, esperando instrucciones.")

                    audio = recognizer.listen(source, timeout=10, phrase_time_limit=8)  
                    command = recognizer.recognize_google(audio, language='es-ES')
                    print(f"Instrucción: '{command}'")

                    if 'prende led' in command.lower():
                        GPIO.output(3, GPIO.HIGH)
                        speak("Luz prendida") 
                    elif 'apaga led' in command.lower():
                        GPIO.output(3, GPIO.LOW)
                        speak("Luz apagada") 
                    elif 'prende motor' in command.lower():
                        GPIO.output(12, GPIO.HIGH)
                        speak("Motor prendido") 
                    elif 'apaga motor' in command.lower():
                        GPIO.output(12, GPIO.LOW)
                        speak("Motor apagado") 

            except sr.UnknownValueError:
                print("No entendí el audio, intenta nuevamente.")
            except sr.RequestError as e:
                print(f"No se pudo solicitar resultados; {e}")

if _name_ == "_main_":
    main()