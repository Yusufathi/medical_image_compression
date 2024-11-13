from src.util.dicom_visualizer import visualize_dicom
from src.scripts.dicom_metadata_viewer import show_dicom_metadata
if __name__ == "__main__":
    # visualize_dicom"src\datasets\CT\dicom_dir\ID_0000_AGE_0060_CONTRAST_1_CT.dcm")
    show_dicom_metadata(
        "src\datasets\CT\dicom_dir\ID_0000_AGE_0060_CONTRAST_1_CT.dcm")
