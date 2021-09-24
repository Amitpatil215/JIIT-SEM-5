def removeNthChar(string, index):
  str1 = string[:index]
  str2 = string[index+1:]
  str3 = str1+str2
  return str3


sentence = input("Enter any sentence: ")
index = int(input("Enter the index value: "))
print(removeNthChar(sentence, index))

"""
Enter any sentence: amit working on flutter
Enter the index value: 8
amit woring on flutter

"""
