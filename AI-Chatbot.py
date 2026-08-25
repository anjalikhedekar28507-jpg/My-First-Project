import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime


# ---------------- CHATBOT LOGIC ----------------

def chatbot_response(user_input):
    text = user_input.lower().strip()

    if text in ["hello", "hi", "hey", "hii"]:
        return "Hello! 👋 How can I help you?"

    elif "your name" in text or "who are you" in text:
        return "I am an AI Chatbot created using Python."

    elif "how are you" in text:
        return "I am doing great! 😊 Thanks for asking."

    elif "time" in text:
        return "Current time is " + datetime.now().strftime("%I:%M %p")

    elif "date" in text or "today" in text:
        return "Today's date is " + datetime.now().strftime("%d-%m-%Y")

    elif "ai" in text or "artificial intelligence" in text:
        return (
            "AI stands for Artificial Intelligence. "
            "It allows computers to perform tasks that normally require human intelligence."
        )

    elif "python" in text:
        return (
            "Python is a popular programming language used "
            "for AI, Data Science, Web Development and Automation."
        )

    elif "machine learning" in text:
        return (
            "Machine Learning is a branch of AI that allows computers "
            "to learn from data and make predictions."
        )

    elif "computer" in text:
        return (
            "A computer is an electronic device that processes data "
            "and produces useful information."
        )

    elif "help" in text:
        return (
            "You can ask me about AI, Python, Machine Learning, "
            "Computer, Date or Time."
        )

    elif "thank" in text:
        return "You're welcome! 😊"

    elif "bye" in text or "goodbye" in text:
        return "Goodbye! 👋 Have a great day!"

    else:
        return (
            "Sorry, I don't understand that yet. 🤔\n"
            "Try asking about AI, Python, Machine Learning, Date or Time."
        )


# ---------------- SEND MESSAGE ----------------

def send_message(event=None):
    user_input = entry.get().strip()

    if user_input == "":
        return

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(tk.END, "You: " + user_input + "\n")

    response = chatbot_response(user_input)

    chat_area.insert(tk.END, "Bot: " + response + "\n\n")

    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)

    entry.delete(0, tk.END)


# ---------------- CLEAR CHAT ----------------

def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete("1.0", tk.END)

    chat_area.insert(
        tk.END,
        "Bot: Hello! 👋 Welcome to AI Chatbot.\n"
        "Bot: How can I help you?\n\n"
    )

    chat_area.config(state=tk.DISABLED)


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()

root.title("AI Chatbot - Python Project")
root.geometry("650x700")
root.resizable(False, False)


# ---------------- TITLE ----------------

title = tk.Label(
    root,
    text="🤖 AI CHATBOT",
    font=("Arial", 26, "bold")
)

title.pack(pady=15)


subtitle = tk.Label(
    root,
    text="Artificial Intelligence Chatbot using Python",
    font=("Arial", 11)
)

subtitle.pack()


# ---------------- CHAT AREA ----------------

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 12),
    width=65,
    height=27
)

chat_area.pack(padx=15, pady=15)

chat_area.config(state=tk.DISABLED)


# ---------------- INPUT FRAME ----------------

input_frame = tk.Frame(root)

input_frame.pack(pady=5)


entry = tk.Entry(
    input_frame,
    font=("Arial", 14),
    width=40
)

entry.grid(row=0, column=0, padx=5)


send_button = tk.Button(
    input_frame,
    text="Send",
    font=("Arial", 12, "bold"),
    command=send_message
)

send_button.grid(row=0, column=1, padx=5)


# ---------------- CLEAR BUTTON ----------------

clear_button = tk.Button(
    root,
    text="Clear Chat",
    font=("Arial", 11, "bold"),
    command=clear_chat
)

clear_button.pack(pady=10)


# ---------------- WELCOME MESSAGE ----------------

chat_area.config(state=tk.NORMAL)

chat_area.insert(
    tk.END,
    "Bot: Hello! 👋 Welcome to AI Chatbot.\n"
    "Bot: Ask me anything about AI, Python, Machine Learning, Date or Time.\n\n"
)

chat_area.config(state=tk.DISABLED)


# ---------------- ENTER KEY ----------------

root.bind("<Return>", send_message)


# ---------------- START CHATBOT ----------------

entry.focus()

root.mainloop()