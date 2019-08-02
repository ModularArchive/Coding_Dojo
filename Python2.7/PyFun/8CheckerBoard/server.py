def board(evens,odds):
    evens =("* " * 4)
    odds =(" *" * 4)
    for i in range(0, 8):
        if i % 2 == 0:
            print(odds)
        else: 
            print(evens)
            #I couldn't get it to excute and print actual code. Even going online
            #and attempting other solutions they always came out blank. Help?
board()