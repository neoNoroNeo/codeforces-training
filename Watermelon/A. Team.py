repeat = int(input())
solved_problems = 0

for repeated in range(1,repeat+1):
    team = input()

    petya = int(team[0])
    vasya = int(team[2])
    tonya = int(team[4])

    team_capability = petya+vasya+tonya

    if team_capability >= 2:
        solved_problems = solved_problems + 1
    else:
        pass

print(solved_problems)