from __future__ import annotations

import numpy as np
import pytest

from cnoise import ecnoise


def test_ecnoise_reports_h_too_large_when_values_vary_too_much() -> None:
    fval = np.linspace(1.0, 2.0, 7)
    original = fval.copy()

    fnoise, level, inform = ecnoise(len(fval), fval)

    assert inform == 3
    assert fnoise == 0.0
    assert level.shape == (6,)
    assert np.array_equal(fval, original)


def test_ecnoise_reports_h_too_small_for_constant_values() -> None:
    fval = np.full(7, 3.0)

    fnoise, level, inform = ecnoise(len(fval), fval)

    assert inform == 2
    assert fnoise == 0.0
    assert np.all(level == 0.0)


def test_ecnoise_detects_noise_for_alternating_values() -> None:
    fval = np.array([1.0, 1.01, 1.0, 1.01, 1.0, 1.01, 1.0])

    fnoise, level, inform = ecnoise(len(fval), fval)

    assert inform == 1
    assert fnoise == pytest.approx(level[0])
    assert fnoise > 0.0
