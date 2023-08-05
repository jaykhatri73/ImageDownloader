import urllib.request
import os


def download_image(url, save_directory):
    # Create the save directory if it doesn't exist
    os.makedirs(save_directory, exist_ok=True)

    # Get the filename from the URL
    filename = os.path.basename(url)

    try:
        # Download the image
        save_path = os.path.join(save_directory, filename)

        # Print the save path for debugging
        print('Save path:', save_path)
        urllib.request.urlretrieve(url, save_path)
        print('Image downloaded successfully!')
    except urllib.error.URLError:
        print('Failed to download image.')
    except IOError:
        print('Failed to save image.')


image_url = input('Enter the image URL or local file path: ')
save_directory = input(
    "Give your save path(Copy file directory from the computer): ")

# adding comment
download_image(image_url, save_directory)
