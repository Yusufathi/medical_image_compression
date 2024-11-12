import os
import pydicom
import matplotlib.pyplot as plt


def visualize_dicom(file_path):
    """
    Function to load and visualize a DICOM file.

    Parameters:
        file_path (str): Path to the DICOM file.
    """
    # Load the DICOM file
    dicom_data = pydicom.dcmread(file_path)

    # Extract the pixel array
    image = dicom_data.pixel_array

    # Display the image
    plt.imshow(image, cmap="gray")
    plt.title(f"DICOM Image - {os.path.basename(file_path)}")
    plt.axis("off")
    plt.show()
