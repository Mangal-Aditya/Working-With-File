''' Let me tell you what did I just did ,so first I open a file in reading mode then read the file content and store the string value at readingFile variable now as it is a string so when I run the len() in the string i actually get the charecter . 

Now spiltline split the new line ( I came to learn that in the string its find \n and if its find it just take the all privious value and make it the  first index of the list and so on  ) so when I run len() in the  line valiable its shows me how many line is present in my file as all the line are just an index of an list .

Now as the reading file is a string when we perform the split method on the file (readingFile , where I store the file content) I actually split the whole thing on the basis of the " " so every its gate a space its make the previous one an index if the list and when I run the len() method its give me the count of words
 '''


fileName  = open('Mangal.txt','r')

readingFile = fileName.read()
line = readingFile.splitlines()
words = readingFile.split()


print("Line count :",len(line))

print("words count :",len(words))
print("charecter number :",len(readingFile))


