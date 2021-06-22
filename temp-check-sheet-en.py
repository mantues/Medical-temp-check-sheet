# web ↓
# https://office54.net/python/tkinter/textbox-get-insert

import tkinter as tk
from tkinter import *
import csv
import os

# Processing when a button is pressed.
def memo_temp():
    #Read IDs from taion.csv
    index=int(textID.get())#ID value judgment
    if(index<1 or 1001<index):
        s="Make sure ID is correct.(Range：1~1000)"
        labelResult['text']=s
        return

    else:
        #Body temperature value judgment
        temp=float(texttemp.get())
        #Body temperature value judgment
        if(temp<35 or 40<temp):
            s="Please re-enter your body temperature. Range: 35~40℃"
            labelResult['text']=s
            return
        else:
            if(37.5<temp):
                s="High fever."
            elif(temp<35.5):
                s="Body temperature is low."
            else:
                s="Let's do our best today!"
        #taion.csv file read
        filename="taion.csv"
        #Check if there is a csv file. If not, create one.
        if (os.path.exists(filename)):
            with open(filename, "r") as f:
                read_csv=csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
                #val=f.read()
                temp_files=[row for row in read_csv]
                #print(temp_files)
        else:
            temp_files=[]


        #Determine if the ID (index) is larger than the list, and if so, add a line.
        if(index<len(temp_files)):
            id_temp=temp_files[index-1]
        else:
            for i in range(0, index-len(temp_files)):
                temp_files.append([])
            id_temp=temp_files[index-1]
        #Add body temperature to the list
        id_temp.append(float(temp))
        #Calculation of average body temperature (must be in str format to be displayed)
        average=str(sum(id_temp)/len(id_temp))
        #print(average)
        print(temp_files)
        labelResult['text']=s+"\n Average: "+ average + "℃"
        #Writing Files
        with open(filename, 'w', newline="") as f:
            writer = csv.writer(f)
            writer.writerows(temp_files)


# Create a window
win = tk.Tk()  # Empty window. This is where you put the information.
win.title("Medical record sheet")  # Specify the window title
win.geometry("250x250")  # Specify size

#Loading image（optional）png, pgm, ppm, gif
image_file = "pic.png"
image = tk.PhotoImage(file=image_file)

if (os.path.exists(image_file)):
    img=tk.Label(image=image)
    img.pack()

# Create the parts
labelID = tk.Label(win, text='ID:')  # Labels to place in the window
labelID.pack()  # Commands to be placed in the window from top to bottom

textID = tk.Entry(win)  # Create a text box
textID.insert(tk.END, '1')  # Default characters
textID.pack()  # deployment

labeltemp = tk.Label(win, text='Body temperature(℃):')  # Same as ID
labeltemp.pack()

texttemp = tk.Entry(win)
texttemp.insert(tk.END, '36.5')
texttemp.pack()

labelResult = tk.Label(win, text='---')  # Same as ID
labelResult.pack()  # This is the part that is specified as labelResult['text'] = s in the memo_temp function. It overwrites the text part of text='---' created in line 86.

calcButton = tk.Button(win, text='Record')  # In Button widget, you can specify the command.
calcButton["command"] = memo_temp  # Calling the function memo_temp
# The above two lines can be summarized as calcButton = tk.Button(win, text='record',command=memo_temp)
calcButton.pack()

# Work the window
win.mainloop()