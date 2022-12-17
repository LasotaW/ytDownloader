from downloader import Download
import tkinter as tk

class YtDownloader(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.lbl = tk.Label(text="Link do filmu YT: ")
        self.lbl.pack()

        self.urlEntry = tk.Entry(width=50)
        self.urlEntry.pack()

        self.downloadButton = tk.Button(text="Pobierz", command=self.download)
        self.downloadButton.pack()


    def download(self):
        link = self.urlEntry.get()
        self.messageLabel = tk.Label(text=Download(link))
        self.messageLabel.pack()
        self.urlEntry.delete(0, tk.END)

app = YtDownloader()

app.master.title("YT Downloader by BGDN v0.1")
app.master.geometry("400x150")
app.master.resizable(0, 0)

app.mainloop()