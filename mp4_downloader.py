import requests
import os

def download_terabox_video(video_url, output_folder):
    try:
        os.makedirs(output_folder, exist_ok=True)

        response = requests.get(video_url, stream=True)

        if response.status_code == 200:
            # Extract the video name from the URL or set a default name
            video_name = "downloaded_video_1.mp4" 
            video_path = os.path.join(output_folder, video_name)

            with open(video_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)

            print("Download completed!")
        else:
            print("Failed to retrieve the video. Status code:", response.status_code)

    except Exception as e:
        print(f"An error occurred: {e}")

# Sample command handling
video_url = input("Enter the Terabox video link: ")
output_folder = input("Enter the folder path to save the video: ")

download_terabox_video(video_url, output_folder)
