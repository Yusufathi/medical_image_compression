# Lossless Compression using POB System
# Based on: "Lossless Compression (POB System) - Li et al., 2022"

from method import CompressionMethodInterface
import time


class POBSystemCompression(CompressionMethodInterface):
    def compress(self):
        """
        Compress the image using the POB (Probability of Blocks) system.

        The POB system is a lossless compression technique that encodes the
        image in a secure format for complete lossless recovery. This function
        should implement the block-based probability encoding.

        Returns:
            Compressed data (implementation-specific format).
        """
        pass

    def decompress(self):
        """
        Decompress the image back to its original form using the POB system.

        This method should decode the block-based probability encoding applied
        during compression, restoring the original data with complete accuracy.

        Returns:
            Decompressed data (original image format).
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the compression method.

        Returns:
            str: "POB System Compression Method"
        """
        pass

    def get_compression_ratio(self):
        """
        Calculate and return the compression ratio.

        The compression ratio is the ratio of the original image size to the
        compressed size, demonstrating the efficiency of the POB system.

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
