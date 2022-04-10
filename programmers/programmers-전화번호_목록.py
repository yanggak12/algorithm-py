def solution(phone_book):
    p_book = sorted(phone_book)
    for i in range(len(p_book)-1):
        if str(p_book[i+1]).startswith(str(p_book[i])):
            return False
    return True
