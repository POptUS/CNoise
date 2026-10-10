from __future__ import annotations

import numpy as np
import pytest

from cnoise import build_c_shape_laplacian, ptrace_l


def test_ptrace_l_is_reproducible_with_a_seed() -> None:
    laplacian, _ = build_c_shape_laplacian(n_grid=10)
    x = np.zeros(laplacian.shape[0], dtype=float)

    y1 = ptrace_l(x, n_grid=10, n_eigs=3, rng=123)
    y2 = ptrace_l(x, n_grid=10, n_eigs=3, rng=123)

    assert y1 == pytest.approx(y2)
    assert np.isfinite(y1)
    assert y1 >= 0.0
