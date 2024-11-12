# Adaptive ROI-Based Compression
# Based on: "Adaptive ROI-Based Compression - Fahrni et al., 2022"

from method import CompressionMethodInterface
import time


class AdaptiveROICompression(CompressionMethodInterface):
    def compress(self):
        """
        Compress the image using an Adaptive Region of Interest (ROI)-based approach.

        This function should selectively compress non-critical regions at a higher
        compression ratio while preserving regions of interest (ROIs) with greater
        accuracy. The adaptive approach should dynamically adjust compression 
        based on image content.

        Returns:
            Compressed data (implementation-specific format).
        """
        pass

    def decompress(self):
        """
        Decompress the image back to its original form, restoring the quality of ROIs.

        This method should restore the full image, maintaining high quality in 
        diagnostic-critical regions while decompressing less important regions at 
        a lower quality.

        Returns:
            Decompressed data (original or near-original image format).
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the compression method.

        Returns:
            str: "Adaptive ROI-Based Compression Method"
        """
        pass

    def get_compression_ratio(self):
        """
        Calculate and return the compression ratio.

        The compression ratio is the ratio of the original image size to the
        compressed size, demonstrating the efficiency of adaptive ROI compression.

        Returns:
            float: Compression ratio.
        """
        pass

    def get_compression_time(self):
        """
        Return the time taken to compress the image.

        This time should be measured within the compress() method.

        Returns:
            float: Compression time in seconds.
        """
        pass

    def get_decompression_time(self):
        """
        Return the time taken to decompress the image.

        This time should be measured within the decompress() method.

        Returns:
            float: Decompression time in seconds.
        """
        pass
