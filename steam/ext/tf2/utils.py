# -*- coding: utf-8 -*-

import struct
from io import BytesIO


class BytesBuffer(BytesIO):
    def read_struct(self, format: str, position: int = None) -> tuple:
        buffer = self.read(position or struct.calcsize(format))
        return struct.unpack(format, buffer)

    def write_struct(self, format: str, to_write: int):
        self.write(struct.pack(format, to_write))

    def read_int16(self, position: int = 2) -> int:
        return self.read_struct("<h", position)[0]

    def write_int16(self, int16: int) -> None:
        self.write_struct("<h", int16)

    def read_uint32(self, position: int = 4) -> int:
        return self.read_struct("<I", position)[0]

    def write_uint32(self, uint32: int) -> None:
        self.write_struct("<I", uint32)

    def read_uint64(self, position: int = 8) -> int:
        return self.read_struct("<Q", position)[0]

    def write_uint64(self, uint64) -> None:
        self.write_struct("<Q", uint64)
