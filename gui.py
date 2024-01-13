# GUI for GithubDNSUpdate

import tkinter as tk
from tkinter import ttk

import main


class GUI:
    # init
    NAME = "GithubDNSUpdate"
    WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 300, 100

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
        self.root.iconbitmap("GithubDNSUpdate.ico")

    def frame(self) -> None:
        """build frame"""
        # set frame
        self.main_frame = ttk.Frame(self.root)

        self.choose_file_label = ttk.Label(self.main_frame, text="file")
        self.choose_file_combobox = ttk.Combobox(self.main_frame, values=tuple(main.file.keys()))
        self.choose_file_combobox.current(main.file_number-1)

        self.start_button = ttk.Button(self.main_frame, text="start", command=self.main)

        # display frame
        self.main_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.choose_file_label.grid(row=0, column=0)
        self.choose_file_combobox.grid(row=0, column=1)

        self.start_button.grid(row=1, column=0, columnspan=2)

    def loop(self) -> None:
        # loop window
        self.root.mainloop()

    def main(self) -> None:
        # run main function
        main.UpdateFile(int(self.choose_file_combobox.get()))
        main.download()
        main.writeToHostsFile()
        main.deleteFile()


if __name__ == "__main__":
    GUI()