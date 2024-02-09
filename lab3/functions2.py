#1
def imdb_check(arr):
    for x in arr:
        if x["imdb"] > 5.5:
            print(x["name"])



#2
def sublist(arr):
    a = []
    for x in arr:
        if x["imdb"] > 5.5:
            a.append(x)
    print(a)



#3
def category_of_movie(s, arr):
    k = True
    for x in arr:
        if x["category"] == s:
            print(x)
            k = False
    if k:
        print("There are no movies in this category")



#4
def average_imdb(arr):
    a = 0.0
    b = 0
    for x in arr:
        a += x["imdb"]
        b += 1
    print(a / b)


#5
def average_imdb_of_category(arr, c):
    a = 0.0
    b = 0
    k = True
    for x in arr:
        if x["category"] == c:
            a += x["imdb"]
            b += 1
            k = False
    if k:
        print('There are no movies in this category')
    else:
        print(a / b)


movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]



print("1. IMDB score is above 5.5:")
imdb_check(movies)

print("2. A sublist of movies with an IMDB score above 5.5:")
sublist(movies)

s = input("Now select movie category(Thriller, Action, Adventure, Drama, Romance, War, Crime, Comedy, Suspense) \n")
print("3. Movies of category", s, ":")
category_of_movie(s, movies)

print("4. The average IMDB score:")
average_imdb(movies)

c = input("Now select movie category again(Thriller, Action, Adventure, Drama, Romance, War, Crime, Comedy, Suspense) \n")
print("5. The average IMDB score of", c, "category:")
average_imdb_of_category(movies, c)