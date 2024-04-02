print("Enter word and hit enter for next word. type 'Q' or 'q' to exit")

word = ""
list_word = []
word = input()
while(word != 'Q' and word != 'q'):
	list_word.append(word)
	word = input()

# print(list_word)
if(len(list_word) != 0):
	list_word.sort()

print(list_word)