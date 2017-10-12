from os import system
#import speech_recognition as sr 
import subprocess



#Startup PAIGE SOUND sound
#audio_file = "/Users/MauricioRojas18755/Desktop/LEGACY INTL/Paige/JARVIS CLIPS/Wavs/STARTUP.wav"
#return_code = subprocess.call(["afplay", audio_file])





#Main Loop
while True:

	#User input
	command = raw_input('Enter a command: ') 

	#Speaking User input...


	##If person recieves a message
	if command == 'Message' :
		audio_file = "/Users/MauricioRojas18755/Desktop/LEGACY INTL/Paige/JARVIS CLIPS/Wavs/New_Message.wav"
		return_code = subprocess.call(["afplay", audio_file])



	##If person recieves a call
	if command == 'Call' :
		audio_file = "/Users/MauricioRojas18755/Desktop/LEGACY INTL/Paige/JARVIS CLIPS/Wavs/Incoming_Call.wav"
		return_code = subprocess.call(["afplay", audio_file])














