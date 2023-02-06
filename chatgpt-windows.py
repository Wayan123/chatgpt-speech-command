
import speech_recognition as sr
from gtts import gTTS 
import time
import os
from playsound import playsound
import openai as ai
import warnings
warnings.filterwarnings("ignore")


# Get the key from an environment variable on the machine it is running on
ai.api_key = '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'

audio_file = "jarvis_record.mp3"

def listen_speak():

    def jarvis():
        myobj = gTTS(text=say, lang='id', slow=False)
        myobj.save(audio_file)
        playsound('jarvis_record.mp3')
        # os.system('jarvis_record.mp3')
        os.remove(audio_file)


    r = sr.Recognizer()
    r.energy_threshold = 4000
    r.dynamic_energy_threshold = True

    with sr.Microphone(sample_rate = 16000, chunk_size = 512) as source:
        print ('Bang Wayan mau nanya apa?')
        say = 'Bang Wayan mau nanya apa?'
        jarvis()
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            message = (r.recognize_google(audio, language = 'id', show_all = False))
            print("You said: " + message)
            #call(["espeak", message])

            def generate_gpt3_response(user_text, print_output=False):
    
            # Query OpenAI GPT-3 for the specific key and get back a response
            # :type user_text: str the user's text to query for
            # :type print_output: boolean whether or not to print the raw output JSON
            
                completions = ai.Completion.create(
                engine='text-davinci-003',  # Determines the quality, speed, and cost.
                temperature=0.5,            # Level of creativity in the response
                prompt=user_text,           # What the user typed in
                max_tokens=4000,             # Maximum tokens in the prompt AND response
                n=1,                        # The number of completions to generate
                stop=None,                  # An optional setting to control response generation
            )

                # Displaying the output can be helpful if things go wrong
                if print_output:
                    print(completions)

                # Return the first choice's text
                return completions.choices[0].text

            """
            models = ai.Model.list()

            for model in models.data:
                print(model.id)
            """

            print(" ")
            # prompt = input("Bang Wayan mau nanya apa? ")
            response = generate_gpt3_response(message)
            
            print(" ")
            print(" ")
            print("Ziyon-GPT3: ", response)
            print(" ")
            say = response
            jarvis()
            print(" ")

        except:
                #call(['espeak', 'Silahkan ulangi'])
                print ('Silahkan ulangi')
                time.sleep(1)

if __name__ == '__main__':
    while True:
        listen_speak()
        
        
        