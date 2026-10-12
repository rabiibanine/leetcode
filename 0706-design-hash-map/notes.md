# Notes

New type of problem.

## Solution 1

Uses an array of 10^6 elements, since thats the max that the problem is going to give each element can live in it's own table cell, a naive solution (not really a hash table)

## Solution 2

Uses buckets of size 769 (a prime number which helps even out the spread of values), uses a resize which doubles the size (not optimal, the ideal solution involves calculating the next prime, wasn't bothered to code implement it)
