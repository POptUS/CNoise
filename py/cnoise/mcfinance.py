"""Monte Carlo example from the MATLAB code."""

from __future__ import annotations

import numpy as np

from ._random import as_rng


def mcfinance(x, *, draws: int = 5000, rng: int | np.random.Generator | None = None) -> float:
    """Evaluate the example finance functional with lognormal rates."""

    x = np.asarray(x, dtype=float).reshape(-1)
    if x.size == 0:
        raise ValueError("x must not be empty")
    if draws <= 0:
        raise ValueError("draws must be positive")

    generator = as_rng(rng)
    u = generator.standard_normal((x.size, draws))
    r = np.full(draws, 0.1, dtype=float)
    pro = 1.0 + r
    x2 = 0.5 * x**2

    for i, xi in enumerate(x):
        r = r * np.exp(xi * u[i] - x2[i])
        pro = pro * (1.0 + r)

    return float(np.mean(1.0 / pro))
