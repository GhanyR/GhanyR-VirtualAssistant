# import speech_recognition as sr

# # obtain audio from the microphone
# # r = sr.Recognizer()
# # with sr.Microphone() as source:
# #     print("Say something!")
# #     audio = r.listen(source)

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print('Listening...')
#     r.pause_threshold = 1
#     r.energy_threshold = 494
#     r.adjust_for_ambient_noise(source, duration=1)
#     audio = r.listen(source)

# # recognize speech using Google Cloud Speech
# GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""INSERT THE CONTENTS OF THE GOOGLE CLOUD SPEECH JSON CREDENTIALS FILE HERE"""
# try:
#     print("Google Cloud Speech thinks you said " + r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS))
# except sr.UnknownValueError:
#     print("Google Cloud Speech could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Cloud Speech service; {0}".format(e))

import speech_recognition as sr
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))