import sys
import random
from collections import defaultdict

# data from http://www.nytimes.com/interactive/2016/upshot/presidential-polls-forecast.html?ref=politics
# as of Nov 7, 12:30am
# state name (typos are mine) mapped to prob(democrat wins) and electorates count
states = {
    'dc': (0.99, 3),
    'hawaii' : (0.99, 4),
    'california' : (0.99, 55),
    'massachusetes': (0.99, 11),
    'new york' : (0.99, 29),
    'Vermont' : (0.99, 3),
    'Rhode Island' : (0.99, 4),
    'Illinois' : (0.99, 20),
    'NJ' : (0.99, 14),
    'Washington' : (0.99, 12),
    'Md' : (0.99, 10),
    'Delaware' : (0.99, 3),
    'Connecticut' : (0.99, 7),
    'Me-1': (0.99, 1),
    'Oregon' : (0.97, 7),
    'va': (0.96, 13),
    'NM' : (0.94, 5),
    'Mich' : (0.92, 16),
    'Wis' : (0.91, 10),
    'Minneapolis' : (0.9, 10),
    'PA' : (0.89, 20),
    'Me' : (0.88, 2),
    'Colorado' : (0.86, 9),
    'NH': (0.8, 4),
    'Florida' : (0.7, 29),
    'Nevada' : (0.66, 7),
    'NC' : (0.66 , 15),
    'Ohio' : (0.46 , 18 ),
    'Iowa' : (0.37 , 6),
    'Me-2' : (0.35 ,1 ),
    'Utah' : (0.23 , 6),
    'Ga' : (0.2 , 16 ),
    'Arizona' : (0.19 , 11),
    'Mississippi' : (0.14 , 6),
    'South Carolina' : (0.12 , 9 ),
    'Alaska' : (0.07 , 3),
    'Tex' : (0.05 , 38 ),
    'Indiana' : (0.02 ,11 ),
    'Mo' : (0.02 ,10 ),
    'Louisiana' : (0.01 ,8 ),
    'Kansas' : (0.01 , 6),
    'Neb-1' : (0.01 , 1),
    'Tennessee' : (0.01 ,11 ),
    'Montana' : (0.01 , 3),    
    'Arkansas' : (0.01 ,6 ),
    'North Dakota' : (0.01 , 3),
    'West Virginia' : (0.01 , 5),
    'Alabama' : (0.01 , 9 ),
    'Nebraska' : (0.01 ,2 ),
    'Idaho' : (0.01 , 4),
    'South Dakota' : (0.01 , 3),
    'Oklahoma' : (0.01 , 7),
    'Kentucky' : (0.01 , 8),
    'Wyoming' : (0.01 , 3),
    'Neb-3' : (0.01 , 1),    
    }


def totalstates(states):
    tot = 0
    for s in states:
        (t, v) = states[s]
        tot += v
    return tot

def simulate(states):
    dem = []
    rep = []
    for s in states:
        (thshold, val) = states[s]
        r = random.random()
        if r < thshold:
            dem.append(s)
        else:
            rep.append(s)

    return (dem, rep)

def tally(states, dem, rep):
    d = 0
    r = 0
    for s in dem:
        (thshold, val) = states[s]
        d += val
    

    for s in rep:
        (thshold, val) = states[s]
        r += val

    return (d,r)

def main():
    dists = defaultdict(int)
    numsim = 5000
    demwins = 0
    repwins = 0
    ties = 0
    tot = totalstates(states)
    print "total votes: %s" % tot
    for i in range(numsim):
        (dem, rep) = simulate(states)
        (d, r) = tally(states, dem, rep)
        dists[d] += 1
        if d*2 > tot:
            w = "D!"
            demwins += 1
            continue
        elif r*2 > tot:
            w = "R!"
            repwins += 1
        elif r == d:
            ties += 1
            w = "**"
        print "%s dem: %d\trep: %d" % (w, d, r)

    print "D: %d  R: %d  Ties: %d" %(demwins, repwins, ties)

    print "heavy results:"
    for d in dists:
        if dists[d] > 65:
            print "%d\t %d" % (dists[d], d)

        
if False:# __name__ == "__main__":
    main()
else:
    main()
