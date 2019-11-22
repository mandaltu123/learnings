def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese")
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Man! That's enough for party")
    print("Get a blanket\n")


print("We can just give the function numbers directly")
cheese_and_crackers(10, 20)

print("Or we can use some variables from our script")
amount_of_cheese = 10
amount_of_crackers = 20

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too")
cheese_and_crackers(10 + 2, 20 * 3)
