

# Make groups of people

import random
random.seed(21) # for reproducibility


def make_groups(people, numPeeps, numTeams, print_groups=1):
	groups = []
	while numPeeps > 0 and numTeams > 0:
		team = random.sample(people, int(numPeeps/numTeams))

		groups.append(team)

		for x in team:
			people.remove(x)

		numPeeps -= int(numPeeps/numTeams)
		numTeams -= 1
		

	if print_groups: # Print the groups
		_ = [print(grp) for grp in groups]

	return groups


people=[
"abby",
"Ali",
"carlene",
"emily",
"gema",
"Jake",
"julia",
"leon",
"marina",
"mulatwa",
"pooja",
"susana",
"vini",
"zahara"]


numTeams = 4
groups = make_groups(people, len(people), numTeams)


