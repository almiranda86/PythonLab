def definehour(hour):
    if hour.startswith("1"):
        if hour == "13":
            return "1"
        elif hour == "14":
            return "2"
        elif hour == "15":
            return "3"
        elif hour == "16":
            return "4"
        elif hour == "17":
            return "5"
        elif hour == "18":
            return "6"
        elif hour == "19":
            return "7"
        else: 
            return "12"
    elif hour.startswith("2"):
        if hour == "20":
            return "8"
        elif hour == "21":
            return "9"
        elif hour == "22":
            return "10"
        elif hour == "23":
            return "11"
         


def time_converter(time):
    
    period = ""
    hour = time.split(':')
    if hour[0] < "12":
        period = " a.m."
        if hour[0] == "00":
            hour[0] = "12"
        elif hour[0] < "10":
            hour[0] = hour[0].lstrip("0")
    else:
        hour[0] = definehour(hour[0])
        period = " p.m."


    return hour[0] +":"+ hour[1] + period

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert time_converter('12:30') == '12:30 p.m.'
    #assert time_converter('09:00') == '9:00 a.m.'
    #assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")