"""
A hackathon has 2 separate tracks, healthcare and e-commerce.
For track1 there is requirement of teamSize1
For track2 there is requirement of teamSize2
Total participants are p
Find minimum number of teams into which the participants can be deivded such that 
each participant belongs to only one team and each team has team size either equal to teamSize1 or teamSize2
If no such division possible then return -1
"""

def countTeams(teamSize1, teamSize2, p):
    minT1 = p // teamSize1
    rem1 = p % teamSize1

    while minT1 >= 0:
        if rem1 % teamSize2 == 0:
            break 
        minT1 -= 1
        rem1 += teamSize1

    minT2 = p // teamSize2
    rem2 = p % teamSize2

    while minT2 >= 0:
        if rem2 % teamSize1 == 0:
            break 
        minT2 -= 1
        rem2 += teamSize2

    #print(minT1, rem1, minT2, rem2)
    if minT1 < 0 and minT2 < 0:
        return -1
    elif minT1 < 0:
        return minT2 + rem2 // teamSize1
    elif minT2 < 0:
        return minT1 + rem1 // teamSize2
    else:
        return min(minT1 + rem1 // teamSize2, minT2 + rem2 // teamSize1)
    
def main():
    teamSize1 = 3
    teamSize2 = 4
    p = 19

    result = countTeams(teamSize1, teamSize2, p)

    if result == -1:
        print("Cannot form teams")
    else:
        print("Minimum number of teams :", {result})

if __name__ == '__main__':
    main()