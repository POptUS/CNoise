# CNoise: Estimating Computational Noise in Numerical Simulations 

This repository contains source code and updates from the codes originally shared at https://www.mcs.anl.gov/~wild/cnoise/.

These codes are based on the supplemental information for the papers:
- [[1](#pap1)] Estimating Computational Noise by J.J. Moré and S.M. Wild. *SIAM J. Scientific Computing*, 33(3):1292-1314, 2011. doi:[10.1137/100786125](https://doi.org/10.1137/100786125); [PDF from earlier preprint](http://www.optimization-online.org/DB_HTML/2010/03/2557.html)
- [[2](#pap2)] Estimating Derivatives of Noisy Simulations by J.J. Moré and S.M. Wild. *ACM Transactions on Mathematical Software*, 38(3):19:1-19:21, 2012. doi:[10.1145/2168773.2168777](https://doi.org/10.1145/2168773.2168777); [PDF from earlier preprint](http://www.mcs.anl.gov/papers/P1785.pdf)
- [[3](#pap3)] Do You Trust Derivatives or Differences? by J.J. Moré and S.M. Wild. *J. Computational Physics*, 273:268-277, 2014. doi:[10.1016/j.jcp.2014.04.056](https://doi.org/10.1016/j.jcp.2014.04.056); [PDF from earlier preprint](http://www.mcs.anl.gov/papers/P2067-0312.pdf)
    

### Estimating Computational Noise
The following information (used in [1]) is provided to encourage the estimation of computational noise in applications and to determine strengths and limitations of the code. The included scripts produce basic noise level estimates from data. 

### Matlab/Octave
The Matlab/Octave version lives under `m/`.

### Python
The Python version lives under `py/`, and the Python tests live at the
repository root in `tests/`. Install it with `python -m pip install --upgrade
pip setuptools wheel` followed by `python -m pip install --no-build-isolation
-e py pytest`, then run the Python suite with `pytest tests`.

### Sample Problems


### Examples
- `difftable` [Matlab/Octave](m/difftable.m)  [Python](py/cnoise/difftable.py): Code for generating the example difference table in Table 3.1 of [1].

## Contributing to CNoise

Contributions are welcome in a variety of forms; please see [CONTRIBUTING](CONTRIBUTING.rst).

## License 

All code included in Cnoise is open source, with the particular form of license contained in the top-level 
subdirectories.  If such a subdirectory does not contain a LICENSE file, then it is automatically licensed 
as described in the otherwise encompassing Cnoise [LICENSE](/LICENSE).  

## Resources

To seek support or report issues, e-mail:

 * ``poptus@mcs.anl.gov``
