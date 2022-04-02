function y = ptrace_L(x)
    %
    %  Evaluating a partial trace for diagonal perturbations of the
    %  Laplacian of a C shaped region (should be noise-free).
    %
    % n = 1857
    %
    %     Argonne National Laboratory
    %     Jorge More' and Stefan Wild. November 2009.

    % Need to reset the random number generator because eigs is stochastic
    rstate = rand('state'); % Current state of rand
    rand('state', 113); % Fixed state of rand

    % Tolerance for eigs
    tol = 1e-9;

    n_eigs = 5;
    n_grid = 50;
    A = delsq(numgrid('C', n_grid));   % Laplacian on the region
    n = size(A, 1);
    opt_eigs = struct('tol', tol, 'disp', 0);

    B = A + spdiags(x, 0, n, n);
    [v, d, flag] = eigs(B, n_eigs, 'LM', opt_eigs); % Take largest eigenvalues

    if flag
        y = 0.0;
    else
        y = sum(diag(d));
    end

    rand('state', rstate); % Reset the state of rand
