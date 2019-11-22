people = 30
cars = 40
trucks = 15

if cars > people:
    print("we should take cars")
elif cars < people:
    print("we should not take cars")
else:
    print("we cant decide")

if trucks > cars:
    print("there's too many trucks")
elif trucks < cars:
    print("may be we should take the trucks")
else:
    print("we still can't decide")

if people > trucks:
    print("alright, let's just take the trucks")
else:
    print("alright, let's just stay at home and watch some movie")
