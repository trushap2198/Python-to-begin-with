import itertools  as it

def win_game(game):
	diag=[]
	for col,row in enumerate(reversed(range(len(game)))):
		diag.append(game[row][col])
	if diag.count(diag[0])==len(diag) and diag[0]!=0:
		print("congo..you did it");
		return 1;
	diag=[]
	for ix in range(len(game)):
		diag.append(game[ix][ix]);	
	if diag.count(diag[0])==len(diag) and diag[0]!=0:
		print("you did it daigonally")
		return 1;

	for col in range(len(game)):
		ver=[]
		for row in game:
			ver.append(row[col])
			#print(ver);
		if ver.count(ver[0])==len(ver) and ver[0]!=0:
			print("you did it vertically")
			return 1;

	for row in game:
		if row.count(row[0])==len(row) and row[0]!=0:
			print("you did it horizontally")
			return 1;
	return 0;
def Move(game_map,col_m=0,row_m=0):
	
	if game_map[row_m][col_m]!=0:
		print("position occupied")
		flag=1;
		return 0;
	else:
		game_map[row_m][col_m]=1;
		win=win_game(game_map)
	if(win):
		return 1;
	else:
		return 0;


game_won=0;
game=[[0,0,0],[0,0,0],[0,0,0]];
players=it.cycle([1,2])
while not game_won:
	if(flag==0):
		curr_player=next(players);
	else:
		curr_palyer=
	print("current palyer=",curr_player);
	print("current map=",game)
	col_choice=int(input("which move col you want"))
	print(col_choice)
	row_choice=int(input("which row you want"))
	game_won=Move(game,col_choice,row_choice);