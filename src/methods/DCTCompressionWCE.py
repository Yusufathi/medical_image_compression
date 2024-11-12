# 3D Discrete Cosine Transform (DCT) Compression for Wireless Capsule Endoscopy
# Based on: "3D DCT for Wireless Capsule Endoscopy - Xue et al., 2021"

from method import CompressionMethodInterface
import time


class DCTCompressionWCE(CompressionMethodInterface):
    def compress(self):
        """
        Compress the image using 3D Discrete Cosine Transform (DCT).

        This function should apply 3D DCT to compress images obtained from
        wireless capsule endoscopy (WCE) by transforming spatial data into
        frequency components, achieving efficient compression.

        Returns:
            Compressed data (implementation-specific format).
        """
        pass

    def decompress(self):
        """
        Decompress the image back to its original form using 3D DCT.

        This method should reverse the 3D DCT applied during compression,
        restoring the original spatial data from the frequency domain.

        Returns:
            Decompressed data (original image format).
        """
        pass

    def __str__(self):
        """
        Returns a string representation of the compression method.

        Returns:
            str: "3D DCT Compression for Wireless Capsule Endoscopy"
        """
        pass

    def get_compression_ratio(self):
        """
        Calculate and return the compression ratio.

        The compression ratio is calculated as the ratio of the original
        image size to the compressed size, indicating compression efficiency.

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
