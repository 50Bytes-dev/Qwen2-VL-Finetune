import os
import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


def download_image(url, folder):
    try_count = 0
    error = None
    while True:
        try:
            # Extract image name from URL
            image_name = url.split("/")[-1].split("?")[0]
            image_path = os.path.join(folder, image_name)

            if os.path.exists(image_path):
                return f"Image already exists: {image_name}"

            # Get the image content
            response = requests.get(url, stream=True, timeout=5)
            response.raise_for_status()

            # Save the image to the specified folder
            with open(image_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return f"Downloaded: {image_name}"
        except Exception as e:
            try_count += 1

            if os.path.exists(image_path):
                os.remove(image_path)

            if try_count >= 3:
                error = e
                break

            time.sleep(0.25)

    return f"Failed to download {url}: {error}"


def download_images(image_urls, folder, max_workers=10):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Use ThreadPoolExecutor for concurrent downloads
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit download tasks
        futures = [executor.submit(download_image, url, folder) for url in image_urls]

        # Process as tasks complete
        count = 0
        for future in as_completed(futures):
            count += 1
            print(f"[{count}/{len(image_urls)}] " + future.result())


if __name__ == "__main__":
    # Example list of image URLs

    file = "images.txt"

    with open(file, "r") as f:
        image_urls = f.readlines()

    image_urls = [url.strip() for url in image_urls]

    # Folder to save images
    download_folder = "data/images"

    # Start downloading images
    download_images(image_urls, download_folder, max_workers=40)
