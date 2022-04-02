% This generates a difference table for
% $f(t)=\cos(t)+\sin(t)+10^{-3}U_{[0,2\sqrt{3}]}$
%     Argonne National Laboratory
%     Jorge More' and Stefan Wild. November 2009.

% This prime state gives Table 3.1 (Matlab 2010a, 64bit) in
%   Estimating Computational Noise.
%   SIAM J. Scientific Computing, 33(3):1292-1314, 2011.
rand('state', 197);

nf = 7;
h = 1e-2;

% Multiply rand by sigma to get std of 1e-3
sigma = (1e-3) * 2 * sqrt(3);
fval = zeros(nf, 1);
U = rand(nf, 1);
x = (0:nf - 1) * h;
for i = 1:nf
    fval(i, 1) = cos(x(i)) + sin(x(i)) + sigma * U(i);
end

% Construct the difference table.
level = zeros(nf - 1, 1);
gamma = 1.0; % gamma(0)
T = fval;
for j = 1:nf - 1
    for i = 1:nf - j
        fval(i) = fval(i + 1) - fval(i);
        T(i, j + 1) = fval(i);
    end
    gamma = 0.5 * (j / (2 * j - 1)) * gamma;

    % Compute the estimates for the noise level.
    level(j) = sqrt(gamma * mean(fval(1:nf - j).^2));
end

% Print the table:
disp('\begin{table}[htb!]');
disp(strcat('\caption{\label{tab:diff} Difference table for $f(t)=\cos(t)+\sin(t)+10^{-3}U_{[0,2\sqrt{3}]}$  $\left(m=6, h=10^{-2}\right)$}'));
disp('\begin{center} \footnotesize');
disp('\begin{tabular}{|c|rrrrrrr|} \hline');
disp('i & k & 1 & 2 & 3 & 4 & 5 & 6 \\ \hline');
for i = 1:nf - 1
    str = strcat(num2str(i - 1), sprintf(' & %4.3f', T(i, 1)), sprintf(' & %3.2e ', T(i, 2:nf - i + 1)));
    str = strrep(str, 'e+0', 'e+');
    str = strrep(str, 'e-0', 'e-');
    for j = 1:i - 1
        str = strcat(str, ' & ');
    end
    str = strcat(str, ' \\');
    disp(str);
end
str = strcat(num2str(nf - 1), sprintf(' & %4.3f', T(nf, 1)));
for j = 1:nf - 1
    str = strcat(str, ' & ');
end
str = strcat(str, ' \\ \hline');
disp(str);

str2 = '$\sigma_k$ & ';
str2 = strcat(str2, sprintf('& %3.2e ', level));
str2 = strrep(str2, 'e-0', 'e-'); % Get rid of extra 0
disp(strcat(str2, '\\ \hline'));
disp('\end{tabular}');
disp('\end{center}');
disp('\end{table}');
disp(' ');
