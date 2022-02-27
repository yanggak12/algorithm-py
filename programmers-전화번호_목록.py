def solution(phone_book):
    p_book = sorted(phone_book)
    for i, j in zip(p_book, p_book[1:]):
        if str(j).startswith(i):
            return False
    return True
