import speech_recognition as sr
import pyttsx3
import pyaudio
import openai
import webbrowser
import os
import random
import datetime
import pywhatkit as pywht
from selenium import webdriver
from selenium.webdriver.common.by import By


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)
    engine.say(text)
    engine.runAndWait()


# greets you... ehehehhehe... Wa Ha Ha Ha ha ha... BuriBuri buriburi..........
def Yo():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Yo! Good Morning!")
    elif hour>=12 and hour<18:
        speak("Yo! Good Afternoon")
    elif hour>=18 and hour<21:
        speak("Yo! Evening!")
    else:
        print(f"\nSleep tight... you damn sleepy head, Yo!\n")
        speak("Sleep tight... you damn sleepy head, Yo!")
    
    say_hi = ("How you doin'...!? I'm Ken... want help with something...!?", "Ken here, hope you doin' well. What can I help you with...!?", "Call me Ken... how you doin' by the way...!? So, what do we have here...!?", "It's Ken, how you doin'...!? So what are we dealing with...!?")
    speak(random.choice(say_hi))


# takes microphone input from the user and returns the string output
def Listeninguh():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("\nSay that again...")
        return "None"
    return query


# ShadowCloninguh googuruh
def Google_2(query):
    link = f"https://www.google.com/search?q={query}"
    webbrowser.open(link)

# ShadowCloninguh YouTubeh
def YouTube(query):
    trimmed_query = ''.join(''.join(''.join(''.join(''.join(query.split("play")).split("on")).split('in')).split("youtube")).split('open')).strip()
    webbrowser.open(f"https://www.youtube.com/results?search_query={trimmed_query}")
    pywht.playonyt(trimmed_query)


# OpenAI API functionalities

def chattohbottoh_dattebayo(query):
    openai.api_key = "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"
    response = openai.ChatCompletion.create(model = 'gpt-3.5-turbo', messages = [{'role': "user", 'content': query}])
    
    try:
        print(f"{response.choices[0].message.content}\n")
        speak(response.choices[0].message.content)
    except:
        print('error404...!\nEncountered some unexpected error!\n')
        speak('something unexpected happened!')    
    
    text = f"{query}\n--------------------\n\n"
    text += response['choices'][0]['message']['content']
    
    if not os.path.exists("C:\\Yo! Nekochi....!!!"):
        os.mkdir("C:\\Ken's Responses")
    with open(f"C:\\Ken's Responses\\{query}.txt", "w") as f:
        f.write(text)
    
    wordCount = text.count(' ') + 1
    if wordCount >= 24:
        periodic_replies = ('''Don't rush to copy, you can access the responses anytime in the C-drive's auto-created folder "Yo! Nekochi....!!!"''', '''You can always find the answers in the C-drive folder, "Yo! Nekochi....!!!"''', '''You can locate the responses anytime in the "Yo! Nekochi....!!!" folder of the C-disk''', '''Don't copy right away... you can always find the answers in C-disk's "Yo! Nekochi....!!!" folder''', '''You can retrieve the responses at any given moment in the "Yo! Nekochi...!!!" folder of the C-disk''', '''Rest Easy... the answers are always available in the C-drive's folder "Yo! Nekochi....!!!"''', '''Relax... the answers can be accessed in C-drive's "Yo! Nekochi....!!!" folder at any given moment''')

        note = ("Don't rush to copy, you can access the responses anytime in the C-drive's auto-created folder Yo Nekochi...", "You can always find the answers in the C-drive folder Yo Nekochi", "You can locate the responses anytime in the Yo Nekochi folder of the C-disk", "Don't copy right away, you can always find the answers in C-disk's Yo Nekochi folder", "You can retrieve the responses at any given moment in the Yo Nekochi folder of the C-disk", "Rest Easy, the answers are always available in the C-drive's folder Yo Nekochi", "Relax... the answers can be accessed in C-drive's Yo Nekochi folder at any given moment")

        print(f'{random.choice(periodic_replies)}\n\n')
        speak(random.choice(note))


def imageh_generatah(query):
    openai.api_key = "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"
    response = openai.Image.create(prompt = ''.join(''.join(''.join(query.split('generate')).split('image')).split('of')))
    try:
        image_url = response['data'][0]['url']
        webbrowser.open(image_url)
    except:
        print('error404...!\nEncountered some unexpected error!\n')
        speak('something unexpected happened!')

                                                                                                        
# &&&&& wrrapping up the AI functionalities


