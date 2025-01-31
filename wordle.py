from os.path import basename

def main():
    basePath = __file__.removesuffix(basename(__file__))

    wordListPath = basePath + "newWords.txt"

    wordFile = open(wordListPath, mode="r")

    words = []
    for line in wordFile:
            words.append(line.removesuffix("\n"))

    wordFile.close()
    
    ##Now we have our list of valid words
    #Next, ask for user input.

    #make a basic screen UI
    import tkinter as tk
    root = tk.Tk()
    root.title("Wordle!")

    screenWidth = root.winfo_screenwidth()
    screenHeight = root.winfo_screenheight()

    windowWidth = screenWidth-850
    windowHeight = screenHeight-100

    root.config(background="#121213")
    root.attributes("-topmost", True)
    root.update_idletasks()

    # makes it in the center of the screen!
    root.geometry(newGeometry=(str(windowWidth) + "x" + str(windowHeight) + "+" + str(int(screenWidth/2)-int(windowWidth/2)) + "+" + str(int(screenHeight/2)-int(windowHeight/2)-10)))

    # make the X button stop program execution
    root.protocol('WM_DELETE_WINDOW', exit)

    

    def detect_key_press(event):
        if (event.char) == " ":  return
        currentText = textBox.cget("text")
        if len(currentText) >= 5:   return
        currentText += event.char.upper()
        textBox.config(text=currentText)

    def backspace(event):
        currentText = textBox.cget("text")
        if len(currentText) == 0:   return
        textBox.config(text=currentText[:-1])

    def enter_pressed(event):
        currentText = textBox.cget("text")
        if len(currentText) != 5:   return
        textBox.config(text="")


    textBoxWidth = 8
    textBoxHeight = 1
    textBox = tk.Label(root, background="#f39291", foreground="White", font=("Helvetica", 50, "bold"), width=textBoxWidth, height=textBoxHeight, borderwidth=0, state="disabled")
    textBox.grid(column=0,row=0, sticky="n")#, padx=(windowWidth/2)-(textBoxWidth/2), pady=80)
    root.update()
    
    #center the thingy
    textBox.grid(padx=(windowWidth/2)-(textBox.winfo_width()/2), pady=20)
    textBox.config(text="")

    def clone(widget):
        parent = widget.nametowidget(widget.winfo_parent())
        cls = widget.__class__

        clone = cls(parent)
        for key in widget.configure():
            clone.configure({key: widget.cget(key)})
        return clone
    
    newThing = clone(textBox)
    newThing.grid(row= 1)#, pady=300)

    #make keys binded to a function
    root.bind_all('<Key>', detect_key_press)
    root.bind_all('<Key-Return>', enter_pressed)
    root.bind_all('<Key-BackSpace>', backspace)



    while True:
        guessedWord = input("Your guess: ").lower()
        if guessedWord.isalpha() and len(guessedWord) == 5:
            print("yay!")
            if guessedWord in words:
                print("valid fr")
        else:
            print("Not valid")
    
    


if __name__ == "__main__":
    main()