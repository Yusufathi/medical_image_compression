from abc import ABC, abstractmethod


class CompressionMethodInterface(ABC):

    @abstractmethod
    def compress(self):
        pass

    @abstractmethod
    def decompress(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_compression_ratio(self):
        pass

    @abstractmethod
    def get_compression_time(self):
        pass

    @abstractmethod
    def get_decompression_time(self):
        pass
