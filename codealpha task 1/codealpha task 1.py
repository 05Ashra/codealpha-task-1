# CodeAlpha Task 1: Language Translation Tool
# Developer: Janufar Fathima Ashra

from tkinter import *
from deep_translator import GoogleTranslator

# --- Window Setup ---
root = Tk()
root.title("Language Translation Tool - CodeAlpha")
root.geometry("500x400")
root.config(bg="#f0f0f0")

# --- Input Text Box ---
Label(root, text="Enter Text:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
input_text = Text(root, height=5, width=55)
input_text.pack(pady=5)

# --- Language Selection ---
Label(root, text="Translate From (source language):", bg="#f0f0f0", font=("Arial", 10)).pack()
src_lang = StringVar(root)
src_lang.set("english")

Label(root, text="Translate To (target language):", bg="#f0f0f0", font=("Arial", 10)).pack()
dest_lang = StringVar(root)
dest_lang.set("tamil")

# Dropdown menus (you can type any supported language manually)
Entry(root, textvariable=src_lang, width=30, font=("Arial", 10)).pack(pady=2)
Entry(root, textvariable=dest_lang, width=30, font=("Arial", 10)).pack(pady=2)

# --- Output Text Box ---
Label(root, text="Translated Text:", bg="#f0f0f0", font=("Arial", 12)).pack(pady=5)
output_text = Text(root, height=5, width=55)
output_text.pack(pady=5)

# --- Translate Function ---
def translate_text():
    try:
        text_to_translate = input_text.get("1.0", END).strip()
        if text_to_translate == "":
            output_text.delete("1.0", END)
            output_text.insert(END, "⚠ Please enter some text to translate.")
            return

        translated = GoogleTranslator(source=src_lang.get(), target=dest_lang.get()).translate(text_to_translate)
        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        output_text.delete("1.0", END)
        output_text.insert(END, f"❌ Error: {e}")

# --- Button ---
Button(root, text="Translate", command=translate_text, bg="#4CAF50", fg="white",
       font=("Arial", 12), relief="raised").pack(pady=10)

root.mainloop()