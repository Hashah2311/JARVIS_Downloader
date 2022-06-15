def main():
    import requests as r
    import tkinter as tk
    from tkinter import Label, Entry, Button, GROOVE, StringVar
    import zipfile as zip
    from tkinter import messagebox, filedialog
    root = tk.Tk()
    def Widgets():
        head_label = Label(root, text="JARVIS Downloader",
                           padx=15,
                           pady=15,
                           font="SegoeUI 14",
                           bg="yellow",
                           fg="red")
        head_label.grid(row=1,
                        column=1,
                        pady=10,
                        padx=5,
                        columnspan=3)
        Plugins_label = Label(root,
                           text="Additonal Plugins :",
                           bg="salmon",
                           pady=5,
                           padx=5)
        Plugins_label.grid(row=2,
                        column=0,
                        pady=5,
                        padx=5)
        root.linkText = Entry(root,
                              width=35,
                              textvariable=Plugins_name,
                              font="Arial 14")
        root.linkText.grid(row=2,
                           column=1,
                           pady=5,
                           padx=5,
                           columnspan=2)
        destination_label = Label(root,
                                  text="Where To Install JARVIS :",
                                  bg="salmon",
                                  pady=5,
                                  padx=9)
        destination_label.grid(row=3,
                               column=0,
                               pady=5,
                               padx=5)
        root.destinationText = Entry(root,
                                     width=27,
                                     textvariable=install_Path,
                                     font="Arial 14")
        root.destinationText.grid(row=3,
                                  column=1,
                                  pady=5,
                                  padx=5)
        browse_B = Button(root,
                          text="Browse",
                          command=Browse,
                          width=10,
                          bg="bisque",
                          relief=GROOVE)
        browse_B.grid(row=3,
                      column=2,
                      pady=1,
                      padx=1)
        Download_B = Button(root,
                            text="Start Download",
                            command=Download,
                            width=20,
                            bg="thistle1",
                            pady=10,
                            padx=15,
                            relief=GROOVE,
                            font="Georgia, 13")
        Download_B.grid(row=4,
                        column=1,
                        pady=20,
                        padx=20)
    def Browse():
        download_Directory = filedialog.askdirectory(initialdir="C:\\Program Files\\JARVIS", title="Choose Location TO INSTALL JARVIS")
        install_Path.set(f"{download_Directory}")
    def Download():
        JARVIS_Download_link = "https://github.com/Hashah2311/JARVIS/releases/download/V-beta-4.5/JARVIS.V-0.4.5.zip"
        file = r.get(JARVIS_Download_link, stream = True, allow_redirects=True)
        install_Folder = install_Path.get()
        with open("JARVIS.zip", "wb") as JARVIS:
            for chunk in file.iter_content(chunk_size=1024):
                if chunk:
                    JARVIS.write(chunk)
        try:
            with zip.ZipFile("JARVIS.zip") as z:
                z.extractall(install_Folder)
                messagebox.showinfo("SUCCESSFULl", f"DOWNLOADED AND INSTALLED IN\n {install_Folder}")
                if Plugins_name != None:
                    messagebox.showinfo("ERROR", "PLUGIN INSTALLATION NOT SUPPORTED YET")
        except:
            messagebox.showinfo("ERROR", "TRY AGAIN")
            exit()
    root.geometry("570x250")
    root.resizable(True, True)
    root.title("JARVIS Downloader")
    root.config(background="Red")
    Plugins_name = StringVar()
    install_Path = StringVar()
    Widgets()
    root.mainloop()