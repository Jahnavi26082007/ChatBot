import tkinter as tk
import ollama
def send_message():
    message = entry.get()
    if message == "":
        return
    chat.insert(tk.END, "You: " + message + "\n")
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": message}
        ]
    )
    reply = response["message"]["content"]
    chat.insert(tk.END, "Bot: " + reply + "\n\n")
    entry.delete(0, tk.END)
window = tk.Tk()
window.title("Ollama AI Chatbot")
window.geometry("600x500")
chat = tk.Text(window, height=25, width=70)
chat.pack(pady=10)
entry = tk.Entry(window, width=50)
entry.pack(side=tk.LEFT, padx=10)
button = tk.Button(window, text="Send", command=send_message)
button.pack(side=tk.LEFT)
window.mainloop()