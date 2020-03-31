def correct_tail(body, tail):
    return True if body [-len(tail):] == tail else False