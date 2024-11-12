# Low-Complexity 3D Discrete Hartley Transform (DHT) Compression
# Based on: "Low-Complexity 3D DHT - Coutinho et al., 2021"

from method import CompressionMethodInterface
import time


class LowComplexity3DDHT(CompressionMethodInterface):
    def compress(self):
        """
        Compress the image using a low-complexity 3D Discrete Hartley Transform (DHT).

        The function should implement 3D DHT for volumetric data compression,
        focusing on reducing computational complexity while achieving effective
        compression. DHT-based compression is particularly suited for 3D data.

        Returns:
            Compressed data (implementation-specific format).
        """
        pass

    def decompress(self):
        """
        Decompress the image back to its original form using 3D DHT.

        This method should reverse the 3D DHT transformation applied during
        compression, restoring the original 3D volumetric data.

        Returns:
            Decompressed data (original 3D image format).
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the compression method.

        Returns:
            str: "Low-Complexity 3D DHT Compression Method"
        """
        pass

    def get_compression_ratio(self):
        """
        Calculate and return the compression ratio.

        The compression ratio is the ratio of the original 3D data size to the
        compressed size, demonstrating the efficiency of 3D DHT.

        Returns:
            float: Compression ratio.
        """
        pass

    def get_compression_time(self):
        """
        Return the time taken to compress the 3D image.

        This time should be measured within the compress() method.

        Returns:
            float: Compression time in seconds.
        """
        pass

    def get_decompression_time(self):
        """
        Return the time taken to decompress the 3D image.

        This time should be measured within the decompress() method.

        Returns:
            float: Decompression time in seconds.
        """
        pass
