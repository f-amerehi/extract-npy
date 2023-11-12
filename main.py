import os
import sys
import numpy as np
from PIL import Image

def save_images_from_npy(npy_file, labels, output_root, label_padding):
    # Load the .npy file
    matrix = np.load(npy_file)

    # Create the output directory if it doesn't exist
    os.makedirs(output_root, exist_ok=True)

    # Iterate through the images in the matrix
    for i, (image, label) in enumerate(zip(matrix, labels)):
        # Convert the NumPy array to a PIL Image
        image_pil = Image.fromarray(image)

        # Generate the filename with padding
        filename = f"{i+1:04d}.png"

        # Create a subdirectory based on the padded label
        label_dir = os.path.join(output_root, str(label).zfill(label_padding))
        os.makedirs(label_dir, exist_ok=True)

        # Save the image to the subdirectory
        image_pil.save(os.path.join(label_dir, filename))

def process_directory(input_directory, output_root):
    # Load labels.npy
    labels_file = os.path.join(input_directory, 'labels.npy')
    if not os.path.exists(labels_file):
        print("Error: labels.npy file not found.")
        sys.exit(1)

    labels = np.load(labels_file)

    # Calculate the label padding based on the maximum label length
    label_padding = len(str(max(labels)))

    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        # Skip processing the labels.npy file
        if filename == 'labels.npy':
            continue

        # Check if the file is a .npy file
        if filename.endswith(".npy"):
            # Create the output directory name by removing the extension
            output_dir = os.path.join(output_root, os.path.splitext(filename)[0])

            # Call the function to save images from the .npy file with labels
            save_images_from_npy(os.path.join(input_directory, filename), labels, output_dir, label_padding)

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py input_directory output_root")
        sys.exit(1)

    # Get input and output directories from command line arguments
    input_directory = sys.argv[1]
    output_root = sys.argv[2]

    # Call the function to process the directories
    process_directory(input_directory, output_root)
