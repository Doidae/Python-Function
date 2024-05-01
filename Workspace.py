def hello():
    print("Hello! Welcome to our program.")

def pack(item1, item2, item3):
    return [item1, item2, item3]

def eat_lunch(lunch_items):
    if not lunch_items:
        print("My lunchbox is empty!")
    else:
        print("First I eat", lunch_items[0])
        for item in lunch_items[1:]:
            print("Next I eat", item)



hello()
packed_items = pack("Sandwich", "Apple", "Chips")
print("Packed items:", packed_items)
eat_lunch(packed_items)