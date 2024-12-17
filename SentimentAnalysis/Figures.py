import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Track sentiment counts globally
sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}

def AnalyzeSentiment(userInput):
    """
    Analyzes the sentiment of the input text by comparing it to a list of positive and negative words.
    Returns 'positive', 'negative', or 'neutral' based on the word counts.
    """
    # Read positive and negative words from CSV files
    pw = pd.read_csv("POSITIVE_WORDS.csv", header=None)
    nw = pd.read_csv("NEGATIVE_WORDS.csv", header=None)
    
    pScore = 0  # Positive score
    nScore = 0  # Negative score
    
    # Split user input into words
    userWords = userInput.split()
    
    # Count positive and negative words in user input
    for word in userWords:
        for pWord in pw[0]:
            if word.lower() == pWord:
                pScore += 1
        for nWord in nw[0]:
            if word.lower() == nWord:
                nScore += 1
    
    pnRatio = 0
    # Calculate the ratio of positive to negative words, to check for neutrality
    if(pScore != 0 and nScore != 0):
        pnRatio = pScore / nScore

    # Return sentiment based on scores and ratio
    if pScore == nScore or (pnRatio > 0.8 and pnRatio < 1.2):
        return ('neutral')
    elif pScore > nScore:
        return ('positive')
    else:
        return ('negative')

def UpdateLastUserInput(userInput):
    """
    Updates the GUI with the user's input and the sentiment analysis result.
    Also updates the sentiment counts.
    """
    youtyped_label.config(text='You typed:')
    lastinput_label.config(text=f'{userInput}')
    thisstatement_label.config(text='This statement might be:')
    sentiment = AnalyzeSentiment(userInput)
    output_label.config(text=sentiment)
    update_sentiment_count(sentiment)

def AcceptInput():
    """
    Retrieves the user's input from the entry field, updates the sentiment analysis,
    and clears the entry field for the next input.
    """
    user_input = entry.get()
    UpdateLastUserInput(user_input)
    entry.delete(0, tk.END)

def update_sentiment_count(sentiment):
    """
    Updates the global sentiment counts based on the sentiment result and triggers the graph update.
    """
    global sentiment_counts
    sentiment_counts[sentiment] += 1
    plot_sentiment_graph()

def plot_sentiment_graph():
    """
    Plots the sentiment counts (positive, negative, neutral) as a bar graph using Matplotlib.
    Displays the graph in the Tkinter window.
    """
    fig, ax = plt.subplots()
    ax.bar(sentiment_counts.keys(), sentiment_counts.values(), color=['green', 'red', 'gray'])

    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Count')
    ax.set_title('Sentiment Analysis Results')

    # Display the graph in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

# Set up the Tkinter window and its components
root = tk.Tk()
root.title("Sentiment Analysis Chamber")
root.geometry("600x600")

label = tk.Label(root, text="Type anything and I will analyze it")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Analyze Sentiment", command=AcceptInput)
button.pack(pady=10)

youtyped_label = tk.Label(root, text="")
youtyped_label.pack(pady=10)
lastinput_label = tk.Label(root, text = "", fg="blue")
lastinput_label.pack(pady=5)

thisstatement_label = tk.Label(root, text="")
thisstatement_label.pack(pady=10)
output_label = tk.Label(root, text="", fg="orange")
output_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()

