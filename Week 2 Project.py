x = 31

print(x, bin(x), hex(x))

#x = 1.825
#print(x, bin(x), hex(x))
#this gives an error, because x needs to be an integer in this case for the bin and hex functions to work. we define x as something other than an integer, thus it throws an error

x = 18
print(x, bin(x), hex(x))

y = 0b1011

z = 0xA3

print(y, z)

w = x + y + z
print(f"the sum is {w}")

original_size = 240
dictionary_size = 25
compressed_text_size = 148

percent_compression = 1 - ((compressed_text_size + dictionary_size) / original_size)

print(f'''
Compressed text size: {compressed_text_size} characters
     Dictionary size: {dictionary_size} characters
               Total: {compressed_text_size + dictionary_size} characters
  Original text size: {original_size} characters
         Compression: {percent_compression * 100}%''')