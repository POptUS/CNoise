from __future__ import annotations

import numpy as np

from cnoise import difftable


def test_difftable_builds_a_deterministic_table() -> None:
    result1 = difftable(rng=197)
    result2 = difftable(rng=197)

    assert result1.table.shape == (7, 7)
    assert result1.level.shape == (6,)
    assert np.allclose(result1.table, result2.table)
    assert np.allclose(result1.level, result2.level)
    assert result1.latex == result2.latex
    assert r"\begin{table}" in result1.latex
    assert r"\sigma_k" in result1.latex
