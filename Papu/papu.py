
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia #tuve que instalar "setuptools" y "PyAudio". Sin ellos, el programa NO funciona.

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait() #funcion para que hable.

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"Comando recibido: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("No entendí el comando.")
            return ""
        except sr.RequestError:
            print("Error al conectar con el servicio de reconocimiento de voz.")
            return "" #función que "escucha", lo manda a google para la identificación y lo retorna como texto. da dos errores en caso que los tenga que dar.

def main():
    speak("Hola, soy papu, su asistente virtual. ¿Para qué soy buena?") #función del bot en general
    
    while True:
        command = listen()

        if "stop" in command: #corta
            speak("Adiós.")
            break
        elif "hora actual" in command: #hora en horas y minutos(PC)
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"La hora actual es {current_time}.")
        elif "video" in command:
            speak("¿Qué recomendaciones de YouTube quieres ver?")
            video_name = listen()
            search_url = f"https://www.youtube.com/results?search_query={video_name.replace(' ', '+')}"
            webbrowser.open(search_url) #abre un link de youtube con recomendaciones del tema de interés.
            speak("Buscando coincidencias.")
        elif "wikipedia" in command:
            speak("¿Qué información quieres buscar en Wikipedia?")
            query = listen()
            try:
                webbrowser.open(f"https://es.wikipedia.org/wiki/{query.replace(' ', '_')}")
                summary = wikipedia.summary(query, sentences=1) #abre wikipedia según lo deseado. en ocasiones, presenta falencias, por eso los tres casos de abajo.
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Hay varias opciones. Puedes ser más específico.")
            except wikipedia.exceptions.PageError:
                speak("No encontré información sobre eso.")
            except wikipedia.exceptions.WikipediaException:
                speak("Ocurrió un error al buscar en Wikipedia.")
        elif "google" in command:
            speak("¿Qué quieres buscar?")
            search_query = listen()
            search_url = f"https://www.google.com/search?q={search_query.replace(' ', '+')}"
            webbrowser.open(search_url) #básicamente, lo mismo que youtube
            speak("Estos son los resultados que encontré.")
        else:
            speak("No puedo ayudar con eso.") #en caso que el bot no entienda. (pasa más de lo que me gusta admitir, no entiende algunas palabras.)

if __name__ == "__main__":
    main()