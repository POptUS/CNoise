"""Sample driver for the ECNoise estimator."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import numpy as np

from ._random import as_rng
from .ecnoise import ecnoise


@dataclass(frozen=True, slots=True)
class ECNDriverResult:
    """Results from the sample ECNoise driver."""

    xb: np.ndarray
    p: np.ndarray
    fval: np.ndarray
    fnoise: float
    level: np.ndarray
    inform: int
    rel_noise: float


def ecn_driver(
    *,
    n: int = 10,
    m: int = 8,
    h: float = 1e-14,
    func: Callable[[np.ndarray], float] = np.linalg.norm,
    rng: int | np.random.Generator | None = None,
) -> ECNDriverResult:
    """Run the ECNoise sample driver and return its computed values."""

    if n <= 0:
        raise ValueError("n must be positive")
    if m < 2:
        raise ValueError("m must be at least 2")

    generator = as_rng(rng)
    xb = generator.random(n)

    p = generator.random(n)
    while np.linalg.norm(p) > 1.0:
        p = generator.random(n)
    p = p / np.linalg.norm(p)

    mid = m // 2 + 1
    fval = np.empty(m + 1, dtype=float)
    for i in range(m + 1):
        s = 2.0 * (i + 1 - mid) / m
        x = xb + s * h * p
        fval[i] = float(func(x))

    fnoise, level, inform = ecnoise(m + 1, fval)
    rel_noise = float(fnoise / fval[mid - 1])
    return ECNDriverResult(xb=xb, p=p, fval=fval, fnoise=fnoise, level=level, inform=inform, rel_noise=rel_noise)
