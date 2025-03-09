def multiply(a, b):
   return a * b


def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    elif boolean ==False:
        return "No"


la_liga_goals = 43
champions_league_goals = 10
copa_del_rey_goals = 5

total_goals = la_liga_goals + champions_league_goals + copa_del_rey_goals


def positive_sum(arr):
    list = 0
    for i in arr:
        if i > 0:
            list = i + list
    
    
        
            
    return list


numbers = [5, 10, 15, 20, 25]
total_sum = sum(numbers)
print( total_sum)


max_number = max(numbers)
print( max_number)

min_number = min(numbers)
print( min_number)

length = len(numbers)
print( length)

words = ["apple", "banana", "cherry", "date", "elderberry"]
words.append("fig")
print( words)

words.insert(2, "grape")  
print( words)

removed_word = words.pop(1)  



