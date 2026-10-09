from __future__ import annotations

import numpy as np
import pytest

from cnoise import mcfinance


def test_mcfinance_is_reproducible_with_a_seed() -> None:
    x = np.array([0.1, 0.2, 0.3])

    y1 = mcfinance(x, draws=1000, rng=123)
    y2 = mcfinance(x, draws=1000, rng=123)

    assert y1 == pytest.approx(y2)
    assert 0.0 < y1 < 1.0
