import re

def regex_tic_tac_toe_win_checker(board):
    return re.match(r'(|...|.{6})(\w)\2\2|.*(\w)..\3..\3|(\w)...\4...\4|..(\w).\5.\5', board) is not None