#!/usr/bin/env python3
import asyncio
import tkinter as tk
from tkinter import ttk
import cut_copy_paste as ccp
import edge_tts


ask = '''<speak>

hello, <emphasis level="strong">Hello motherfucker</emphasis> <break strength="weak"/> <emphasis level="strong">i will fill you ass with cum</emphasis>

</speak>'''

names = {}

async def retVoiceList():
    return await edge_tts.list_voices()

for voice in asyncio.run(retVoiceList()):
    print(voice)
    name = voice["Name"]
    fname = voice["FriendlyName"]

    names[fname] = name

    print(names)


async def Speak(filename, text):
    l2.configure(text=f"Started")
    print(ssml.get())








    """
    Main function
    """
    communicate = edge_tts.Communicate()
    with open(filename, "wb") as file:
        length = len(text)
        f = 0

        vci = names[v.get()]

        print(vci)
        try:
            async for i in communicate.run(text, voice=vci,  customspeak=ssml.get()):
                print(f"{f}")
                l2.configure(text=f"Saved as {filename}")


                file.write(i[2])

                f += 1
        except:
            pass



def on_button():
    asyncio.run(Speak("hello.mp3", "Hello my friend"))



root = tk.Tk()

# Pack a big frame so, it behaves like the window background
big_frame = ttk.Frame(root, padding=15)
big_frame.pack(fill="both", expand=True)

# Set the initial theme
root.tk.call("source", "sun-valley.tcl")
root.tk.call("set_theme", "light")

def change_theme():
    # NOTE: The theme's real name is sun-valley-<mode>
    if root.tk.call("ttk::style", "theme", "use") == "sun-valley-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")

def OnClickSave():
    text = e.get("1.0",'end-1c')


    fname = filename.get()
    print(text)
    print(fname)

    asyncio.run(Speak(f"{fname}.mp3", text))
# Remember, you have to use ttk widgets
e = tk.Text(big_frame, height=10, width=80)
e.grid(row=0, column=0)

filename_frame = ttk.Frame(big_frame)
filename_frame.grid(row=1, column=0)

l1 = ttk.Label(filename_frame, text="Filename:    ", justify=tk.LEFT, anchor=tk.W)
l1.grid(row=2, column=0, sticky=tk.W)

e1text = "file"
filename = tk.StringVar()
e1 = ttk.Entry(filename_frame, textvariable=filename)
e1.grid(row=2, column=1, sticky=tk.E)
e1.insert(0, e1text)

v = tk.StringVar(filename_frame)
v.set(list(names.keys())[0]) # default value

w = tk.OptionMenu(filename_frame,v , *list(names.keys()))
w.grid(row=2, column=2)

b1text = tk.StringVar(value="save")
text = tk.StringVar()
b1 = ttk.Button(filename_frame, text='save', textvariable=b1text, command=OnClickSave)
b1.grid(row=3, column=0)

l2 = ttk.Label(filename_frame, text="Progress", justify=tk.LEFT, anchor=tk.W)
l2.grid(row=3, column=1, sticky=tk.W)

ssml = tk.BooleanVar()
c1 = ttk.Checkbutton(filename_frame, text="SSML", state=False, variable=ssml)
c1.grid(row=3, column=2)



#button = ttk.Button(big_frame, text="Change theme!", command=change_theme)
#button.grid(row=1, column=1)

ccp.make_textmenu(root, tk)
root.bind_class("Text", "<Button-3><ButtonRelease-3>", ccp.show_textmenu)



if __name__ == "__main__":
    root.mainloop()
