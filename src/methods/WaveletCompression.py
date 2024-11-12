# Wavelet-based Compression Method
# Based on: "Empirical Selection of Wavelets for Near-Lossless Compression (2024)"

from method import CompressionMethodInterface
import time


class WaveletCompression(CompressionMethodInterface):
    def compress(self):
        """
        Compress the image using a wavelet-based approach.

        The function should implement a wavelet transformation (e.g., DWT) 
        to reduce the image size while preserving critical details.

        Returns:
            Compressed data (implementation-specific format).
        """
        pass

    def decompress(self):
        """
        Decompress the image back to its original form.

        This method should reverse the wavelet transformation applied during
        compression, restoring the original data with no loss.

        Returns:
            Decompressed data (original image format).
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the compression method.

        This can be used to identify the method in output or logs.

        Returns:
            str: "Wavelet-based Compression Method"
        """
        pass

    def get_compression_ratio(self):
        """
        Calculate and return the compression ratio.

        The compression ratio should be calculated by comparing the original
        image size with the compressed size.

        Returns:
            float: Compression ratio.
        """
        pass

    def get_compression_time(self):
        """
        Return the time taken to compress the image.

        The time should be measured in seconds and can be calculated by 
        recording the start and end time of the compress() function.

        Returns:
            float: Compression time in seconds.
        """
        pass

    def get_decompression_time(self):
        """
        Return the time taken to decompress the image.

        The time should be measured in seconds, similar to the compression
        time, but measured in the decompress() function.

        Returns:
            float: Decompression time in seconds.
        """
        pass
