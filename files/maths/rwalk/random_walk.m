% Script for creating an arbitrarily dimensioned walk. It has the option
% to create historgrams of each location coordinate and if the dimension
% is 1, 2, or 3 it has the option of plotting the walk. 'tiledlayout' is
% used and so it requires MATLAB R2019b or later to work.

dim      = 3;                   % dimension of the walk
new_step = zeros(1, dim);       % walks starts at zero
length   = 1e3;                 % length of the walk
steps    = zeros(length, dim);  % prealocated matrix to store walk

map = true;     % option to map the walk
freq = true;    % option to plot histograms of location

% generate a random walk in 'dim' dimensions
for i = 2:length
    coord_change   = randi(dim);
    step_direction = randsample([-1,1], 1);
    new_step(coord_change) = new_step(coord_change) + step_direction;
    steps(i,:) = new_step;
end

% handles the setting up of the plot tiles
if (dim < 4 && map && freq)
    tiledlayout(2,dim)
    nexttile([1,dim])
elseif (dim < 4 && map)
    tiledlayout(1,1)
    nexttile
elseif (freq)
    tiledlayout(1,dim)
    nexttile
end
 
% mapping the walk for 1, 2, or 3 dimensions
if (map && dim < 4)
    if (dim == 1)
        plot(steps(:,1)); hold on;
        plot(0, 's', 'MarkerFaceColor', 'red'); hold off;
    elseif (dim == 2)
        plot(steps(:,1), steps(:,2), '*-'); hold on;
        plot(0, 0, 's', 'MarkerFaceColor', 'red');
        axis equal; hold off;
    elseif (dim == 3)
        plot3(steps(:,1), steps(:,2), steps(:,3), '*-'); hold on;
        plot3(0, 0, 0, 's', 'MarkerFaceColor', 'red');
        axis equal; hold off;
    end
    nexttile
end

% plotting histograms of the locations
if freq
    for i = 1:dim
        histogram(steps(:,i),20)
        if i ~= dim
            nexttile
        end
    end
end
