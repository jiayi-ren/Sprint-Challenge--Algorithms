#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The time complexity is O(n) because at each iteration n^2 is added to a. n^2 * n = n^3. Hence, the function will loop n times.


b) The time complexity is O(n log(n)). The nested while loop's time complexity is O(log(n)) because j is double every iteration hence not linear. The outer loop has n iteration.


c) The time complexity is O(n) since the function recurse itself n times from bunnyEars(n-1) to bunnyEars(0). 

## Exercise II

One way is to start throw egg from the first floor until th egg breaks. The worst case scenario is floor f will be the last floor of n-story building. Hence time complexity is O(n)
