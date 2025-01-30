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

    windowWidth = screenWidth-650
    windowHeight = screenHeight-100

    root.config(background="#faa5a4", width=windowWidth, height=windowHeight)
    root.attributes("-topmost", True)
    root.update_idletasks()

    print(root.winfo_geometry())
    print(root.wm_geometry())
    #makes it in the center of the screen!
    root.geometry(newGeometry=(str(windowWidth) + "x" + str(windowHeight) + "+" + str(int(screenWidth/2)-int(windowWidth/2)) + "+" + str(int(screenHeight/2)-int(windowHeight/2))))

    

    while True:
        guessedWord = input("Your guess: ").lower()
        if guessedWord.isalpha() and len(guessedWord) == 5:
            print("yay!")
        else:
            break
    
    


if __name__ == "__main__":
    main()