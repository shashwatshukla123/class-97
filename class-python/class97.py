print("hello world")

myname="shashwat"
print(len(myname))
print(myname)

mygrade=9
print(mygrade)

myfriendlist=["kishan","shvanshi"]
print(len(myfriendlist))
print(myfriendlist)
print(myfriendlist[1])
print(type(myfriendlist))

print(type(mygrade))

print(type(myname))
 
name=input("What is your name")
print(name)

hi="hello"
print(hi+name)

introString=input("Enter String: ")
characterCount=0
wordCount=1
for i in introString:
    characterCount=characterCount+1
    if (i=='  '):
        wordCount=wordCount+1

print("number of Words in the string :")
print(wordCount)
print("number of characters in the string: ")
print(characterCount)
