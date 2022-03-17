# hours=input('How many hourse you worked this month? ')
# h=float(hours)
# rate=10.50

# if h<=40.0:
#     print(h*rate)
# else:
#     print((40*rate)+((h-40.0)*(1.5*rate)))


# quiz 2

# grade=float(input('Enter your grade :'))
# if grade>= 0.9:
#     print('A')
# elif grade>= 0.8:
#     print('B')
# elif grade>= 0.7:
#     print('C')
# elif grade>= 0.6:
#     print('D')
# elif grade< 0.6:
#     print('F')
# else:
#     print('No grade entered') 



# def computepay(h,rt):
#     if h<=40.0:
#         return h*rt
#     else:
#         return ((40*rt)+((h-40.0)*(1.5*rt)))
# h=(input('Enter hours: '))
# h=float(h)
# p=computepay(45,10.50)
# print('Pay: ',p)


# a=5 
# print('Welcome')
# while a<8:

#     print(a)
#     print('Ulvi')
#     a+=1
#     if a==7:
        
        
#         print("Don't print me please!")
#     print('Bye bye')




# smallest_so_far = -1
# for the_num in [9, 41, 12, 3, 74, 15] :
#    if the_num < smallest_so_far :
#       smallest_so_far = the_num
# print(smallest_so_far)



# Look through the code block again and again!
# Look through the code block again and again!
# Look through the code block again and again!
# Look through the code block again and again!
# Look through the code block again and again!
# largest = -1
# smallest = None

# while True:
#     num = input("Enter a number: ")
#     if num== "done":
#         break   
#     try:
#         num=int(num)
#         if num>largest:
#             largest=num
#         elif smallest is None:
#             smallest=num      
#     except:
#         print('Invalid input')   

# print("Maximum", largest)
# print('Minimum', smallest)
 
# Look through the code block again and again!
# Look through the code block again and again!
# Look through the code block again and again!
# Look through the code block again and again!
# Look through the code block again and again!



# text = "X-DSPAM-Confidence:    0.8475"
# text.find('0')
# text.find('5')
# print(float(text[23:]))
# print(float(text[text.find('0'):]))
# def text():
#     from os import read, write
#     fname=input('Enter file name: ')
#     name=open(fname)
#     for x in name:
#         x=x.strip()
#         print(x.upper())

# name=open('words.txt','w')
# name.write(text())


# fname=input('Enter the file name: ')
# note=open(fname)
# counter=0
# total=0
# for line in note:
#     if line.startswith("X-DSPAM-Confidence:"):
        
#         counter+=1
        
#         confidence=float(line[20:])
#         total+=confidence
# average=total/counter       
# print("Average spam confidence: "+str(average))


# text=open("romeo.txt")
# word_list=list()

# for words in text:
#     word=words.split()
#     word_list.append(word)
# word_list.sort()

# print(*word_list, sep='')
    
    
#exercise_8.5

# fname=input("Enter the file name: ")
# fh=open(fname)
# count=0
# for line in fh:
#     if "From:" in line:
#         x=(line.split("From: "))
#         mail=x[1]
#         count+=1
#         print(mail.strip("\n"))

# print("There were", count, "lines in the file with From as the first word")

        
# fname=input("Enter the file name: ")
# fh=open(fname)
# committer=dict()

# for line in fh:
#     if "From " in line:
#         x=(line.split("From "))
#         mail=x[1]
#         email=mail.split()
#         person=email[0]
#         committer[person]=committer.get(person,0)+1
# print(person,committer[person])

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(days[2])