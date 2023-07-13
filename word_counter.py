# word counter 
def word_counter(s):
    count={}
    for char in s:
        count[char]=s.count(char)
    return count

print(word_counter('mukesh'))    
print(word_counter('banana'))    

# word counter dictionary
user = {}

name=input('what is your name: ')
age =input('what is your age: ')
fav_movies=input('your fav movies separated by comma: ').split(',')
fav_songs=input('your fav songs separated by comma: ').split(',')

user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs

# print(user)

for key,value in user.items():
    print(f'{key} : {value}')
