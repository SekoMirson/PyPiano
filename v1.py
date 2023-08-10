import tkinter as tk
import winsound

notlar = {
    "1": 261.63,  # C4
    "2": 293.66,  # D4
    "3": 329.63,  # E4
    "4": 349.23,  # F4
    "5": 392.00,  # G4
    "6": 440.00, 
    "7": 493.88, 
    "8": 523.25, 
    "9": 553.55
}

def cal(event):
    key = event.char.upper()
    if key in notlar:
        frequency = notlar[key]
        winsound.Beep(int(frequency), 300)  # 300 ms boyunca nota çal


root = tk.Tk()
root.title("PyPiano by SekoMirson")

label = tk.Label(root, text="123456789 tuşlarına basarak piyano çalabilirsiniz.")
label.pack(padx=25, pady=25)
root.bind("<Key>", cal)
root.mainloop()
