"""Represent bytes as LZMA-compressed, base64-encoded strings."""

from __future__ import annotations
from base64 import b64decode, b64encode
from lzma import compress, decompress


__all__ = ["B64LZMA"]


class B64LZMA(str):
    """A string of base64 encoded, LZMA compressed data."""

    def __bytes__(self) -> bytes:
        """Returns the decompressed data."""
        return decompress(b64decode(self.encode()))

    def __str__(self) -> str:
        """Returns the string decoded from __bytes__."""
        return bytes(self).decode()

    @classmethod
    def from_b64bytes(cls, b64bytes: bytes) -> B64LZMA:
        """Creates an instance from base64 encoded, compressed bytes."""
        return cls(b64bytes.decode())

    @classmethod
    def from_compressed_bytes(cls, compressed_bytes: bytes) -> B64LZMA:
        """Creates an instance from the respective compressed bytes."""
        return cls.from_b64bytes(b64encode(compressed_bytes))

    @classmethod
    def from_bytes(cls, bytes_: bytes) -> B64LZMA:
        """Creates an instance from the respective bytes."""
        return cls.from_compressed_bytes(compress(bytes_))

    @classmethod
    def from_string(cls, string: str, *, encoding: str = "utf-8") -> B64LZMA:
        """Creates an instance from the respective string."""
        return cls.from_bytes(string.encode(encoding=encoding))
