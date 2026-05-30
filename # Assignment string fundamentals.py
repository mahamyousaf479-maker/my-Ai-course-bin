# Assignment string fundamentals 
#lenght of a string

text = 'Hello World'
print("\n lenght of string:")
print(text.__len__())

#for uppercase and lowercase
text = 'Python3'
print("\n uppercase:")
print(text.upper())

print("\n Lowercase:")
print(text.lower())

#count a character
text= 'banana'
char = 'a'
print("\n counted character:")
print(text.count(char))

#print first and last character
text = 'drawer'
print("first digit:")
print(text[0])
print(text[5])

#check substring presence
string = 'data science'
subtring = 'science'
text = subtring in string
print(text)

#slice a string
string = 'programming'
print(string[3:8:1])

#reverse a string
string = 'python'
print(string[::-1])

#replace substring
text = 'I love apples.Apples are great!'
print(text.replace('apple','orange'))

#split and join
text = 'split the sentence'
print(text.split())
stdata =  text.split()
print('-'.join(stdata))

#strip whitespace
word = '   padded text  '
print(word.strip())