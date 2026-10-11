# Notes

-- TODO: not solved

## Solution 1

Pop the largest k times and return it, this doesn't solve the problem because we exceed the time limit.

## Solution 2

Using quick select, non-recursive, O(n) time complexity on average.

## Solution 3

Using quick select, recursive (uses more space + list slicing shallow copies which takes even more space), O(n) time complexity on average

## Solution 4

Using quick select, recursive (uses more space), O(n) time complexity on average
