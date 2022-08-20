## Finding the Closest Starbucks to Houses in the US

This program uses the Sklearn library's neighbors.distancemetric method to find the nearest starbucks to a list of housing addresses in the US.
The starbucks data is open source and contains the latitude and longitude of all starbucks locations in the US.
The housing data is an open source dataset from home physical inspection scores in the US.

This program uses the the latitude and longitude of all locations to find the Haversine distance between each of them, and keep the smallest distance.
The program currently runs as a brute force method with high time complexity, however a faster solution is being worked on.
