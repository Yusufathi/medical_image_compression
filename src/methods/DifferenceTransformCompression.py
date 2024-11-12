# Lossless Compression using Difference Transform
# Based on: "Lossless Compression using Difference Transform - Rojas-Hernández et al., 2022"

from method import CompressionMethodInterface
import time


class DifferenceTransformCompression(CompressionMethodInterface):
    def compress(self):
        """
        Compress the image using a difference transform-based approach.

        The difference transform encodes the differences between neighboring 
        pixels or blocks to reduce redundancy and achieve lossless compression.

        Returns:
            Compressed data (implementation-specific format).
        """
        pass

    def decompress(self):
        """
        Decompress the image back to its original form using the difference transform.

        This method should restore the image data by reversing the difference 
        encoding process applied during compression.

        Returns:
            Decompressed data (original image format).
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the compression method.

        Returns:
            str: "Difference Transform Compression Method"
        """
        pass

    def get_compression_ratio(self):
        """
        Calculate and return the compression ratio.

        The compression ratio is the ratio of the original image size to the
        compressed size, demonstrating the efficiency of the difference transform.

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
