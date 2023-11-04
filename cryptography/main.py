#!/usr/bin/python3
import tkinter as tk
import tkinter.messagebox as tm
import cryptography as crypt

class MainuiApp:
    def __init__(self, master=None):
        # build ui
        self.main_window = tk.Tk() if master is None else tk.Toplevel(master)
        very_dark = "#D4A373"
        dark = "#CCD5AE"
        mid = "#DDA15E"
        very_light = "#FEFAE0"

        self.main_window.configure(
            height=200,
            background=very_dark,
            highlightbackground="#77adca",
            highlightcolor="#77adca",
            width=200)
        self.main_window.geometry("640x480")
        self.main_window.resizable(False, False)
        self.main_window.title("Cryptography")
        self.techniques = tk.StringVar(value='Caesar Cipher')
        __values = [
            'Caesar Cipher',
            'Keyword Cipher',
            'Giovanni’s Method',
            'Transposition Techniques']
        self.cryptography_option_menu = tk.OptionMenu(
            self.main_window, self.techniques, *__values, command=self.open_diff_cipher)
        self.cryptography_option_menu.configure(background=very_dark,font="{Times New Roman} 18 {bold}",foreground=very_light)
        self.cryptography_option_menu.place(
            anchor="center", relx=.5, rely=0.075, x=0, y=0)
        self.cryptography_options = self.main_window.nametowidget(
            self.cryptography_option_menu.menuname
        )
        self.cryptography_options.config(background=very_dark,font="{times new roman} 16", foreground=very_light)

        #-------caesar-------------
        self.caesar_frame = tk.Frame(self.main_window)
        self.caesar_frame.configure(background=very_dark, height=400, width=200)
        self.encrypt_button_c = tk.Button(self.caesar_frame)
        self.encrypt_button_c.configure(
            background=dark,
            font="{times} 16 {bold}",
            foreground=mid,
            text='Encrypt')
        self.encrypt_button_c.place(anchor="center", relx=.5, rely=.6, x=0, y=0)
        self.encrypt_button_c.bind("<Button>", self.encrypt_action, add="")

        self.shift_entry = tk.Entry(self.caesar_frame)
        self.shift_entry.configure(
            background=very_light,
            font="{times new roman} 16 {}",
            foreground=very_dark)
        self.shift_entry.place(
            anchor="center",
            relx=0.315,
            rely=0.26,
            x=0,
            y=0)
        self.shift_label = tk.Label(self.caesar_frame)
        self.shift_label.configure(
            background=very_dark,
            font="{times new roman} 16 {}",
            foreground=very_light,
            text='Shift:')
        self.shift_label.place(
            anchor="center",
            relx=0.17,
            rely=0.175,
            x=0,
            y=0)
        self.plaintext_label = tk.Label(self.caesar_frame)
        self.plaintext_label.configure(
            background=very_dark,
            font="{times new roman} 16 {}",
            foreground=very_light,
            text='Plaintext:')
        self.plaintext_label.place(
            anchor="center", relx=0.2, rely=.35, x=0, y=0)
        self.plaintext_entry_c = tk.Entry(self.caesar_frame)
        self.plaintext_entry_c.configure(
            background=very_light,
            font="{times} 16 {}",
            foreground=very_dark)
        self.plaintext_entry_c.place(
            anchor="center",
            relwidth=0.75,
            relx=.52,
            rely=0.45,
            x=0,
            y=0)
        self.answer_frame_c = tk.Frame(self.caesar_frame)
        self.answer_frame_c.configure(background=very_dark, height=200, width=200)
        self.ciphertext_label_c = tk.Label(self.answer_frame_c)
        self.ciphertext_label_c.configure(
            background=very_dark,
            font="{Times} 16 {}",
            foreground=very_light,
            text='Ciphertext:')
        self.ciphertext_label_c.place(
            anchor="center", relx=0.1, rely=.45, x=0, y=0)
        self.ciphertext_answer_c = tk.Label(self.answer_frame_c)
        self.ciphertext_answer_c.configure(
            background=very_dark,
            font="{Times} 12 {}",
            foreground=very_light,
            text='-')
        self.ciphertext_answer_c.place(
            anchor="center", relx=0.25, rely=.75, x=0, y=0)
        self.answer_frame_c.place(
            anchor="center",
            relheight=0.26,
            relwidth=0.73,
            relx=.5,
            rely=0.8,
            x=0,
            y=0)
        self.caesar_frame.pack(
            anchor="s",
            expand="true",
            fill="x",
            side="top")
        
        #self.caesar_frame.pack_forget()
        #----keyword------------------------------------------------------
        
        self.keyword_frame = tk.Frame(self.main_window)
        self.keyword_frame.configure(
            background=very_dark, height=400, width=200)
        self.encrypt_button_k = tk.Button(self.keyword_frame)
        self.encrypt_button_k.configure(
            background=dark,
            font="{times} 16 {bold}",
            foreground=mid,
            text='Encrypt')
        self.encrypt_button_k.place(anchor="center", relx=.5, rely=.6, x=0, y=0)
        self.encrypt_button_k.bind("<Button>", self.encrypt_action, add="")
        self.keyword_entry_k = tk.Entry(self.keyword_frame)
        self.keyword_entry_k.configure(
            background=very_light,
            font="{times new roman} 16 {}",
            foreground=very_dark)
        self.keyword_entry_k.place(
            anchor="center",
            relx=0.315,
            rely=0.26,
            x=0,
            y=0)
        self.keyword_label_k = tk.Label(self.keyword_frame)
        self.keyword_label_k.configure(
            background=very_dark,
            font="{times new roman} 16 {}",
            foreground=very_light,
            text='Keyword:')
        self.keyword_label_k.place(
            anchor="center", relx=0.2, rely=0.175, x=0, y=0)
        self.plaintext_label = tk.Label(self.keyword_frame)
        self.plaintext_label.configure(
            background=very_dark,
            font="{times new roman} 16 {}",
            foreground=very_light,
            text='Plaintext:')
        self.plaintext_label.place(
            anchor="center", relx=0.2, rely=.35, x=0, y=0)
        self.plaintext_entry_k = tk.Entry(self.keyword_frame)
        self.plaintext_entry_k.configure(
            background=very_light,
            font="{times} 16 {}",
            foreground=very_dark)
        self.plaintext_entry_k.place(
            anchor="center",
            relwidth=0.75,
            relx=.52,
            rely=0.45,
            x=0,
            y=0)
        self.answer_frame_k = tk.Frame(self.keyword_frame)
        self.answer_frame_k.configure(
            background=very_dark, height=200, width=200)
        self.ciphertext_label = tk.Label(self.answer_frame_k)
        self.ciphertext_label.configure(
            background=very_dark,
            font="{Times} 16 {}",
            foreground=very_light,
            text='Ciphertext:')
        self.ciphertext_label.place(
            anchor="center", relx=0.1, rely=.45, x=0, y=0)
        self.ciphertext_answer_k = tk.Label(self.answer_frame_k)
        self.ciphertext_answer_k.configure(
            background=very_dark,
            font="{Times} 16 {}",
            foreground=very_light,
            text='-')
        self.ciphertext_answer_k.place(
            anchor="center", relx=0.25, rely=.75, x=0, y=0)
        self.answer_frame_k.place(
            anchor="center",
            relheight=0.26,
            relwidth=0.73,
            relx=.5,
            rely=0.8,
            x=0,
            y=0)
        self.keyword_frame.pack(
            anchor="s",
            expand="true",
            fill="x",
            side="bottom")
        
        self.keyword_frame.pack_forget()


        #-------giovanni----

        self.giovanni_frame = tk.Frame(self.main_window)
        self.giovanni_frame.configure(
            background=very_dark, height=400, width=200)
        self.encrypt_button_g = tk.Button(self.giovanni_frame)
        self.encrypt_button_g.configure(
            background=dark,
            font="{times} 16 {bold}",
            foreground=mid,
            text='Encrypt')
        self.encrypt_button_g.place(
            anchor="center", relx=.5, rely=.6, x=0, y=0)
        self.encrypt_button_g.bind("<Button>", self.encrypt_action, add="")
        self.keyword_entry_g = tk.Entry(self.giovanni_frame)
        self.keyword_entry_g.configure(
            background=very_light,
            font="{times new roman} 16 {}",
            foreground=very_dark)
        self.keyword_entry_g.place(
            anchor="center", relx=0.315, rely=0.325, x=0, y=0)
        self.keyword_label_g = tk.Label(self.giovanni_frame)
        self.keyword_label_g.configure(
            background=very_dark,
            font="{times new roman} 16 {}",
            foreground=very_light,
            text='Keyword:')
        self.keyword_label_g.place(
            anchor="center", relx=0.21, rely=0.25, x=0, y=0)
        self.plaintext_label_g = tk.Label(self.giovanni_frame)
        self.plaintext_label_g.configure(
            background=very_dark,
            font="{times new roman} 16 {}",
            foreground=very_light,
            text='Plaintext:')
        self.plaintext_label_g.place(
            anchor="center", relx=0.21, rely=.4, x=0, y=0)
        self.plaintext_entry_g = tk.Entry(self.giovanni_frame)
        self.plaintext_entry_g.configure(
            background=very_light,
            font="{times} 16 {}",
            foreground=very_dark)
        self.plaintext_entry_g.place(
            anchor="center",
            relwidth=0.75,
            relx=.515,
            rely=0.475,
            x=0,
            y=0)
        self.key_letter_entry = tk.Entry(self.giovanni_frame)
        self.key_letter_entry.configure(
            background=very_light,
            font="{times new roman} 16 {}",
            foreground=very_dark)
        self.key_letter_entry.place(
            anchor="center", relx=0.315, rely=0.175, x=0, y=0)
        self.key_letter_label = tk.Label(self.giovanni_frame)
        self.key_letter_label.configure(
            background=very_dark,
            font="{times new roman} 16 {}",
            foreground=very_light,
            text='Key Letter:')
        self.key_letter_label.place(
            anchor="center", relx=0.215, rely=0.1, x=0, y=0)
        self.answer_frame_g = tk.Frame(self.giovanni_frame)
        self.answer_frame_g.configure(
            background=very_dark, height=200, width=200)
        self.ciphertext_label_g = tk.Label(self.answer_frame_g)
        self.ciphertext_label_g.configure(
            background=very_dark,
            font="{Times} 16 {}",
            foreground=very_light,
            text='Ciphertext:')
        self.ciphertext_label_g.place(
            anchor="center", relx=0.1, rely=.45, x=0, y=0)
        self.ciphertext_answer_g = tk.Label(self.answer_frame_g)
        self.ciphertext_answer_g.configure(
            background=very_dark,
            font="{Times} 12 {}",
            foreground=very_light,
            text='-')
        self.ciphertext_answer_g.place(anchor="center", relx=0.25, rely=.75, x=0, y=0)
        self.answer_frame_g.place(
            anchor="center",
            relheight=0.26,
            relwidth=0.73,
            relx=.5,
            rely=0.8,
            x=0,
            y=0)
        self.giovanni_frame.pack(
            anchor="s",
            expand="true",
            fill="x",
            side="bottom")

        self.giovanni_frame.pack_forget()

        #------transposition----
        self.transpo_frame = tk.Frame(self.main_window)
        self.transpo_frame.configure(
            background="#D4A373", height=400, width=200)
        self.encrypt_button_t = tk.Button(self.transpo_frame)
        self.encrypt_button_t.configure(
            background="#CCD5AE",
            font="{times} 16 {bold}",
            foreground="#DDA15E",
            text='Encrypt')
        self.encrypt_button_t.place(
            anchor="center", relx=.5, rely=.6, x=0, y=0)
        self.encrypt_button_t.bind("<Button>", self.encrypt_action, add="")
        self.plaintext_label_t = tk.Label(self.transpo_frame)
        self.plaintext_label_t.configure(
            background="#D4A373",
            font="{times new roman} 16 {}",
            foreground="#FEFAE0",
            text='Plaintext:')
        self.plaintext_label_t.place(
            anchor="center", relx=0.21, rely=.25, x=0, y=0)
        self.plaintext_entry_t = tk.Entry(self.transpo_frame)
        self.plaintext_entry_t.configure(
            background="#FEFAE0",
            font="{times} 16 {}",
            foreground="#D4A373")
        self.plaintext_entry_t.place(
            anchor="center",
            relwidth=0.75,
            relx=.515,
            rely=0.35,
            x=0,
            y=0)
        self.answer_frame_t = tk.Frame(self.transpo_frame)
        self.answer_frame_t.configure(
            background="#D4A373", height=200, width=200)
        self.ciphertext_label_t = tk.Label(self.answer_frame_t)
        self.ciphertext_label_t.configure(
            background="#D4A373",
            font="{Times} 16 {}",
            foreground="#FEFAE0",
            text='Ciphertext:')
        self.ciphertext_label_t.place(
            anchor="center", relx=0.1, rely=.45, x=0, y=0)
        self.ciphertext_answer_t = tk.Label(self.answer_frame_t)
        self.ciphertext_answer_t.configure(
            background="#D4A373",
            font="{Times} 12 {}",
            foreground="#FEFAE0",
            text='-')
        self.ciphertext_answer_t.place(
            anchor="center", relx=0.25, rely=.75, x=0, y=0)
        self.answer_frame_t.place(
            anchor="center",
            relheight=0.26,
            relwidth=0.73,
            relx=.5,
            rely=0.8,
            x=0,
            y=0)
        self.transpo_frame.pack(
            anchor="s",
            expand="true",
            fill="x",
            side="bottom")

        self.transpo_frame.pack_forget()

        # Main widget
        self.mainwindow = self.main_window

    def run(self):
        self.mainwindow.mainloop()

    def do_caesar_cipher(self):
        if (self.plaintext_entry_c.get().isalpha() or self.plaintext_entry_c.get() == "") and (self.shift_entry.get().isdigit() or self.shift_entry.get() == ""):
            ciphertext = crypt.caeasar_shift(self.plaintext_entry_c.get(), self.shift_entry.get()) 
            self.ciphertext_answer_c.config(text=ciphertext)
        else:  
            tm.showerror(title=None, message="Use Number for Shift; Letters for Plaintext")

    def do_keyword_cipher(self):
        if (self.plaintext_entry_k.get().isalpha() or self.plaintext_entry_k.get() == "") and (self.keyword_entry_k.get().isalpha() or self.keyword_entry_k.get() == ""):
            ciphertext = crypt.keyword_cipher_encrypt(self.plaintext_entry_k.get(), self.keyword_entry_k.get())
            self.ciphertext_answer_k.config(text=ciphertext)
        else:  
            tm.showerror(title=None, message="Use Letters for Plaintext and Keyword")

    def do_giovannis_method(self):
        if ((self.plaintext_entry_g.get().isalpha() or self.plaintext_entry_g.get() == "") and (self.keyword_entry_g.get().isalpha() or self.keyword_entry_g.get() == "") 
        and (self.key_letter_entry.get().isalpha() or self.key_letter_entry.get() == "")):
            ciphertext = crypt.giovanni_cipher(self.plaintext_entry_g.get(), self.keyword_entry_g.get(),self.key_letter_entry.get())
            self.ciphertext_answer_g.config(text=ciphertext)
        else:  
            tm.showerror(title=None, message="Use Number for Shift; Letters for Plaintext")

    def do_transposition_tech(self):
        if (self.plaintext_entry_t.get().isalpha() or self.plaintext_entry_t.get() == ""):
            ciphertext = crypt.transposition(self.plaintext_entry_t.get())
            self.ciphertext_answer_t.config(text=ciphertext)
        




    def encrypt_action(self, event=None):
        if self.techniques.get() == 'Caesar Cipher':
            self.do_caesar_cipher()
        if self.techniques.get() == 'Keyword Cipher':
            self.do_keyword_cipher()
        if self.techniques.get() == 'Giovanni’s Method':
            self.do_giovannis_method()
        if self.techniques.get() == 'Transposition Techniques':
            self.do_transposition_tech()

    def open_diff_cipher(self, event=None):
        if self.techniques.get() == 'Caesar Cipher':
            self.caesar_frame.pack(
                anchor="s",
                expand="true",
                fill="x",
                side="top")
            self.keyword_frame.pack_forget()
            self.giovanni_frame.pack_forget()
            self.transpo_frame.pack_forget()

        if self.techniques.get() == 'Keyword Cipher':
            self.keyword_frame.pack(
                anchor="s",
                expand="true",
                fill="x",
                side="bottom")
            self.caesar_frame.pack_forget()
            self.giovanni_frame.pack_forget()
            self.transpo_frame.pack_forget()

        if self.techniques.get() == 'Giovanni’s Method':
            self.caesar_frame.pack_forget()
            self.keyword_frame.pack_forget()
            self.giovanni_frame.pack(
                anchor="s",
                expand="true",
                fill="x",
                side="bottom")
            self.transpo_frame.pack_forget()
        if self.techniques.get() == 'Transposition Techniques':
            self.caesar_frame.pack_forget()
            self.keyword_frame.pack_forget()
            self.giovanni_frame.pack_forget()
            self.transpo_frame.pack(
                anchor="s",
                expand="true",
                fill="x",
                side="bottom")



if __name__ == "__main__":
    app = MainuiApp()
    app.run()
