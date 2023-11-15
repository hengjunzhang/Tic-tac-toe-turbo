from logic import check_winner
#test None
test_board = [[None,"X","O"], ["X",None,"O"], ["X","X",None]]
winner = check_winner(test_board)
print(winner)

#test X
test_board = [["X","X","O"], ["X",None,"O"], ["X","X",None]]
winner = check_winner(test_board)
print(winner)


#test O
test_board = [[None,"X","O"], ["X",None,"O"], ["X","X","O"]]
winner = check_winner(test_board)
print(winner)
