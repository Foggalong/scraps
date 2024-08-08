% demonstration of basic plotting in MATLAB, used as a
% reference whenever I forgot the basic workflow.

fdata = load('float_data.csv');
ddata = load('double_data.csv');

figure;

% plot graphs for float data
subplot(1,2,1)
plot(fdata(1:21, 1), fdata(1:21, 3)); hold on
plot(fdata(1:21, 1), fdata(1:21, 2)); hold off

% decorations for float graphs
ylim ([-0.25, 1.25]);
title('Calculating terms using float variables')
legend('Numerical Solution',
       'Analytical Solution',
       'location', 'southwest')
xlabel('n'), ylabel('p_n')

% plot graphs for double data
subplot(1,2,2)
plot(ddata(1:21, 1), ddata(1:21, 3)); hold on
plot(ddata(1:21, 1), ddata(1:21, 2)); hold off

% decorations for double graphs
ylim ([-0.25, 1.25]);
title('Calculating terms using double variables')
legend('Numerical Solution',
       'Analytical Solution',
       'location', 'southwest')
xlabel('n'), ylabel('p_n')

saveas (1, 'figure1.png');
