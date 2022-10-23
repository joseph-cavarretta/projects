## Finding the Closest Starbucks to Houses in the US

What's the fastest way to find the closest Starbucks to any house in the US?

In one of my previous roles, I encountered a business problem where I needed to take a list of thousands of locations and, for each one, find the nearest location from another list with thousands of potential matches (using latitude and longitude).

Initially, I used a k-nearest neighbors pairwise approach to find the distance of every location to every other location (cartesian product) and keep the smallest distance for each one. But with over 10,000 locations in each list, this brute force method took several hours to run.

After some additional research, I was able to optimize my approach to run in under 1 minute using a Ball Tree algorithm.

Using a US housing dataset and a list of all Starbucks locations in the US, I've recreated this problem using both approaches here: https://lnkd.in/gtwggkbm

**Runtime to find the closest Starbucks to each house using brute force?** 20 minutes 24 seconds.

**Runtime using the Ball Tree?** 1.44 seconds!

**Average distance to a Starbucks from over 27,000 houses in the US?** 8.15 miles :)
