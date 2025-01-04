# Importing the necessary modules
from tkinter import *  # importing all widgets and modules from tkinter
from tkinter import messagebox as mb  # importing the messagebox module from tkinter
from tkinter import filedialog as fd  # importing the filedialog module from tkinter
from yt_dlp import YoutubeDL  # importing YoutubeDL from yt-dlp

# ------------------------- defining functions -------------------------  

# Function to browse the folder
def browse_folder():
    download_path = fd.askdirectory(initialdir="D:/Downloads", title="Select the folder to save the music")
    download_dir.set(download_path)

# Function to download music to the designated path
def download_music():
    youtube_url = video_url.get()
    download_folder = download_dir.get()

    # Check if the entry fields are not empty
    if youtube_url != "" and download_folder != "":
        try:
            # Path to FFmpeg executable
            ffmpeg_path = r"B:\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin"  # Update with your FFmpeg path

            # Configure yt-dlp options for audio download
            ydl_opts = {
                'format': 'bestaudio/best',  # Download the best available audio
                'outtmpl': f'{download_folder}/%(title)s.%(ext)s',  # Save with the title as the filename
                'ffmpeg_location': ffmpeg_path,  # Specify FFmpeg path
                'postprocessors': [{  # Use postprocessors to convert to MP3
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',  # Set preferred audio codec
                    'preferredquality': '192',  # Set audio quality
                }],
            }

            # Use YoutubeDL to download the audio
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([youtube_url])

            # Display a success message
            mb.showinfo("Download Complete", f"Selected music is downloaded\nand saved successfully in {download_folder}")

        except Exception as e:
            # Display an error message in case of exceptions
            mb.showerror("Download Error", f"An error occurred: {e}")

    else:
        # Display an error message indicating empty fields
        mb.showerror("Empty Fields", "Fields are empty!")

# Function to reset the entries
def reset():
    video_url.set("")
    download_dir.set("")
    url_field.focus_set()

# Function to close the application
def exit():
    gui_root.destroy()

# ------------------------- main function -------------------------  
if __name__ == "__main__":
    gui_root = Tk()
    gui_root.title("YouTube Music Downloader Developed @ PAWAN YADAV")
    gui_root.geometry("580x220+700+250")
    gui_root.resizable(0, 0)
    gui_root.config(bg="#FEE4E3")

    # Adding frames
    header_frame = Frame(gui_root, bg="#FEE4E3")
    entry_frame = Frame(gui_root, bg="#FEE4E3")
    button_frame = Frame(gui_root, bg="#FEE4E3")
    header_frame.pack()
    entry_frame.pack()
    button_frame.pack()

    # Header Frame
    header_label = Label(
        header_frame,
        text="YouTube Music Downloader",
        font=("verdana", "16", "bold"),
        bg="#FEE4E3",
        anchor=SE
    )
    header_label.grid(row=0, column=1, padx=10, pady=10)

    # Entry Frame
    url_label = Label(
        entry_frame,
        text="Video URL:",
        font=("verdana", "12"),
        bg="#FEE4E3",
        fg="#000000",
        anchor=SE
    )
    des_label = Label(
        entry_frame,
        text="Destination:",
        font=("verdana", "12"),
        bg="#FEE4E3",
        fg="#000000",
        anchor=SE
    )
    url_label.grid(row=0, column=0, padx=5, pady=5, sticky=E)
    des_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    # StringVar for input fields
    video_url = StringVar()
    download_dir = StringVar()

    # Entry Fields
    url_field = Entry(
        entry_frame,
        textvariable=video_url,
        width=35,
        font=("verdana", "10"),
        bg="#FFFFFF",
        fg="#000000",
        relief=GROOVE
    )
    des_field = Entry(
        entry_frame,
        textvariable=download_dir,
        width=26,
        font=("verdana", "10"),
        bg="#FFFFFF",
        fg="#000000",
        relief=GROOVE
    )
    url_field.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
    des_field.grid(row=1, column=1, padx=5, pady=5)

    browse_button = Button(
        entry_frame,
        text="Browse",
        width=7,
        font=("verdana", "10"),
        bg="#FF9200",
        fg="#FFFFFF",
        activebackground="#FFE0B7",
        activeforeground="#000000",
        relief=GROOVE,
        command=browse_folder
    )
    browse_button.grid(row=1, column=2, padx=5, pady=5)

    # Button Frame
    download_button = Button(
        button_frame,
        text="Download Music",
        width=12,
        font=("verdana", "10"),
        bg="#15EF5F",
        fg="#FFFFFF",
        activebackground="#97F9B8",
        activeforeground="#000000",
        relief=GROOVE,
        command=download_music
    )
    reset_button = Button(
        button_frame,
        text="Clear",
        width=12,
        font=("verdana", "10"),
        bg="#23B1E6",
        fg="#FFFFFF",
        activebackground="#C3E6EF",
        activeforeground="#000000",
        relief=GROOVE,
        command=reset
    )
    close_button = Button(
        button_frame,
        text="Exit",
        width=12,
        font=("verdana", "10"),
        bg="#F64247",
        fg="#FFFFFF",
        activebackground="#F7A2A5",
        activeforeground="#000000",
        relief=GROOVE,
        command=exit
    )
    download_button.grid(row=0, column=0, padx=5, pady=10)
    reset_button.grid(row=0, column=1, padx=5, pady=10)
    close_button.grid(row=0, column=2, padx=5, pady=10)

    gui_root.mainloop()
