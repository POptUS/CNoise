function ECNdriver
    %
    %  Sample driver for quantifying computational noise with ECNoise
    %
    %     Argonne National Laboratory
    %     Jorge More' and Stefan Wild. November 2009.

    % Define the function
    func = @norm;

    % Define the number of variables
    n = 10;

    % Define the base point
    rand('state', 0);
    xb = rand(n, 1);

    % Define the (unit) sampling vector
    rand('state', 113);
    p = rand(n, 1);
    % This procedure is inefficient for large n.
    while norm(p) > 1
        p = rand(n, 1);
    end
    p = p / norm(p);

    % Define the number of additional evaluations
    m = 8;

    % Define the sampling distance
    h = 1e-14;

    % Evaluate the function at m+1 equally spaced points
    fval = zeros(m + 1, 1);
    mid = floor((m + 2) / 2);
    for i = 1:m + 1
        s = 2 * (i - mid) / m;
        x = xb + s * h * p;
        fval(i) = feval(func, x);
    end

    % Call the noise estimator
    [fnoise, level, inform] = ECNoise(m + 1, fval);

    rel_noise = fnoise / fval(mid);
    return
