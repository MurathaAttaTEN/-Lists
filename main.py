import numbers


letters=["a","b","c"]
matrix=[[0,1],[2,3]]
zeros=[0] * 5
combined=zeros + letters
number=list(range(20))
chars = list("hello world")
print(len(chars))
letters=["a","b","c","d"]
letters[0]="A"
print(letters[0:3])
print(letters[:2])
numbers=[1,2,3,4,4,4,4,9]
first,second,*other,last=numbers
first=number[0]
second=number[1]
third=[2]
print(first)
print(other)
for letter in letters:
    print(letter[0],letter[1])
for index, letter in enumerate(letters):
    print(index,letter)
    #add
    letters.append("d")
    letter.insert(0,"-")
    print(letters)
    #remove
    letters.pop(0)
    letters.remove("b")
    del letters[0:3]
    letters.clear()
    print(letters)
    print(letters.index("a"))
    


