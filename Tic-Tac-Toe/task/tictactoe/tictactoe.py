# write your code here
cells = input("Enter cells:")
tic_tac_toe = [cells[n:n + 3] for n, row in enumerate(cells) if n % 3 == 0]
print("---------")
for i in range(len(tic_tac_toe)):
    print("|" , *tic_tac_toe[i] , "|", sep=" ")
print("---------")
