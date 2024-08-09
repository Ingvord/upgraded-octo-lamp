import argparse
import requests
import termplotlib as tpl
import matplotlib.pyplot as plt
import numpy as np

def upload_image(url, image_path):
    with open(image_path, 'rb') as image_file:
        files = {'file': (image_path, image_file, 'image/png')}
        response = requests.post(url, files=files, headers={"accept": "application/json"})

    return response.json()

def show_histogram_plot(histogram_data):
    bins = np.arange(len(histogram_data))

    # Create a plot
    fig = tpl.figure()
    fig.hist(histogram_data, bins, orientation='vertical', force_ascii=False)
    fig.show()

def save_histogram_plot(histogram_data, output_path="histogram_plot.png"):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(histogram_data)), histogram_data, color='blue')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.title('Histogram of Image')
    plt.savefig(output_path)
    plt.close()
    print(f"Histogram plot saved to {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Client to send an image file to the server.')

    parser.add_argument('--image', type=str, required=True, help='The path to the image file')
    parser.add_argument('--url', type=str, required=True, help='URL of the processing endpoint')
    parser.add_argument('--histogram', type=str, required=True, help='The path to the output histogram file')

    print("Parsing arguments...")
    args = parser.parse_args()
    url = args.url
    image_path = args.image
    histogram_path = args.histogram
    print("Done.")

    print(f"Processing image {image_path} by sending it to {url}")
    response = upload_image(url, image_path)
    print(response)
    # Define the number of bins (x-axis)
    histogram = response['histogram']

    show_histogram_plot(histogram)

    save_histogram_plot(histogram, histogram_path)
