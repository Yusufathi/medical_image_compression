# Region-based Improved Gradient Encoding and Decoding (RIGED)
# Based on: "Region-based Improved Gradient Encoding and Decoding (RIGED) - Sharma et al., 2020"

from method import CompressionMethodInterface
import time


class RIGEDCompression(CompressionMethodInterface):
    def compress(self):
        """
        Compress the image using the Region-based Improved Gradient Encoding and Decoding (RIGED) technique.

        This function should apply the RIGED approach, which is designed to 
        achieve near-lossless compression by focusing on regions of interest 
        and encoding gradient changes efficiently.

        Returns:
            Compressed data (implementation-specific format).
        """
        pass

    def decompress(self):
        """
        Decompress the image back to its near-original form using RIGED.

        This method should reverse the RIGED encoding process, restoring
        diagnostic-quality image data suitable for medical applications.

        Returns:
            Decompressed data (near-original image format).
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the compression method.

        Returns:
            str: "RIGED Compression Method"
        """
        pass

    def get_compression_ratio(self):
        """
        Calculate and return the compression ratio.

        The compression ratio is the ratio of the original image size to the
        compressed size, demonstrating the effectiveness of the RIGED method.

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
