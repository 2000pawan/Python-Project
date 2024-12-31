import streamlit as st
from yt_dlp import YoutubeDL
import os
from PIL import Image

img=Image.open('img.jpeg')


# Function to download the video
def download_video(youtube_url, download_folder):
    if youtube_url != "" and download_folder != "":
        try:
            # Path to ffmpeg executable
            ffmpeg_path = r"B:\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin"  # Set the correct path to your FFmpeg folder

            # Configuring yt-dlp options with ffmpeg location
            ydl_opts = {
                'outtmpl': f'{download_folder}/%(title)s.%(ext)s',  # Set output template
                'format': 'bestvideo+bestaudio/best',  # Choose the best video and audio
                'ffmpeg_location': ffmpeg_path,  # Setting the FFmpeg location
            }

            # Using YoutubeDL to download the video
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([youtube_url])

            # Displaying a message indicating the successful download
            st.success(f"Video downloaded and saved successfully in {download_folder}")

        except Exception as e:
            # Displaying an error message in case of exceptions
            st.error(f"An error occurred: {e}")

    else:
        # Displaying an error message indicating empty fields
        st.error("Fields are empty!")

# Streamlit UI components
st.image(img,width=800)
st.title("YouTube Video Downloader...(@Pawan Yadav)...")

# URL input
video_url = st.text_input("Enter YouTube Video URL:")

# Folder input for download location
download_folder = st.text_input("Enter the folder to save the video (using\\ as path separator instead of /):")

# Download button
if st.button("Download"):
    download_video(video_url, download_folder)

# Clear button functionality
if st.button("Clear"):
    st.text_input("Enter YouTube Video URL:", value="")
    st.text_input("Enter the folder to save the video:", value="")
    st.experimental_rerun()  # Clear inputs and refresh

