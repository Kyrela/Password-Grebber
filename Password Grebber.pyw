"""
The GUI version of Password Grebber
"""


from functools import partial
import tkinter as tk
from tkinter import ttk
import os
import sys
import generator as core
import datetime as dt
from language import Language


def get_path(relative_path: str) -> str:
    """
    Transform the given relative path to an absolute path

    :param relative_path: the relative path to absolute
    :return: the absolute path
    """

    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


lang = Language(get_path("assets/languages.json"))


def logger(log: tk.Label, text: str) -> None:
    """
    logs informations in the footer and in the console

    :param log: the label where the text should be put
    :param text: the text to log
    :return: None
    """

    print(f"[{dt.datetime.now()}] {text}")
    log.configure(text=text)


def paste(window: tk.Tk, string_var: tk.StringVar, log: tk.Label) -> None:
    """
    Paste the text in the clipboard in the given StringVar

    :param window: the window from where the clipboard is get
    :param string_var: the string variable where the clipboard content is pasted
    :param log: the label where the logging infos whould be
    :return: None
    """

    try:
        clipboard_key = window.clipboard_get()
        string_var.set(clipboard_key)
        logger(log, lang.pasted_log.format(repr(clipboard_key)))
    except:
        logger(log, lang.empty_clipboard_log)


def generate(window: tk.Tk, string_var: tk.StringVar, mode: tk.IntVar, log: tk.Label) -> None:
    """
    Generate and copy the password to the clipboard

    :param window: the window from where the clipboard is get
    :param string_var: the string variable where the key is get
    :param mode: the mode of the password generation
    :param log: the label where the logging infos whould be
    :return: None
    """

    gen_key = string_var.get()
    if not gen_key:
        paste(window, string_var, log)
        gen_key = string_var.get()
    if gen_key:
        gen_key = core.generate(gen_key, mode.get())
        window.clipboard_clear()
        window.clipboard_append(gen_key)
        logger(log, lang.generation_log.format(repr(string_var.get()), repr(core.modes[mode.get()])))
    else:
        logger(log, lang.empty_key_log)


def main() -> None:
    """
    The main code of the program

    :return: None
    """

    window = tk.Tk()
    window.title(lang.app_name)
    window.resizable(False, False)

    window.call('wm', 'iconphoto', window._w, tk.PhotoImage(file=get_path('assets/logo.png')))

    body = tk.Frame(window)
    body.pack()
    footer = tk.Frame(window, background='white', height=17)
    footer.pack_propagate(0)
    footer.pack(fill=tk.X)

    img = tk.PhotoImage(file=get_path('assets/info.png'))
    tk.Label(footer, image=img, background='white').pack(side='left')

    log = tk.Label(footer, text="...", bg='white', anchor="w")
    log.pack(side='left')

    string_var = tk.StringVar()
    string_var.set("")
    text_field = ttk.Entry(body, width=45, textvariable=string_var)
    text_field.pack(pady=30, padx=80)
    text_field.focus()

    radio_frame = tk.Frame(body)
    radio_frame.pack()

    mode = tk.IntVar(value=0)

    for index, elem in enumerate(core.modes):
        ttk.Radiobutton(radio_frame, text=elem, variable=mode, value=index).pack(fill=tk.X)

    button_frame = tk.Frame(body)
    button_frame.pack(pady=30)

    ttk.Button(
        button_frame, text=lang.generation_button, command=partial(generate, window, string_var, mode, log), width=15
    ).pack(side="left", padx=15)
    ttk.Button(
        button_frame, text=lang.paste_button, command=partial(paste, window, string_var, log), width=15
    ).pack(side="right", padx=15)

    def on_key_press(event: tk.Event) -> None:
        """
        The triggered function when a keyboard key is pressed

        :param event: the pressed key
        :return: None
        """

        if event.char == "\n" or event.char == "\r":
            generate(window, string_var, mode, log)

    window.bind('<KeyPress>', on_key_press)

    window.mainloop()


if __name__ == "__main__":
    main()
