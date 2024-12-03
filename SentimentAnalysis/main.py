import pandas as pd
import tkinter as tk

def AcceptInput():
    user_input = entry.get()
    output_label = (AnalyzeSentiment(user_input))
    entry.delete(0, tk.END)

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
    
    return (f'Positive: {pScore}, Negative: {nScore}')


root = tk.Tk()
root.title("Enter Here")
root.geometry("400x200")


label = tk.Label(root, text="Type anything and I will analyze it")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Analyze Sentiment", command=AcceptInput)
button.pack(pady=10)

output_label = tk.Label(root, text="", fg="blue")
output_label.pack(pady=10)

root.mainloop()



