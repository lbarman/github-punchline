import datetime
import subprocess

letterWidth = 4
letterHeight = 7

A = [[0,0,0,0],
	 [0,0,1,0],
	 [0,1,0,1],
	 [0,1,1,1],
	 [0,1,0,1],
	 [0,1,0,1],
	 [0,0,0,0]];

C = [[0,0,0,0],
	 [0,0,1,1],
	 [0,1,0,0],
	 [0,1,0,0],
	 [0,1,0,0],
	 [0,0,1,1],
	 [0,0,0,0]];


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
letters = [A, C];

#compose the list
grid = [];

for letter in letters:
	for x in range(letterWidth):
		for y in range(letterHeight):
			grid.append(letter[y][x])

# browse on the flattened list
for daysSinceBeginning in range(len(grid)):

	#compute date
	dateForThisDay = dateTopLeftCorner + datetime.timedelta(days=daysSinceBeginning)

	formattedDate = dateForThisDay.strftime("%a %b %d %H:%M:%S CET %Y")

	print(formattedDate, "->", grid[daysSinceBeginning], "->", daysSinceBeginning, "/", 365)

	if grid[daysSinceBeginning] > 0:
		#print(formattedDate, "->", grid[daysSinceBeginning])
		subprocess.call(["./create-commit-for-date.sh", formattedDate])