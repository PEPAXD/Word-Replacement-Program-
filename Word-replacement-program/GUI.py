import tkinter
import customtkinter
import lorem
import PyPDF4
from tkinter import filedialog

#Window ChangeText
class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry(f"{350}x{200}")
        self.resizable(False, False)

        # TEXT-LABEL
        self.label = customtkinter.CTkLabel(self, text="WORD-REPLACEMENT", font=("Arial Black", 22, "underline"))
        self.label.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

        # create text-entry 1
        self.entry1 = customtkinter.CTkEntry(self, placeholder_text=("Inserte una palabra del texto"), width=300, height=30, corner_radius=8)
        self.entry1.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        # create text-entry 2
        self.entry2 = customtkinter.CTkEntry(self, placeholder_text=("Inserte una palabra que reemplazara la anterior"), width=300, height=30, corner_radius=8)
        self.entry2.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

        def click_button_changeText():

            pdfText = app.textbox.get("1.0", tkinter.END)
            wordToReplace = self.entry1.get()
            wordReplacement = self.entry2.get()

            newTexto = pdfText.replace(wordToReplace, wordReplacement)

            # insert PDF text into textbox
            app.textbox.delete("1.0", tkinter.END)
            app.textbox.insert("1.0", newTexto)

        # create button change txt
        self.button = customtkinter.CTkButton(self, text="CHANGE WORDS", command=click_button_changeText)
        self.button.place(relx=0.27, rely=0.85, anchor=tkinter.CENTER)

        def click_button_savepdf():

            pdfText = app.textbox.get("1.0", tkinter.END)
            filename = "New-PDF"

            file = open(filename+".txt", "w")
            file.write(pdfText)
            exit()

        # create button
        self.button1 = customtkinter.CTkButton(self, text="SAVE PDF.TEXT", command=click_button_savepdf)
        self.button1.place(relx=0.73, rely=0.85, anchor=tkinter.CENTER)




#Main Window
class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configure window appearance
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")

        # configure window size
        self.geometry(f"{400}x{450}")
        self.resizable(False, False)

        # configure window title
        self.title("word-replacement 'By Mauro Pepa'")

        # create canvas
        self.frame = customtkinter.CTkFrame(self, corner_radius=30)
        self.frame.pack(fill="both", expand=True)
        self.frame.place(relx=0.07, rely=0.07, relwidth=0.87, relheight=0.87)

        # TEXT-LABEL
        self.label = customtkinter.CTkLabel(self.frame, text="PDF-PRINT-TEXT", font=("Arial Black", 22, "underline"))
        self.label.place(relx=0.5, rely=0.08, anchor=tkinter.CENTER)

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.frame, width=300, height=270)
        self.textbox.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # print loremText in textbox
        self.textbox.insert("0.0", "Lorem-text\n\n" + lorem.text() + "\n\n")

        # create button for pdf.file selection
        self.select_button = customtkinter.CTkButton(self.frame, text="ADD PDF", command=self.select_pdf)
        self.select_button.place(relx=0.27, rely=0.92, anchor=tkinter.CENTER)

        # create button for change txt
        self.string_input_button = customtkinter.CTkButton(self.frame, text="CHANGE TEXT", command=self.open_toplevel)
        self.string_input_button.place(relx=0.73, rely=0.92, anchor=tkinter.CENTER)

        self.toplevel_window = None

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed

        else:
            self.toplevel_window.focus()  # if window exists focus it

    # open window and get pdf.file path
    def select_pdf(self):
        # open file dialog and get file path
        file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        # read PDF file
        with open(file_path, 'rb') as file:
            reader = PyPDF4.PdfFileReader(file)
            # get text from PDF
            pdf_text = ""
            for i in range(reader.getNumPages()):
                page = reader.getPage(i)
                pdf_text += page.extractText()+"\n"
            # insert PDF text into textbox
            self.textbox.delete("1.0", tkinter.END)
            self.textbox.insert("1.0", pdf_text)

app = App()
app.mainloop()