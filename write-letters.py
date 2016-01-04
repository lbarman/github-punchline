import datetime
import sys
import subprocess
import os
from letters import * #import in current namespace

# finds the date x=0,y=0 on github grid
today = datetime.datetime.now()
dayOfTheWeek = datetime.datetime.today().weekday() #starts on sunday
DD_day = datetime.timedelta(days=dayOfTheWeek+1)
DD_year = datetime.timedelta(weeks=52)
dateTopLeftCorner = today - DD_day
dateTopLeftCorner = dateTopLeftCorner - DD_year

earlier_str = dateTopLeftCorner.strftime("%d/%m/%Y")
print(earlier_str)

# word to print
letters = [P,R,O,B,A,B,L,Y, space, N,O,T];

#compose the list
grid = [];

for letter in letters:
	for x in range(len(letter[0])):
		for y in range(len(letter)):
			grid.append(letter[y][x])

for shift in range(7):
	i = shift
	s = ""
	while i<len(grid):
		if grid[i]==1:
			s += "x"
		else:
			s += " "
		i += 7
	print(s)

# browse on the flattened list
for daysSinceBeginning in range(len(grid)):

	#compute date
	dateForThisDay = dateTopLeftCorner + datetime.timedelta(days=daysSinceBeginning)

	formattedDate = dateForThisDay.strftime("%a %b %d %H:%M:%S CET %Y")

	print(formattedDate, "->", grid[daysSinceBeginning], "->", daysSinceBeginning, "/", 365)

	if grid[daysSinceBeginning] > 0:
		#print(formattedDate, "->", grid[daysSinceBeginning])
		subprocess.call(["./create-commit-for-date.sh", formattedDate])