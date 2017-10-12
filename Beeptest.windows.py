
#import speech_recognition as sr 
import subprocess
import winsound


#Startup PAIGE SOUND sound
audio_file = winsound.PlaySound("C:\Users\Alan\Desktop\ACUSIO-master\STARTUP.wav", winsound.SND_FILENAME)






#Main Loop
while True:

	#User input
	command = raw_input('Enter a command: ') 

	#Speaking User input...


	##If person recieves a message
	if command == 'Message' :
		audio_file =  winsound.PlaySound("C:\Users\Alan\Desktop\ACUSIO-master\New_Message.wav", winsound.SND_FILENAME)
		



	##If person recieves a call
	if command == 'Call' :
		audio_file =  winsound.PlaySound("C:\Users\Alan\Desktop\ACUSIO-master\Incoming_Call.wav", winsound.SND_FILENAME)
		













