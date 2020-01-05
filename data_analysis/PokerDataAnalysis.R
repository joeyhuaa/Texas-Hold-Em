data = read.csv('/Users/joeyhua/PycharmProjects/Texas-Hold-Em/simulation-winrates.csv')

## INTRODUCTION
## using my python Poker class, I simulated 999 rounds of 100 games each, AA vs. KK
## i wanted to test whether the resulting histograms would prove that my program was 
## running properly
## beyond simply outputting mathematically correct percetanges,
## if the histograms resembled a gaussian, 
## then that would prove my Poker class was running true binomial experiments


## THE PROCESS
# histogram of AA winrate (AA vs KK) to verify that the results are approx. gaussian
hist(data[1:999,1], 
     main = 'AA vs KK (999 Binomial Experiments)', 
     xlab = 'AA Win %',
     ylab = 'Frequency out of 999',
     col = 'red')

# histogram of KK winrate (AA vs KK) to verify that the results are approx. gaussian
hist(data[1:999,2],
     main = 'AA vs KK (999 Binomial Experimentss)',
     xlab = 'KK Win %',
     ylab = 'Frequency out of 999',
     col = 'blue')

# scatter plot should be very close to a straight line
scatter.smooth(x = data[1:999,1], 
               y = data[1:999,2],
               main = 'AA Win % vs KK Win %',
               xlab = 'AA Win %',
               ylab = 'KK Win %')


## CONCLUSION
## the histograms are rather skewed but still resemble bell curves nonetheless
## running more trials would probably help


