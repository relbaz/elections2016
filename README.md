# elections2016. Obviously this didn't go as planned..

2016 elections simulations

A very simple elections simulation: repeat K = 5000 rounds, where for each round iterate on all the states and simulate it going to democrats or republicans according to current probabilities from the new york times (Nov 7 early am).

Sum the number of democrat wins, republican wins, and ties, out of K.
Also print a list of the more common electroal votes.

Interestingly, in this model Trump only gets 3% chance of winning.

### edit Nov 23
My guess is that the states' winning probabilities from the NYTimes were wayyyy off. There are minor issues of dependence between states but that shouldn't have caused such a big difference from the real results.  
