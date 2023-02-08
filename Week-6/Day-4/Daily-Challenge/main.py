# Challenge 1
# Ask the user for a number and a length.
num    = int(input('give me a Number'));
length = int(input('give me a length too'));

# probabvly would be good if the inputs arent texts before we turn them to
# numbers or after we turn them to number
# Create a program that prints a list of multiples of the number until the list length reaches length.

i = 1
multi_list = []
while i < length + 1:
    multi_list.append(i*num);
    i+=1

print(multi_list)

# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
rep_word = input('give me a word with consecutive letters')
new_word = []
for i in range(0,len(rep_word)):
    if len(new_word) == 0:
        new_word.append(rep_word[i])
    if rep_word[i] in new_word:
        continue
    else:
        new_word.append(rep_word[i])

new_word = ''.join(new_word)
print(new_word)