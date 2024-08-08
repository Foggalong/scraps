% Simulates the St. Petersberg paradox a variable number of times for
% user-set cost, stake, and chance of success. My hypothesis as to why
% the game may seem tempting to run (or conversely why a gambler would have an
% aversion to playing) is that the chance of payout is very small, even if
% on average the payout would cover all previously incurred costs.

cost    = 500;
stake   = 2;
chance  = 0.5;
games   = 100;
payouts = zeros(1, games);

for i = 1:games
    payout = stake;
    while rand < chance
        payout = 2*payout;
    end
    payouts(1,i) = payout;
end

boxplot(log(payouts))
sum(payouts)
