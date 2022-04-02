function y = mcfinance(x)
    %
    %  Evaluating today's value of a dollar n years from now with lognormal
    %  interest rates with variance x. For details see page 20 of:
    %     R. E. Caflisch, Monte Carlo and Quasi-Monte Carlo methods,
    %     Acta Numerica, 7(1998), pp. 1--49.
    %
    %  n = 3
    %
    %     Argonne National Laboratory
    %     Jorge More' and Stefan Wild. November 2009.

    tol = 5000; % Number of MC draws

    n = 3; % dimension
    x = x(:); % Make sure we have a column vector

    % Vectorized for speed:
    x2 = .5 * x.^2;
    u = randn(n, tol);
    r = .1 * ones(1, tol);
    pro = 1 + r;
    for i = 1:n
        r = r .* exp(x(i, :) .* u(i, :) - x2(i));
        pro = pro .* (1 + r);
    end
    y = mean(1 ./ pro);
