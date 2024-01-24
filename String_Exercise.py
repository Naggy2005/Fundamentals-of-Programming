
#Take user input and set to variable
user_string= str(input("Enter a name: "))

#Get first charcter using index 0
first_char = user_string[0]

#Get Last charcter using index -1
last_char= user_string[-1]



str_length= len(user_string)
mid_index = int(str_length/2)#Need to convert to int because indices should always be integer

mid_char= user_string[mid_index]
new = first_char + mid_char + last_char
print(new)