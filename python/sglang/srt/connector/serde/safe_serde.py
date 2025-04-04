# SPDX-License-Identifier: Apache-2.0

from typing import Union

import torch
from safetensors.torch import load, save

from sglang.srt.connector.serde.serde import Deserializer, Serializer


class SafeSerializer(Serializer):

    def __init__(self):
        super().__init__()

    def to_bytes(self, t: torch.Tensor) -> bytes:
        return save({"tensor_bytes": t.cpu().contiguous()})


class SafeDeserializer(Deserializer):

    def __init__(self, dtype):
        super().__init__(dtype)

    def from_bytes_normal(self, b: Union[bytearray, bytes]) -> torch.Tensor:
        return load(bytes(b))["tensor_bytes"].to(dtype=self.dtype)

    def from_bytes(self, b: Union[bytearray, bytes]) -> torch.Tensor:
        return self.from_bytes_normal(b)
