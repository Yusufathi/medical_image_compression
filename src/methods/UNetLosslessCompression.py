# Lossless Compression using U-Net
# Based on: "LFC-UNet: Learned Lossless Medical Image Fast Compression with U-Net - Liao and Li, 2024"

from method import CompressionMethodInterface
import time


class UNetLosslessCompression(CompressionMethodInterface):
    def compress(self):
        """
        Compress the image using a U-Net-based lossless compression model.

        This function should apply a deep learning model based on U-Net to
        perform lossless compression by learning spatial features effectively.

        Returns:
            Compressed data (implementation-specific format).
        """
        pass

    def decompress(self):
        """
        Decompress the image back to its original form using U-Net.

        This method should restore the image by reversing the learned encoding
        applied during compression, ensuring lossless recovery of data.

        Returns:
            Decompressed data (original image format).
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the compression method.

        Returns:
            str: "U-Net Lossless Compression Method"
        """
        pass

    def get_compression_ratio(self):
        """
        Calculate and return the compression ratio.

        The compression ratio is the ratio of the original image size to the
        compressed size, indicating the effectiveness of the U-Net compression.

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
