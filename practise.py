# Write a python program to count the number of strings where the
# string length is 2 or more and the first and last character are 
# same from a given list of strings

def String_count(words):
    count = 0
    for i in words:
        if(len(i)>1 and i[0]==i[-1]):
            count += 1
    return count


words = [input() for words in range(5)]
print(String_count(words))