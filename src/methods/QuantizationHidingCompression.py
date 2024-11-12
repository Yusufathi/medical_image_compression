# Downsampling and Upsampling with Quantization Hiding for Telemedicine
# Based on: "Downsampling and Upsampling with Quantization Hiding - Elhadad et al., 2024"

from method import CompressionMethodInterface
import time


class QuantizationHidingCompression(CompressionMethodInterface):
    def compress(self):
        """
        Compress the image using downsampling, upsampling, and quantization hiding.

        This function should apply downsampling and quantization hiding to
        reduce the image size while maintaining sufficient quality for telemedicine.

        Returns:
            Compressed data (implementation-specific format).
        """
        pass

    def decompress(self):
        """
        Decompress the image back to its original form, restoring hidden details.

        This method should reverse the downsampling and quantization hiding,
        restoring as much original detail as possible.

        Returns:
            Decompressed data (original or near-original image format).
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the compression method.

        Returns:
            str: "Quantization Hiding Compression Method"
        """
        pass

    def get_compression_ratio(self):
        """
        Calculate and return the compression ratio.

        The compression ratio is the ratio of the original image size to the
        compressed size, demonstrating the efficiency of quantization hiding.

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
