from __future__ import annotations

from collections.abc import Iterable

from chia_rs.sized_bytes import bytes32


class IntegrityError(Exception):
    pass


def build_message_with_hashes(message: str, bytes_objects: Iterable[bytes]) -> str:
    return "\n".join([message, *[f"    {b.hex()}" for b in bytes_objects]])


class TreeGenerationIncrementingError(IntegrityError):
    def __init__(self, store_ids: list[bytes32]) -> None:
        super().__init__(
            build_message_with_hashes(
                message="Found trees with generations not properly incrementing:",
                bytes_objects=store_ids,
            )
        )


class NodeHashError(IntegrityError):
    def __init__(self, node_hashes: list[bytes32]) -> None:
        super().__init__(
            build_message_with_hashes(
                message="Found nodes with incorrect hashes:",
                bytes_objects=node_hashes,
            )
        )


class KeyNotFoundError(Exception):
    def __init__(self, key: bytes) -> None:
        super().__init__(f"Key not found: {key.hex()}")


class OfferIntegrityError(Exception):
    pass


class ProofIntegrityError(Exception):
    pass


class LauncherCoinNotFoundError(Exception):
    pass
