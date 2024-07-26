# Virtual Assistant: Jarvis

This project implements a virtual assistant named Jarvis, which can perform various tasks such as opening web pages, playing music, fetching news, and responding to general queries using the OpenAI API.

## Modules Used

### speech_recognition
- **Function**: Recognizes speech input from the microphone.
- **Methods**:
  - `Recognizer()`: Creates a recognizer instance.
  - `Microphone()`: Captures audio from the default microphone.

### webbrowser
- **Function**: Opens web pages in the default browser.
- **Methods**:
  - `open(url)`: Opens the specified URL.

### pyttsx3
- **Function**: Converts text to speech.
- **Methods**:
  - `init()`: Initializes the TTS engine.
  - `say(text)`: Converts text to speech.
  - `runAndWait()`: Processes the queued commands.

### pyaudio
- **Function**: Required for accessing the microphone.

### musicLibary
- **Function**: Custom module containing a dictionary of songs and URLs.

### requests
- **Function**: Makes HTTP requests to fetch data from APIs.
- **Methods**:
  - `get(url)`: Sends a GET request.

### openai
- **Function**: Interacts with the OpenAI API.
- **Methods**:
  - `OpenAI(api_key)`: Initializes the client.
  - `chat.completions.create(parameters)`: Generates a response.

### gtts
- **Function**: Converts text to speech using Google Text-to-Speech.
- **Methods**:
  - `gTTS(text)`: Converts text and saves it as an MP3 file.

### pygame
- **Function**: Plays MP3 files.
- **Methods**:
  - `mixer.init()`: Initializes the mixer module.
  - `mixer.music.load(file)`: Loads an MP3 file.
  - `mixer.music.play()`: Plays the loaded file.
  - `mixer.music.get_busy()`: Checks if music is playing.
  - `time.Clock().tick(time)`: Controls loop frequency.

### os
- **Function**: Interacts with the operating system.
- **Methods**:
  - `remove(file)`: Deletes the specified file.

## Functions

### speak(text)
Uses `pyttsx3` to convert text to speech.
```python
def speak(text):
    engine.say(text)
    engine.runAndWait()
```
aiProcess(command)
Uses the OpenAI API to process the user's command and return a response.

```python
def aiProcess(command):
    client = OpenAI(api_key="*************************************************")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant. Give short responses, please."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content
```
processCommand(c)
Processes the user's command and performs the corresponding action.

```python
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    else:
        output = aiProcess(c)
        speak(output)
```
# Main Block
Initializes the virtual assistant and continuously listens for the wake word "Jarvis".

```python
if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if word.lower() == "jarvis":
                speak("Yes")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print(f"Error: {e}")
```
