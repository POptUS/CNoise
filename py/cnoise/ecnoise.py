"""Estimate function noise from equally spaced samples."""

from __future__ import annotations

import numpy as np


def ecnoise(nf: int, fval) -> tuple[float, np.ndarray, int]:
    """Estimate noise level from a finite-difference table."""

    fval = np.asarray(fval, dtype=float).reshape(-1).copy()
    if nf != fval.size:
        raise ValueError(f"nf ({nf}) must match len(fval) ({fval.size})")
    if nf < 4:
        raise ValueError("nf must be at least 4")

    level = np.zeros(nf - 1, dtype=float)
    dsgn = np.zeros(nf - 1, dtype=bool)
    fnoise = 0.0
    gamma = 1.0

    fmin = float(np.min(fval))
    fmax = float(np.max(fval))
    scale = max(abs(fmax), abs(fmin))
    if scale != 0.0 and (fmax - fmin) / scale > 0.1:
        return fnoise, level, 3

    diffs = fval.copy()
    for j in range(1, nf):
        count = nf - j
        diffs[:count] = diffs[1 : count + 1] - diffs[:count]

        if j == 1 and np.count_nonzero(diffs[:count] == 0.0) >= nf / 2:
            return fnoise, level, 2

        gamma = 0.5 * (j / (2 * j - 1)) * gamma
        active = diffs[:count]
        level[j - 1] = np.sqrt(gamma * np.mean(active**2))

        if np.min(active) * np.max(active) < 0.0:
            dsgn[j - 1] = True

    for k in range(nf - 3):
        window = level[k : k + 3]
        if np.max(window) <= 4.0 * np.min(window) and dsgn[k]:
            return float(level[k]), level, 1

    return fnoise, level, 3
