import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pyttsx3

class TextToSpeechApp:
    def __init__(self, master):
        self.master = master
        master.title("Text-to-Speech App")

        # Load the background image
        self.bg_image = Image.open("C:/Users/ADMIN/Downloads/images.png")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)
        
        # Create a canvas to put the background image on
        self.canvas = tk.Canvas(master, width=self.bg_image.width, height=self.bg_image.height)
        self.canvas.pack()

        # Place the background image on the canvas
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor=tk.NW)

        # Text entry field
        self.text_entry = tk.Text(master, height=10, width=50)
        self.text_entry.pack()

        # Language selection dropdown
        self.language_label = tk.Label(master, text="Select Language:")
        self.language_label.pack()
        self.language_var = tk.StringVar()
        self.language_dropdown = tk.OptionMenu(master, self.language_var, "English", "French", "German")  # Add more languages as needed
        self.language_dropdown.pack()

        # Voice selection dropdown
        self.voice_label = tk.Label(master, text="Select Voice:")
        self.voice_label.pack()
        self.voice_var = tk.StringVar()
        self.voice_dropdown = tk.OptionMenu(master, self.voice_var, "male", "female")  # Add more voices as needed
        self.voice_dropdown.pack()

        # Rate adjustment scale
        self.rate_label = tk.Label(master, text="Speech Rate:")
        self.rate_label.pack()
        self.rate_scale = tk.Scale(master, from_=50, to=300, orient=tk.HORIZONTAL)
        self.rate_scale.pack()

        # Pitch adjustment scale
        self.pitch_label = tk.Label(master, text="Pitch:")
        self.pitch_label.pack()
        self.pitch_scale = tk.Scale(master, from_=0, to=200, orient=tk.HORIZONTAL)
        self.pitch_scale.pack()

        # Volume adjustment scale
        self.volume_label = tk.Label(master, text="Volume:")
        self.volume_label.pack()
        self.volume_scale = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL)
        self.volume_scale.pack()

        # Play button
        self.play_button = tk.Button(master, text="Play", command=self.play_text)
        self.play_button.pack()

        # Stop button
        self.stop_button = tk.Button(master, text="Stop", command=self.stop_text)
        self.stop_button.pack()

        # Save audio button
        self.save_button = tk.Button(master, text="Save Audio", command=self.save_audio)
        self.save_button.pack()

        # Initialize pyttsx3 engine
        self.engine = pyttsx3.init()

    def play_text(self):
        text = self.text_entry.get("1.0", "end-1c")
        language = self.language_var.get()
        voice = self.voice_var.get()
        rate = self.rate_scale.get()
        pitch = self.pitch_scale.get()
        volume = self.volume_scale.get()

        # Set speech parameters
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume/100)
        self.engine.setProperty('voice', voice)
        
        # Convert text to speech
        self.engine.say(text)
        self.engine.runAndWait()

    def stop_text(self):
        self.engine.stop()

    def save_audio(self):
        text = self.text_entry.get("1.0", "end-1c")
        file_path = "output.mp3"  # Change the file extension as needed
        self.engine.save_to_file(text, file_path)
        self.engine.runAndWait()

root = tk.Tk()
app = TextToSpeechApp(root)
root.mainloop()
