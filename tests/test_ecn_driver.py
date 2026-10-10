from __future__ import annotations

import numpy as np
import pytest

from cnoise import ecnoise, ecn_driver


def test_ecn_driver_is_deterministic_with_a_seed() -> None:
    result1 = ecn_driver(rng=123)
    result2 = ecn_driver(rng=123)

    assert np.allclose(result1.xb, result2.xb)
    assert np.allclose(result1.p, result2.p)
    assert np.allclose(result1.fval, result2.fval)
    assert result1.inform == result2.inform
    assert result1.fnoise == pytest.approx(result2.fnoise)


def test_ecn_driver_reuses_ecnoise_output() -> None:
    result = ecn_driver(rng=123)
    fnoise, level, inform = ecnoise(len(result.fval), result.fval)

    assert result.fnoise == pytest.approx(fnoise)
    assert np.allclose(result.level, level)
    assert result.inform == inform
    assert result.rel_noise == pytest.approx(result.fnoise / result.fval[len(result.fval) // 2])