def music(query):
    pywht.playonyt(query)
    
    try:
        username = "enter the spotify email"
        password = "enter the spotify password"

        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        YoHoHoHoHohoho = webdriver.Chrome(options = options)
    
        YoHoHoHoHohoho.get(f'https://accounts.spotify.com/en/login?continue=https%3A%2F%2Fopen.spotify.com%2Fsearch%2F{query}')
        YoHoHoHoHohoho.find_element(By.CSS_SELECTOR, '#login-username').send_keys(username)
        YoHoHoHoHohoho.find_element(By.CSS_SELECTOR, '#login-password').send_keys(password)
        YoHoHoHoHohoho.find_element(By.CSS_SELECTOR, '.ButtonInner-sc-14ud5tc-0.cJdEzG.encore-bright-accent-set').click()
        print("Opening the song in Youtube, SoundCloud & Spotify...\n")
    
    except:
        print('\nSomething unexpected happened while opening in spotify, make sure to have the latest version of chrome installed\n')


# Final Xecution

if __name__ == "__main__":
    Yo()
    # speak("It's more fun to chase than be chased.. that's why young girls grow up to be adults falling in love with love...")
    
    while True:
        query = Listeninguh().lower()
        
        # logic for xecuting tasks based on query

        if "jarvis" in query:
            
            if "open gintama" in query or "open one piece" in query or "open naruto shippuden" in query or "open naruto" in query or 'open demon slayer' in query:
                l =(("open gintama", "https://sanji.to/gintama-13"), ("open one piece", "https://sanji.to/one-piece-100"), ("open naruto", "https://sanji.to/naruto-677"), ("open naruto shippuden", "https://sanji.to/naruto-shippuden-355"), ("open demon slayer", "https://sanji.to/demon-slayer-kimetsu-no-yaiba-47"))
                [webbrowser.open(s[1]) and speak(f"opening {''.join(s[0].split('open')).strip()}") for s in l if s[0] in query]

            elif "whatsapp" in query or "linkedin" in query or "discord" in query or 'telegram' in query or 'spotify' in query:
                sites = (("whatsapp", 'https://web.whatsapp.com/'), ("linkedin', 'https://in.linkedin.com/"), ("discord", "https://discord.com/"), ('telegram', 'https://web.telegram.org/k/'), ('spotify', 'https://open.spotify.com/'))
                [webbrowser.open(site[1]) and speak(f"opening {site[0]}") for site in sites if site[0] in query]

            elif "open anime" in query:
                trim_query = ''.join(query.split("open anime")).strip()
                webbrowser.open(f"https://sanji.to/search?keyword={trim_query}")
                speak("just scroll down...")

            elif "youtube" in query:
                YouTube(query)
                speak("just a second")

            elif "play" in query:
                music(''.join(query.split("play")).strip())

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%X")
                strDate = datetime.datetime.now().strftime("%x")
                strDay = datetime.datetime.now().strftime("%A")
                print(strTime)
                print(strDate)
                print(f"{strDay}\n")
                speak(f"the time is {strTime}, it's {strDate} & {strDay}")

            elif "image" in query:
                print(f"Just a sec...\n\n")
                speak("just a second")
                imageh_generatah(query)
                speak('creating the image')
            
            elif "quit" in query or 'close the app' in query:
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<18:
                    print("Have a good day ahead.......... Yo!\n\n")
                    speak("Have a good day ahead, Yo!")
                elif hour>=18 and hour<21:
                    print("Have a bliss evening ahead.......... Yo!\n\n")
                    speak("have a bliss evening ahead, Yo!")
                else:
                    print(f"bummer... just go to bed... you sus sleepy head, Yo!\n\n")
                    speak("bummer... just go to bed... you sleepy head, Yo!")
                exit

            elif 'shutdown' in query:
                print("Save all your work before the device shuts down within the next 27 seconds!\n")
                speak("save all your work before the device shuts down within the next 27 seconds!")
                os.system('shutdown /s /t 27')
                
            elif 'reboot' in query:
                print("Save all your work before the device reboots within the next 27 seconds!\n")
                speak("save all your work before the device reboots within the next 27 seconds!")
                os.system('shutdown /r /t 27')
                
            elif 'none' in query:
                replies = ("I don't get what you're saying. Can you just rephrase or provide more context...!?", "I'm not getting what you are trying to communicate...", "Can you give more context to what you're trying to say?", "Can you rephrase or ask a different question?", "I don't quite get it...! Be more creative...", "Can't understand what you mean. Provide more information or context", "Can't reply to null inputs, give a specific task to assist you better", "I don't get it! Can you be more clear...!?")
                print(f"\n{random.choice(replies)}\n\n")
                
            elif 'porn' in query or 'sex videos' in query or 'adult content' in query or 'adult videos' in query:
                print('fuckin diabolical cunt, ya got that much time to spare? better go outdoors, learn market relevent skills or better yet, just get some "sleep"...\n')
                speak('fuckin diabolical cunt, ya got that much time to spare? better go outdoors, learn market relevent skills or better yet, just get some "sleep"...')

            elif "screenshot" in query:
                pywht.take_screenshot()
            
            else:
                print(f"Just a sec...\n")
                speak("just a second")
                Google_2(query)
                chattohbottoh_dattebayo(query)
