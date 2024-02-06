# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:52:53 2024

@author: uviwe
"""

import pandas as pd
import matplotlib.pyplot as plt

#import dataset
movie = pd.read_csv("movie_dataset.csv")
movie.head()

#Highest rated movie in the dataset (Q1)
movie[movie.Rating == movie.Rating.max()]["Title"]

#Average revenue (Q2)
print(movie ['Revenue (Millions)'.split(',')])
x = movie["Revenue (Millions)"].mean()
movie["Revenue (Millions)"].fillna(x, inplace = True)
print(movie)

string = 'Revenue (Millions)'
ascii_sum = sum(ord(char) for char in string)
print("Sum of ASCII values:", ascii_sum)

#Calculate the length of the Revenue
string_length = len("Revenue (Millions)")

#calc average
average_ascii = ascii_sum / string_length
print("Average of ASCII value:", average_ascii)


#What is the average revenue of movies from 2015 to 2017 in the dataset? (Q3)
movies_2015_to_2017 = movie[(movie['Year'] >= 2015) & (movie['Year'] <= 2017)]
average_revenue_2015_to_2017 = movies_2015_to_2017['Revenue (Millions)'].mean()
print("Average revenue of movies from 2015 to 2017:", average_revenue_2015_to_2017)


#How many movies were released in the year 2016? (Q4)
year_2016 = movie.Year.value_counts()
year_2016

#How many movies were directed by Christopher Nolan? (Q5)
director_ChrisNolan = movie[movie["Director"] == "Christopher Nolan"]
director_ChrisNolan_count = len(director_ChrisNolan)
print("Number of movies directed by Christopher Nolan:", director_ChrisNolan_count)

#How many movies in the dataset have a rating of at least 8.0? (Q6)
rating_count = movie[movie["Rating"] >= 8.0]
movie_ratings = len(rating_count)
print("Number of movies with a rating of at least 8.0:", movie_ratings)

#What is the median rating of movies directed by Christopher Nolan? (Q7)
nolan_movies = movie[movie["Director"] == "Christopher Nolan"]
median_rating_nolan = nolan_movies["Rating"].median()
print("Median rating of movies directed by Christopher Nolan:", median_rating_nolan)

#Find the year with the highest average rating? (Q8)
average_rating_by_year = movie.groupby("Year")["Rating"].mean()
highest_avg_rating_year = average_rating_by_year.idxmax()
print("Year with the highest average rating:", highest_avg_rating_year)

#What is the percentage increase in number of movies made between 2006 and 2016? (Q9)
# Count the number of movies made in each year
movies_by_year = movie["Year"].value_counts()

# Get the number of movies made in 2006 and 2016
movies_2006 = movies_by_year.get(2006, 0)
movies_2016 = movies_by_year.get(2016, 0)

# Calculate the percentage increase
percentage_increase = ((movies_2016 - movies_2006) / movies_2006) * 100
print("Percentage increase in number of movies between 2006 and 2016:", percentage_increase)

#Find the most common actor in all the movies? (Q10)
all_actors = movie["Actors"].str.split(", ").explode()
# Count the occurrences of each actor
actor_counts = all_actors.value_counts()
# Determine the most common actor
most_common_actor = actor_counts.idxmax()
print("The most common actor in all the movies is:", most_common_actor)

#How many unique genres are there in the dataset? (Q11)
# Flatten the list of genres into a single list
all_genres = movie["Genre"].str.split(", ").explode()
# Convert the list of genres to a set to remove duplicates
unique_genres = set(all_genres)
# Count the number of unique genres
num_unique_genres = len(unique_genres)
print("Number of unique genres in the dataset:", num_unique_genres)

#Do a correlation of the numerical features, what insights can you deduce? Mention at least 5 insights. And what advice can you give directors to produce better movies? (Q12)
# Calculate correlation between Rating and Revenue
correlation_rating_revenue = movie["Rating"].corr(movie["Revenue (Millions)"])
print("Correlation between Rating and Revenue:", correlation_rating_revenue)

#Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(movie["Rating"], movie["Revenue (Millions)"], color='blue')
plt.title('Scatter Plot of Rating vs Revenue')
plt.xlabel('Rating')
plt.ylabel('Revenue (Millions)')
plt.grid(True)
plt.show()
