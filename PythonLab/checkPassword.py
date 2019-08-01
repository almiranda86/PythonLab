def checkio(data: str) -> bool:

    if len(data) < 10:
        return False
    elif not any(c.isdigit() for c in data):
        return False
    elif not any(c.isupper() for c in data) or not any(c.islower() for c in data):
        return False
    else:
        return True
#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    assert checkio('erer798rew9rew9r7ew987rw') == False
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
