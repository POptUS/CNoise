"""Random-number helper utilities."""

from __future__ import annotations

from numpy.random import Generator, default_rng


def as_rng(rng: Generator | int | None = None) -> Generator:
    """Normalize an RNG argument to a NumPy Generator."""

    if isinstance(rng, Generator):
        return rng
    return default_rng(rng)
