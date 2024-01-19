# GUI for GithubDNSUpdate

import tkinter as tk
from tkinter import ttk

import main


class GUI:
    # init
    NAME = "GithubHostUpdate"
    WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 400, 100
    ICO_PATH = "./GithubHostUpdate.ico"

    def __init__(self) -> None:
        self.build()
        self.frame()
        self.loop()

    def build(self) -> None:
        """build window"""
        # init window
        self.root = tk.Tk()

        # set window
        self.root.title(GUI.NAME)
        self.root.geometry(str(GUI.WINDOW_WIDTH)+'x'+str(GUI.WINDOW_HEIGHT))
        self.root.resizable(False, False)
        self.root.iconbitmap(GUI.ICO_PATH)

    def frame(self) -> None:
        """build frame"""
        # init info
        self.file_numbers = list(main.file.keys())
        self.file_numbers.append("custom")

        # set frame
        self.main_frame = tk.Frame(self.root)

        self.choose_file_label = tk.Label(self.main_frame, text="file")
        self.choose_file_combobox = ttk.Combobox(self.main_frame, values=self.file_numbers, width=50)
        self.choose_file_combobox.current(main.file_number-1)
        self.choose_file_combobox.bind('<<ComboboxSelected>>', self.changeFileInfoUrlEntryState)

        self.file_info_url_label = tk.Label(self.main_frame, text="url")
        self.file_info_url_entry_textvariable_StringVar = tk.StringVar()
        self.file_info_url_entry_textvariable_StringVar.set(value=main.file[int(self.choose_file_combobox.get())])
        self.file_info_url_entry = tk.Entry(self.main_frame, state=tk.DISABLED, width=50,
                                            textvariable=self.file_info_url_entry_textvariable_StringVar)

        self.start_button = tk.Button(self.main_frame, text="start", command=self.main)

        # display frame
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.choose_file_label.grid(row=0, column=0)
        self.choose_file_combobox.grid(row=0, column=1)

        self.file_info_url_label.grid(row=1, column=0)
        self.file_info_url_entry.grid(row=1, column=1)

        self.start_button.grid(row=2, column=0, columnspan=2)

    def loop(self) -> None:
        # loop window
        self.root.mainloop()

    def main(self) -> None:
        # run main function
        main.download(self.file_info_url_entry)
        main.writeToHostsFile()

    def changeFileInfoUrlEntryState(self, event: tk.Event) -> None:
        # change self.file_info_url_entry state
        if self.choose_file_combobox.get() == "custom":
            self.file_info_url_entry.config(state=tk.NORMAL)
            self.file_info_url_entry_textvariable_StringVar.set('')
        else:
            self.file_info_url_entry.config(state=tk.DISABLED)
            self.file_info_url_entry_textvariable_StringVar.set(value=main.file[int(self.choose_file_combobox.get())])


if __name__ == "__main__":
    GUI()
