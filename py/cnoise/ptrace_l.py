"""Partial trace example using a C-shaped Laplacian."""

from __future__ import annotations

import numpy as np
from scipy.sparse import coo_matrix, csr_matrix, diags
from scipy.sparse.linalg import ArpackNoConvergence, eigsh

from ._random import as_rng


def build_c_shape_mask(n_grid: int = 50, arm_width: int | None = None) -> np.ndarray:
    """Create a simple C-shaped boolean mask on an n_grid by n_grid mesh."""

    if n_grid < 3:
        raise ValueError("n_grid must be at least 3")
    if arm_width is None:
        arm_width = max(1, int(round(n_grid * 0.3)))
    arm_width = max(1, min(arm_width, n_grid - 1))

    mask = np.zeros((n_grid, n_grid), dtype=bool)
    mask[:, :arm_width] = True
    mask[:arm_width, :] = True
    mask[-arm_width:, :] = True
    return mask


def build_c_shape_laplacian(
    n_grid: int = 50,
    *,
    arm_width: int | None = None,
) -> tuple[csr_matrix, np.ndarray]:
    """Build the discrete Laplacian for the C-shaped region."""

    mask = build_c_shape_mask(n_grid=n_grid, arm_width=arm_width)
    index = np.full(mask.shape, -1, dtype=int)
    index[mask] = np.arange(mask.sum(), dtype=int)

    rows: list[int] = []
    cols: list[int] = []
    data: list[float] = []

    for i, j in zip(*np.nonzero(mask)):
        node = index[i, j]
        degree = 0
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni = i + di
            nj = j + dj
            if 0 <= ni < n_grid and 0 <= nj < n_grid and mask[ni, nj]:
                rows.append(node)
                cols.append(index[ni, nj])
                data.append(-1.0)
                degree += 1
        rows.append(node)
        cols.append(node)
        data.append(float(degree))

    laplacian = coo_matrix((data, (rows, cols)), shape=(mask.sum(), mask.sum())).tocsr()
    return laplacian, mask


def ptrace_l(
    x,
    *,
    n_grid: int = 50,
    n_eigs: int = 5,
    tol: float = 1e-9,
    rng: int | np.random.Generator | None = None,
    arm_width: int | None = None,
) -> float:
    """Evaluate the partial trace example for a diagonal perturbation."""

    laplacian, _ = build_c_shape_laplacian(n_grid=n_grid, arm_width=arm_width)
    x = np.asarray(x, dtype=float).reshape(-1)
    n = laplacian.shape[0]
    if x.size != n:
        raise ValueError(f"x must have length {n}, not {x.size}")
    if not 1 <= n_eigs < n:
        raise ValueError("n_eigs must satisfy 1 <= n_eigs < number of grid points")

    matrix = laplacian + diags(x, offsets=0, format="csr")
    generator = as_rng(rng)
    v0 = generator.standard_normal(n)

    try:
        eigvals = eigsh(
            matrix,
            k=n_eigs,
            which="LM",
            tol=tol,
            return_eigenvectors=False,
            v0=v0,
        )
    except ArpackNoConvergence:
        return 0.0

    return float(np.sum(eigvals))
