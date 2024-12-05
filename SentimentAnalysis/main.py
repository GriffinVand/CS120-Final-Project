import pandas as pd
import tkinter as tk

"""Compares given input against two lists of words(positive and negative) and determines if
the input is positive or negative"""
def AnalyzeSentiment(userInput):
    pw = pd.read_csv("SentimentAnalysis/POSITIVE_WORDS.csv", header=None)
    nw = pd.read_csv("SentimentAnalysis/NEGATIVE_WORDS.csv", header=None)

    pScore = 0
    nScore = 0
    
    userWords = userInput.split()
    for word in userWords:
        for pWord in pw[0]:
            if word.lower() == pWord:
                pScore += 1
        for nWord in nw[0]:
            if word.lower() == nWord:
                nScore += 1
    
    """Stores the ratio of positive to negative words"""
    pnRatio = 0
    if(pScore != 0 and nScore != 0):
        pnRatio = pScore / nScore

    """If the ratio of positive to negative words is within a given range
    it's safer to assume the statement is not specifically negative or positive"""
    if pScore == nScore or (pnRatio > 0.8 and pnRatio < 1.2):
        return ('neutral')
    elif pScore > nScore:
        return ('positive')
    else:
        return ('negative')
    

"""Updates the display to show the last statement typed by the user"""
def UpdateLastUserInput(userInput):
    youtyped_label.config(text='You typed:')
    lastinput_label.config(text=f'{userInput}')
    thisstatement_label.config(text='This statement might be:')
    output_label.config(text=(AnalyzeSentiment(userInput)))


"""Reads the user entry and sends it to the analyze sentiment function"""
def AcceptInput():
    user_input = entry.get()
    UpdateLastUserInput(user_input)
    entry.delete(0, tk.END)

"""Creates new tk instance"""
root = tk.Tk()
root.title("Sentiment Analysis Chamber")
root.geometry("600x400")

"""Instructions label"""
label = tk.Label(root, text="Type anything and I will analyze it")
label.pack(pady=10)

"""Area for user to enter their statement"""
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

"""Button to start analysis"""
button = tk.Button(root, text="Analyze Sentiment", command=AcceptInput)
button.pack(pady=10)

"""Displays the last typed statment"""
youtyped_label = tk.Label(root, text="")
youtyped_label.pack(pady=10)
lastinput_label = tk.Label(root, text = "", fg="blue")
lastinput_label.pack(pady=5)

"""Where the analysis results are displayed"""
thisstatement_label = tk.Label(root, text="")
thisstatement_label.pack(pady=10)
output_label = tk.Label(root, text="", fg="orange")
output_label.pack(pady=5)

"""Continues running until the user exits"""
root.mainloop()



