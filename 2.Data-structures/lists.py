motorcycles = ['honda', 'yamaha', 'suzuki']

################### INSERT #####################

#Append in the last position of the list
motorcycles.append('ducati')
#Insert element in specific position of the list
motorcycles.insert(0, 'daelim')

################### DELETIONS #####################

#Remove specific element of the list
del motorcycles[1]
#Remove the last element of the list and it return it.
last_element = motorcycles.pop()
#Also we can remove specific element with pop and get the value deleted. 
element = motorcycles.pop(0)
#Remove element by value (The remove() method deletes only the first occurrence of the value you specify)
motorcycles.remove('yamaha')


################# SORT ######################

#Sort alphabetical or reverse permantly
motorcycles.sort()
motorcycles.sort(reverse=True)
#Sort list temporaly
sorted(motorcycles)
#Give reverse to the list (Darle la vuelta a una lista)
motorcycles.reverse()


#MAKING NUMERICAL LISTS range(x,y-1)
for value in range(1,5):
    break
    print(value)

even_numbers = list(range(2,11,2)) #Lista de pares del 2 al 10

min(even_numbers) #Minimum
max(even_numbers) #Maximum
sum(even_numbers) #Sum 

################# COPY LIST ######################

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #IMPORTANT [:] if not they will point to the same list (friends_foods = my_foods doesn't work)