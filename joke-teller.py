import pyjokes as pj
import pyttsx3 as pt
import SpeechRecognition as sr
import speech_recognition as sr
import pyttsx3 
import pyjokes as pj
r = sr.Recognizer() 


def SpeakText(command):


    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()




while(1):


    try:


        with sr.Microphone() as source2:


            r.adjust_for_ambient_noise(source2, duration=0.2)


            audio2 = r.listen(source2)


            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say "+MyText)
#             SpeakText(MyText)

            if MyText == "joke":
                joke = pj.get_joke(language = "en", category = "neutral")
                SpeakText(joke)




    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occured")
joke = pj.get_joke(language = "en", category = "all")
e = pt.init()
e.say(joke)
e.runAndWait()