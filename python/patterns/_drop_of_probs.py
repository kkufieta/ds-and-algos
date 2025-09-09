'''
Graphs:
* Shortest path between cities: Given multiple paths from city A to city B, find the shortest path to reach city B from city A.
* (not graphs) Sort colors: Given a list of three colors, represented by 0, 1, and 2, sort the array in place so that the elements of the same color must be adjacent.
* (not graphs) Set zeroes: Given an mxn integer matrix, if an element is 0, set its entire row and column to 0's.
* Network communication failure: Given a network of routers connected to each other, find such a path between two routers whose removal will fail the communication across the network.
* (not graphs) Check for cycles: Given the head of a linked list, determine if the linked list has a cycle in it.
* Shortest clear path length: Given an nxn binary matrix grid, find the length of the shortest clear path in the matrix.
* Network delay time


1. Generate a string of n balanced parentheses.
2. Find all permutations of the following set of elements: {1,2,3}.
3. Check whether a given string is a palindrome.
4. Detect a cycle in a linked list.
6. Reverse the words in a given sequence of letters.
7. Middle of the linked list: Given the head of a singly linked list, return the middle node of the linked list.
8. Detect cycle in an array: Given an array of non-negative integers where elements are indexes pointing to the next element, determine if there is a cycle in the array.
9. Convert an infix expression (like 3+4x5) to a postfix notation (like 3 4 5x+).
10. Find the k-th largest element in an unsorted array.
* Find the minimum number of perfect squares summing to a positive integer n.
* Check if the parentheses in a mathematical expression are balanced or not. 
* Evaluate postfix expression, e.g.: `[2, 3, *, 5, +]` --> 11
* Reverse a string using a stack
* Two sum: Check for a pair in an array with a target sum.
  --> Example:
    a = [1, 3, 34, 7, 11, 23]
    target = 18
    output = (7, 11)

* Word count: Find the occurrence of every word in a string.
* Find the kth smallest element in an array.
* Given an array of integers, find the contiguous subarray with the largest sum.
* Divide an array into pairs whose sum is divisible by 2.
* Contains duplicate II (see Hashmap Notes)
* Count prefixes of a given string (see Hashmap Notes)
* Given a half-filled board, fill the empty cells to solve the Sudoku puzzle.
* Given a string, count the substrings that have all of the vowels.
* Detect a cycle in a graph.
* Shift all 0s in an array to the right.

* Find a peak element in an array where the peak element is the one that’s strictly greater than its immediate left and right neighbors.
    Assume that adjacent elements in the array can never be equal.

Linked List problems:
* Given a linked list, bring all nodes with negative values at the start of the linked list.
* Given a linked list, determine if it contains a cycle.
* Given a linked list of length 10, reverse the nodes from position 3 to position 7.
* Given the head of a singly linked list, return the middle node of the linked list. 
* Rotate a linked list clockwise k times

Trees:
Find the zig-zag level order traversal of a binary tree.
Find the maximum path sum in a binary tree. The path may start and end at any node in the tree.
Find the lowest common parent node of two given nodes in a binary tree.
Connect all the siblings at each level in a binary tree.
Path sum: Determine if the tree contains a root-to-leaf path, such that adding up all the values along the path equals the specified target sum
Valid binary search tree: Determine if a tree is a valid binary search tree
Find the lowest common ancestor of two given nodes in a binary tree.
Traverse a tree one level at a time and print out the node values in the same order.
Find the shortest path between two given nodes, u and v, in a binary tree.
Connect all the nodes at the same level in a binary tree.
Bottom-up order traversal
Minimum depth of a tree

Bitwise Manipulation:
Swap without extra space
Check for even/odd without division/modulus
Check if an integer is a power of 2.
(not bitwise) Given a set of positive integers and a target sum, determine whether there is a subset of the given set that adds up exactly to the target sum.
Given an array where every element occurs even times except for one element occurring odd times, find the element with the odd occurrence.
(not bitwise) Find the maximum element in an unsorted array.

Matrices:
Toeplitz matrix
Rotate and invert an image
Rotate an image.
(not matrices) Find the longest palindromic sequence in a given string.
(not matrices) Implement a basic calculator.
Given an $m \times n$ map of a server center, return the number of servers that communicate with any other server.

Intervals:
Meeting rooms: Can a person attend all meetings?
(not intervals) Find the 3rd closest point to the origin.
Schedule three interviews for an interviewer in one day.
For a football tournament, find the durations during which more than one games are being played simultaneously.
(not intervals) Given an unsorted array of integers, find the length of the longest increasing subsequence.

K-way merge:
Median of k sorted arrays 
The k-th smallest element in multiple sorted arrays
(not k-way merge) Find out if the given string is a palindrome or not
Merge 5 sorted arrays
(not k-way merge) Find the middle of the linked list
Find the 2nd smallest number in 20 sorted arrays

Cyclic sort:
Set mismatch
Find the k-th missing positive number
(not cyclic sort) Given a string representing a number, return the closest number that is a palindrome.
Given an array of numbers in the range 1 to n, find all the numbers that are missing in the array.
Given a set of numbers, find the first 5 missing positive numbers.
(not cyclic sort) Given a set, return the number of subsets with the sum equal to 10.

Top k elements:
Sort characters by frequency 
Connect n ropes with minimum cost
Rearrange the given string so that no two identical characters are adjacent to each other.
(not top k elements) Detect a cycle in a linked list.
Find the five nearest points to the origin.
(not top k elements) Implement a stack in which the pop operation removes the most frequent element.
Kth Largest Element in a Stream

Heaps:
*  Last Stone Weight
* Find the median of a number stream
* Find Right Interval
* Sliding window median
Given an array, find the difference between the maximum and minimum elements in each window of size 4 as it slides through the array.
* Sort the characters of the given string by frequency. 
* Design a data structure to store a collection of integers supporting the following two operations:
		1. Add an integer to the collection.
		2. Find the median of all the elements in the collection in constant time
* (not heaps) Given the string “hellocodingking”, find the longest substring with 5 distinct characters. 
* Given an array of unique athlete scores, rank them based on their scores. The top three athletes get “Gold,” “Silver,” and “Bronze” medals, while athletes ranked 4th and below receive their respective position numbers as ranks. Return an array containing the ranks in the same order as the input.
* Schedule tasks on Minimum Machines problem

Greedy Algorithms:
* Find the path with maximum sum of node values 
* Loading maximum containers in a cargo
* Graph Coloring
* Find the shortest period of time to schedule a set of jobs on a set of machines.
* (not greedy algorithm) Find the number of palindromic substrings contained in a given string.
* Find the shortest path between two intersections on a road map.
* Find the most cost-effective way to lay an optical fiber cable in a neighborhood, such that all the houses get connected.

Sliding window:
* Maximum sum subarray of size k
* Longest substring without repeating characters
* (not sliding window) Locate the 6th largest element in an array. 
* Given a string S and a string T, find the shortest substring in S that contains all the characters in T.
* Given an array of integers and a target sum, find the length of the smallest subarray whose sum is greater than or equal to the target sum.
* (not sliding window) Find safe places for five queens on a 5x5 chessboard.

'''