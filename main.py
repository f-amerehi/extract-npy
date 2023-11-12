import os
import sys
import numpy as np
from PIL import Image

def save_images_from_npy(npy_file, output_dir):
    # Load the .npy file
    matrix = np.load(npy_file)

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Iterate through the images in the matrix
    for i, image in enumerate(matrix):
        # Convert the NumPy array to a PIL Image
        image_pil = Image.fromarray(image)

        # Generate the filename with padding
        filename = f"{i+1:04d}.png"

        # Save the image to the output directory
        image_pil.save(os.path.join(output_dir, filename))

def process_directory(input_directory, output_directory):
    # Iterate through all files in the input directory
    for filename in os.listdir(input_directory):
        # Check if the file is a .npy file
        if filename.endswith(".npy"):
            # Create the output directory name by removing the extension
            output_dir = os.path.join(output_directory, os.path.splitext(filename)[0])

            # Call the function to save images from the .npy file
            save_images_from_npy(os.path.join(input_directory, filename), output_dir)

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python main.py input_directory output_directory")
        sys.exit(1)

    # Get input and output directories from command line arguments
    input_directory = sys.argv[1]
    output_directory = sys.argv[2]

    # Call the function to process the directories
    process_directory(input_directory, output_directory)
