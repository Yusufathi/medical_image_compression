import pydicom
import sys


def show_dicom_metadata(file_path):
    """
    Load and display all metadata from a DICOM file, handling binary data properly.

    Parameters:
        file_path (str): Path to the DICOM file.
    """
    try:
        # Load the DICOM file
        dicom_data = pydicom.dcmread(file_path)

        # Print DICOM metadata
        print(f"Metadata for {file_path}:\n")
        for element in dicom_data:
            # Check if the element contains pixel data or other binary large objects
            if element.VR in ['OB', 'OW', 'OF', 'OD', 'UN', 'UT'] and len(element.value) > 64:
                # Print a summary instead of the full binary data
                print(
                    f"{element.tag} - {element.name}: [Binary Data, Length: {len(element.value)} bytes]")
            else:
                # Print text or number-based metadata directly
                print(f"{element.tag} - {element.name}: {element.value}")

    except Exception as e:
        print(f"Error reading DICOM file: {e}")
