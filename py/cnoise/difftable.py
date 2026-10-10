"""Construct the example difference table from the MATLAB script."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from ._random import as_rng


@dataclass(frozen=True, slots=True)
class DifferenceTableResult:
    """Results from the example difference-table construction."""

    x: np.ndarray
    fval: np.ndarray
    table: np.ndarray
    level: np.ndarray
    latex: str


def difftable(
    *,
    nf: int = 7,
    h: float = 1e-2,
    sigma: float = 1e-3,
    rng: int | np.random.Generator | None = 197,
) -> DifferenceTableResult:
    """Build the example difference table and LaTeX rendering."""

    if nf < 2:
        raise ValueError("nf must be at least 2")

    generator = as_rng(rng)
    x = np.arange(nf, dtype=float) * h
    u = generator.random(nf)
    noise_scale = sigma * 2.0 * np.sqrt(3.0)
    fval = np.cos(x) + np.sin(x) + noise_scale * u

    table = np.zeros((nf, nf), dtype=float)
    table[:, 0] = fval

    level = np.zeros(nf - 1, dtype=float)
    diffs = fval.copy()
    gamma = 1.0
    for j in range(1, nf):
        count = nf - j
        diffs[:count] = diffs[1 : count + 1] - diffs[:count]
        table[:count, j] = diffs[:count]
        gamma = 0.5 * (j / (2 * j - 1)) * gamma
        level[j - 1] = np.sqrt(gamma * np.mean(diffs[:count] ** 2))

    latex = format_latex_table(table, level, h=h, sigma=sigma)
    return DifferenceTableResult(x=x, fval=fval, table=table, level=level, latex=latex)


def format_latex_table(
    table: np.ndarray,
    level: np.ndarray,
    *,
    h: float,
    sigma: float,
) -> str:
    """Render the difference table in a LaTeX-friendly form."""

    nf = table.shape[0]
    n_diffs = nf - 1
    lines = [
        r"\begin{table}[htb!]",
        rf"\caption{{\label{{tab:diff}} Difference table for $f(t)=\cos(t)+"
        rf"\sin(t)+{sigma:.0e}U_{{[0,2\sqrt{{3}}]}}$  $(m={nf - 1}, h={h:.0e})$}}",
        r"\begin{center} \footnotesize",
        r"\begin{tabular}{|c|c|" + "c|" * n_diffs + r"} \hline",
        "i & k & " + " & ".join(str(i) for i in range(1, n_diffs + 1)) + r" \\ \hline",
    ]

    for i in range(nf - 1):
        row = [str(i), f"{table[i, 0]:4.3f}"]
        row.extend(f"{table[i, j]:3.2e}" for j in range(1, nf - i))
        row.extend("" for _ in range(n_diffs - (nf - i - 1)))
        lines.append(" & ".join(row) + r" \\")

    row = [str(nf - 1), f"{table[nf - 1, 0]:4.3f}"]
    row.extend("" for _ in range(n_diffs))
    lines.append(" & ".join(row) + r" \\ \hline")

    lines.extend(
        [
            r"$\sigma_k$ & " + " & ".join(f"{value:3.2e}" for value in level) + r" \\ \hline",
            r"\end{tabular}",
            r"\end{center}",
            r"\end{table}",
            " ",
        ]
    )
    return "\n".join(lines)
