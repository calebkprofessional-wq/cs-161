from time import sleep

print("1._______________________________________________________")

x = int(input("Enter a number: ").strip())
while x > 0:
    print(x)
    x-=1
print("Blastoff!!")

print("2._______________________________________________________")

x = int(input("Enter a number: ").strip())
while x > 0:
    if x % 2 == 0:
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")
    x-=1
print("Blastoff!!")

print("3._______________________________________________________")

x = int(input("Enter a number: ").strip())
y = int(input("Decrease by: ").strip())
while x > 0:
    if x % 2 == 0:
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")
    x-=y
print("Blastoff!!")

print("4.1._______________________________________________________")

while True:
    word = input("Enter a word: ").strip()
    if len(word) < 5:
        print("Goodbye.")
        break
    else:
        print(f"{word} has {len(word)} letters.")
        continue

print("4.2._______________________________________________________")

tries = 0
while True:
    if tries > 4:
        print("Loser.")
        break
    word = input("Enter a word: ").strip()
    if len(word) < 5:
        print("Goodbye.")
        break
    else:
        print(f"{word} has {len(word)} letters.")
        tries+=1
        continue

print("5._______________________________________________________")

print(3)
sleep(1)
print(2)
sleep(1)
print(1)
sleep(1)
for i in range(10, 101):
    bin_i = bin(i)
    hex_i = hex(i)
    print(f"{i}, {bin_i}, {hex_i}")

print("6. (iterative)_______________________________________________________")

length = int(input("Enter the number of stars: ").strip())
while length > 0:
    stars = "*" * length
    print(stars)
    length-=1

print("6. (recursive)_______________________________________________________")

def stars(func_length):
    if func_length == 0:
        return
    func_stars = "*" * func_length
    print(func_stars)
    func_length-=1
    stars(func_length)

length = int(input("Enter the number of stars: ").strip())
stars(length)