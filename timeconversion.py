twelvehr = "12:45:54PM"
daynight = twelvehr[-2]+twelvehr[-1]
if daynight == "AM" and int(twelvehr[:2]) == 12:
    t1 = twelvehr[:2]
    t2 = str("00")
    twentyfourhr = twelvehr.replace(t1, str(t2), 1)
    print(twentyfourhr[0:-2])
elif daynight == "AM":
    print(twelvehr[0:-2])
elif daynight == "PM" and int(twelvehr[:2]) == 12:
    print(twelvehr[0:-2])
else:
    t1 = twelvehr[:2]
    t2 = int(t1)+12
    twentyfourhr = twelvehr.replace(t1, str(t2), 1)
    print(twentyfourhr[0:-2])
