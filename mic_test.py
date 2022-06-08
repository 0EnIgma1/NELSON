import speech_recognition as s_r
print(s_r.__version__) # just to print the version not required
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1) #my device index is 1, you have to put your device index
with my_mic as source:
    print("Say now!!!!")
    audio = r.listen(source) #take voice input from the microphone
print(r.recognize_google(audio, language='en-us')) #to print voice into text