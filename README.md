# CNoise: Estimating Computational Noise in Numerical Simulations

This repository contains source code and updates from the codes originally shared at https://www.mcs.anl.gov/~wild/cnoise/.

These codes are based on the supplemental information for the papers:
- [[1](#pap1)] Estimating Computational Noise by J.J. Moré and S.M. Wild. *SIAM J. Scientific Computing*, 33(3):1292-1314, 2011. doi:[10.1137/100786125](https://doi.org/10.1137/100786125); [PDF from earlier preprint](http://www.optimization-online.org/DB_HTML/2010/03/2557.html)
- [[2](#pap2)] Estimating Derivatives of Noisy Simulations by J.J. Moré and S.M. Wild. *ACM Transactions on Mathematical Software*, 38(3):19:1-19:21, 2012. doi:[10.1145/2168773.2168777](https://doi.org/10.1145/2168773.2168777); [PDF from earlier preprint](http://www.mcs.anl.gov/papers/P1785.pdf)
- [[3](#pap3)] Do You Trust Derivatives or Differences? by J.J. Moré and S.M. Wild. *J. Computational Physics*, 273:268-277, 2014. doi:[10.1016/j.jcp.2014.04.056](https://doi.org/10.1016/j.jcp.2014.04.056); [PDF from earlier preprint](http://www.mcs.anl.gov/papers/P2067-0312.pdf); [Supplement](docs/doyoutrust_supplement.md)


### Main Files
The following information, used in [1], is provided to encourage the
estimation of computational noise in applications and to show the strengths
and limitations of the code. The original CNoise site groups the main scripts
into routines for estimating computational noise, sample problems, and a data
example. The repository follows that structure below.

#### Estimating Computational Noise
- `ECNdriver` - sample driver that picks a base point and sampling direction,
  evaluates a function on equally spaced points, and calls `ECNoise` to
  estimate the relative noise. [Matlab/Octave](m/ECNdriver.m) |
  [Python](py/cnoise/ecn_driver.py)
- `ECNoise` - estimates the noise level of a function from equally spaced
  samples by building a finite-difference table and checking when noise is
  detected. [Matlab/Octave](m/ECNoise.m) | [Python](py/cnoise/ecnoise.py)

#### Sample Problems
- `mcfinance` - Monte Carlo evaluation of a small finance model with
  lognormal interest-rate perturbations. [Matlab/Octave](m/mcfinance.m) |
  [Python](py/cnoise/mcfinance.py)
- `ptrace_L` - partial-trace example for a diagonal perturbation of a
  C-shaped Laplacian. [Matlab/Octave](m/ptrace_L.m) |
  [Python](py/cnoise/ptrace_l.py)

#### Example
- `difftable` - generates the example difference table for
  `cos(t) + sin(t) + noise` and produces the LaTeX table used in [1].
  [Matlab/Octave](m/difftable.m) | [Python](py/cnoise/difftable.py)

### Matlab/Octave
The Matlab/Octave code lives in `m/`.

### Python
The Python code lives in `py/`, and the Python tests live in `tests/`.

## Contributing to CNoise

Contributions are welcome in a variety of forms; please see [CONTRIBUTING](CONTRIBUTING.rst).

## License

All code included in CNoise is open source, with the particular form of license contained in the top-level
subdirectories. If such a subdirectory does not contain a LICENSE file, then it is automatically licensed
as described in the otherwise encompassing CNoise [LICENSE](/LICENSE).
