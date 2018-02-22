#First we import the time and webbrowser packages
import time
import webbrowser

#This is important to have a count of how many times you want to open the browser
No_of_breaks = 3
counter = 0
#print a statement to show at what time the program started
print("The program started at "+time.ctime())
while(counter < No_of_breaks):
    time.sleep(60 * 25) #the time.sleep takes time in terms of seconds
    webbrowser.open("https://www.youtube.com/watch?v=AfDfoQE2iyM")
    counter = counter + 1
