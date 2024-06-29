from tkinter import *
from tkinter import ttk, messagebox
from googletrans import LANGUAGES, Translator
import textblob
from PIL import Image, ImageTk

# Extract languages from googletrans LANGUAGES dictionary
language_list = list(LANGUAGES.values())

def trans_late():
    txt2.delete(1.0, END)
    try:
        for key, value in LANGUAGES.items():
            if value == c1.get():
                from_language_key = key
        for key, value in LANGUAGES.items():
            if value == c2.get():
                to_language_key = key

        words = textblob.TextBlob(txt1.get(1.0, END))
        words = words.translate(from_lang=from_language_key, to=to_language_key)
        txt2.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)
# Function to swap languages
def swap_languages():
    c1_value = c1.get()
    c2_value = c2.get()
    c1.set(c2_value)
    c2.set(c1_value)


root = Tk()
root.geometry("700x400")
root.title("Language Translator")
root.config(bg='#D3D3D3')

Label(root, text="Language Translator-by Harsh Kumar", font=('Arial,bold', 20), bg='#8B8B7A', fg='White', width=50, pady=5).pack(pady=10)

f1 = Frame(root, width=320, height=200, bg='white', bd=5)
f1.place(x=15, y=70)
f2 = Frame(root, width=320, height=200, bg='white', bd=5)
f2.place(x=360, y=70)

txt1 = Text(f1, font=('Arial,bold'), width=28, height=8)
txt1.place(x=0, y=0)
txt2 = Text(f2, font=('Arial,bold'), width=28, height=8)
txt2.place(x=0, y=0)

c1 = ttk.Combobox(root, values=language_list, font=('Arial,bold', 12), width=20)
c1.place(x=60, y=290)
c2 = ttk.Combobox(root, values=language_list, font=('Arial,bold', 12), width=20)
c2.place(x=420, y=290)

# Swap button
swap_image = Image.open('swap_icon.jpg').resize((20, 20), Image.LANCZOS)
swap_icon = ImageTk.PhotoImage(swap_image)
swap_button = Button(root, image=swap_icon, bd=0, bg='#F0F0F0', command=swap_languages)
swap_button.place(x=336, y=170)

btn = Button(root, text="Translate", font=('Arial,bold', 15), bd=5, bg='#8B8B7A', fg='White', command=trans_late)
btn.place(x=290, y=320)

root.mainloop()
