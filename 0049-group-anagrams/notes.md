# Notes

## Solution 1

Uses a dictionary to store the sorted string and the list of anagrams as a key value pair, once done returns all the values of the dictionary as a list, slower due to sort. O(n*log(n))

## Solution 2

Uses a letter prime map to calculate the product of those primes to the key that is then used in the dictionary, faster due to instant key access. O(n)
