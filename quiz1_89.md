# Coding Interview in Java
August 1 st, 2016

- [Coding Interview in Java](#coding-interview-in-java)
  * [1 Two Sum](#1-two-sum)
  * [2 Two Sum II Input array is sorted](#2-two-sum-ii-input-array-is-sorted)
  * [3 Two Sum III Data structure design](#3-two-sum-iii-data-structure-design)
  * [4 3Sum](#4-3sum)
  * [5 4Sum](#5-4sum)
  * [6 3Sum Closest](#6-3sum-closest)
  * [7 Minimum Size Subarray Sum](#7-minimum-size-subarray-sum)
  * [8 Remove Duplicates from Sorted Array](#8-remove-duplicates-from-sorted-array)
  * [9 Remove Duplicates from Sorted Array II](#9-remove-duplicates-from-sorted-array-ii)
  * [10 Remove Element](#10-remove-element)
  * [11 Move Zeroes](#11-move-zeroes)
  * [12 Container With Most Water](#12-container-with-most-water)
  * [13 Candy](#13-candy)
  * [14 Trapping Rain Water](#14-trapping-rain-water)
  * [15 Summary Ranges](#15-summary-ranges)
  * [16 One Edit Distance](#16-one-edit-distance)
  * [17 Merge Sorted Array](#17-merge-sorted-array)
  * [18 Shortest Word Distance](#18-shortest-word-distance)
  * [19 Shortest Word Distance II](#19-shortest-word-distance-ii)
  * [20 Shortest Word Distance III](#20-shortest-word-distance-iii)
  * [21 Intersection of Two Arrays Contents](#21-intersection-of-two-arrays-contents)
  * [22 Intersection of Two Arrays II](#22-intersection-of-two-arrays-ii)
  * [23 Median of Two Sorted Arrays](#23-median-of-two-sorted-arrays)
  * [24 Search Insert Position](#24-search-insert-position)
  * [25 Find Minimum in Rotated Sorted Array](#25-find-minimum-in-rotated-sorted-array)
  * [26 Find Minimum in Rotated Sorted Array II](#26-find-minimum-in-rotated-sorted-array-ii)
  * [27 Search for a Range](#27-search-for-a-range)
  * [28 Guess Number Higher or Lower](#28-guess-number-higher-or-lower)
  * [29 First Bad Version](#29-first-bad-version)
  * [30 Search in Rotated Sorted Array](#30-search-in-rotated-sorted-array)
  * [31 Search in Rotated Sorted Array II](#31-search-in-rotated-sorted-array-ii)
  * [32 Evaluate Reverse Polish Notation](#32-evaluate-reverse-polish-notation)
  * [33 Valid Parentheses](#33-valid-parentheses)
  * [34 Longest Valid Parentheses](#34-longest-valid-parentheses)
  * [35 Valid Palindrome](#35-valid-palindrome)
  * [36 Min Stack](#36-min-stack)
  * [37 Largest Rectangle in Histogram](#37-largest-rectangle-in-histogram)
  * [38 Maximal Rectangle](#38-maximal-rectangle)
  * [39 Valid Anagram](#39-valid-anagram)
  * [40 Group Shifted Strings](#40-group-shifted-strings)
  * [41 Palindrome Pairs](#41-palindrome-pairs)
  * [42 Insert Delete GetRandom O(1)](#42-insert-delete-getrandom-o-1-)
  * [43 Longest Substring Without Repeating Characters](#43-longest-substring-without-repeating-characters)
  * [44 Longest Substring with At Most K Distinct Characters](#44-longest-substring-with-at-most-k-distinct-characters)
  * [45 Substring with Concatenation of All Words](#45-substring-with-concatenation-of-all-words)
  * [46 Minimum Window Substring Contents](#46-minimum-window-substring-contents)
  * [47 Isomorphic Strings](#47-isomorphic-strings)
  * [48 Longest Consecutive Sequence](#48-longest-consecutive-sequence)
  * [49 Majority Element](#49-majority-element)
  * [50 Majority Element II](#50-majority-element-ii)
  * [51 Increasing Triplet Subsequence](#51-increasing-triplet-subsequence)
  * [52 Rotate Array in Java](#52-rotate-array-in-java)
  * [53 Reverse Words in a String II](#53-reverse-words-in-a-string-ii)
  * [54 Group Anagrams](#54-group-anagrams)
  * [55 Wildcard Matching](#55-wildcard-matching)
  * [56 Regular Expression Matching in Java](#56-regular-expression-matching-in-java)
  * [57 Get Target Number Using Number List and Arithmetic Operations](#57-get-target-number-using-number-list-and-arithmetic-operations)
  * [58 Flip Game](#58-flip-game)
  * [59 Flip Game II](#59-flip-game-ii)
  * [60 Word Pattern](#60-word-pattern)
  * [61 Word Pattern II](#61-word-pattern-ii)
  * [62 Scramble String](#62-scramble-string)
  * [63 Remove Invalid Parentheses](#63-remove-invalid-parentheses)
  * [64 Shortest Palindrome](#64-shortest-palindrome)
  * [65 Word Ladder](#65-word-ladder)
  * [66 Word Ladder II](#66-word-ladder-ii)
  * [67 Kth Largest Element in an Array](#67-kth-largest-element-in-an-array)
  * [68 Top K Frequent Elements](#68-top-k-frequent-elements)
  * [69 Meeting Rooms II](#69-meeting-rooms-ii)
  * [70 Meeting Rooms](#70-meeting-rooms)
  * [71 Range Addition Contents](#71-range-addition-contents)
  * [72 Merge K Sorted Arrays in Java](#72-merge-k-sorted-arrays-in-java)
  * [73 Merge k Sorted Lists](#73-merge-k-sorted-lists)
  * [74 Contains Duplicate](#74-contains-duplicate)
  * [75 Contains Duplicate II](#75-contains-duplicate-ii)
  * [76 Contains Duplicate III](#76-contains-duplicate-iii)
  * [77 Missing Number](#77-missing-number)
  * [78 Find the Duplicate Number](#78-find-the-duplicate-number)
  * [79 First Missing Positive](#79-first-missing-positive)
  * [80 HIndex](#80-hindex)
  * [81 HIndex II](#81-hindex-ii)
  * [82 Sliding Window Maximum](#82-sliding-window-maximum)
  * [83 Moving Average from Data Stream](#83-moving-average-from-data-stream)
  * [84 Find Median from Data Stream](#84-find-median-from-data-stream)
  * [85 Data Stream as Disjoint Intervals](#85-data-stream-as-disjoint-intervals)
  * [86 Largest Number](#86-largest-number)
  * [87 Sort List](#87-sort-list)
  * [88 Quicksort Array in Java](#88-quicksort-array-in-java)
  * [89 Solution Sort a linked list using insertion sort in Java](#89-solution-sort-a-linked-list-using-insertion-sort-in-java)

## 1 Two Sum

Given an array of integers, find two numbers such that they add up to a specific target
number. The function twoSum should return indices of the two numbers such that they add
up to the target, where index 1 must be less than index 2. Please note that your returned answers (both index 1 and index 2 ) are not zero-based.
For example:

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=0, index2=1

**1.1 Java Solution**

Use HashMap to store the target value.

public class Solution {
public int[] twoSum(int[] numbers, int target) {
HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
int[] result = new int[2];

```
for (int i = 0; i < numbers.length; i++) {
if (map.containsKey(numbers[i])) {
int index = map.get(numbers[i]);
result[0] = index ;
result[1] = i;
break;
} else {
map.put(target - numbers[i], i);
}
}
```
return result;
}
}

Time complexity depends on the put and get operations of HashMap which is nor-
mally O( 1 ).

Time complexity of this solution is O(n).

15 | 677



## 2 Two Sum II Input array is sorted

This problem is similar to Two Sum.
To solve this problem, we can use two points to scan the array from both sides. See
Java solution below:

public int[] twoSum(int[] numbers, int target) {
if (numbers == null || numbers.length == 0)
return null;

```
int i = 0;
int j = numbers.length - 1;
```
```
while (i < j) {
int x = numbers[i] + numbers[j];
if (x < target) {
++i;
} else if (x > target) {
j--;
} else {
return new int[] { i + 1, j + 1 };
}
}
```
return null;
}

17 | 677



## 3 Two Sum III Data structure design

Design and implement a TwoSum class. It should support the following operations:
add and find.

add - Add the number to an internal data structure. find - Find if there exists any
pair of numbers which sum is equal to the value.

For example,

add(1);
add(3);
add(5);
find(4) -> true
find(7) -> false

**3.1 Java Solution**

Since the desired class need add and get operations, HashMap is a good option for
this purpose.

public class TwoSum {
private HashMap<Integer, Integer> elements = new HashMap<Integer,
Integer>();

```
public void add(int number) {
if (elements.containsKey(number)) {
elements.put(number, elements.get(number) + 1);
} else {
elements.put(number, 1);
}
}
```
```java
public boolean find(int value) {
for (Integer i : elements.keySet()) {
int target = value - i;
if (elements.containsKey(target)) {
if (i == target && elements.get(target) < 2) {
continue;
}
return true;
}
}
return false;
}
}
```

20 | 677 Program Creek


## 4 3Sum

Problem:

Given an array S of n integers, are there elements a, b, c in S such that a + b + c = _0_?
Find all unique triplets in the array which gives the sum of zero.
Note: Elements in a triplet (a,b,c) must be in non-descending order. (ie, a≤b≤c)
The solution set must not contain duplicate triplets.

For example, given array S = {-1 0 1 2 -1 -4},

```
A solution set is:
(-1, 0, 1)
(-1, -1, 2)
```
**4.1 Java Solution**

This problem can be solved by using two pointers. Time complexity is O(n 2 ˆ).
To avoid duplicate, we can take advantage of sorted arrays, i.e., move pointers by

> 1 to use same element only once.

public List<List<Integer>> threeSum(int[] nums) {
List<List<Integer>> result = new ArrayList<List<Integer>>();

```
if(nums == null || nums.length<3)
return result;
```
```
Arrays.sort(nums);
```
```
for(int i=0; i<nums.length-2; i++){
if(i==0 || nums[i] > nums[i-1]){
int j=i+1;
int k=nums.length-1;
```
```
while(j<k){
if(nums[i]+nums[j]+nums[k]==0){
List<Integer> l = new ArrayList<Integer>();
l.add(nums[i]);
l.add(nums[j]);
l.add(nums[k]);
result.add(l);
```
```
j++;
```
21 | 677


4 3Sum

```
k--;
```
```
//handle duplicate here
while(j<k && nums[j]==nums[j-1])
j++;
while(j<k && nums[k]==nums[k+1])
k--;
```
```
}else if(nums[i]+nums[j]+nums[k]<0){
j++;
}else{
k--;
}
}
}
```
```
}
```
return result;
}

22 | 677 Program Creek


## 5 4Sum

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c

+ d = target? Find all unique quadruplets in the array which gives the sum of target.
Note: Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a≤
b≤c≤d) The solution set must not contain duplicate quadruplets.

For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

```
A solution set is:
(-1, 0, 0, 1)
(-2, -1, 1, 2)
(-2, 0, 0, 2)
```
**5.1 Java Solution**

A typical k-sum problem. Time is N to the power of (k- 1 ).

public List<List<Integer>> fourSum(int[] nums, int target) {
List<List<Integer>> result = new ArrayList<List<Integer>>();

```
if(nums==null|| nums.length<4)
return result;
```
```
Arrays.sort(nums);
```
```
for(int i=0; i<nums.length-3; i++){
if(i!=0 && nums[i]==nums[i-1])
continue;
for(int j=i+1; j<nums.length-2; j++){
if(j!=i+1 && nums[j]==nums[j-1])
continue;
int k=j+1;
int l=nums.length-1;
while(k<l){
if(nums[i]+nums[j]+nums[k]+nums[l]<target){
k++;
}else if(nums[i]+nums[j]+nums[k]+nums[l]>target){
l--;
}else{
List<Integer> t = new ArrayList<Integer>();
t.add(nums[i]);
t.add(nums[j]);
```
23 | 677


5 4Sum

```
t.add(nums[k]);
t.add(nums[l]);
result.add(t);
```
```
k++;
l--;
```
```
while(k<l &&nums[l]==nums[l+1] ){
l--;
}
```
```
while(k<l &&nums[k]==nums[k-1]){
k++;
}
}
}

}

}
```

return result;
}

24 | 677 Program Creek


## 6 3Sum Closest

Given an array S of n integers, find three integers in S such that the sum is closest to a
given number, target. Return the sum of the three integers. You may assume that each
input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

**6.1 Analysis**

This problem is similar to 2 Sum. This kind of problem can be solved by using a
similar approach, i.e., two pointers from both left and right.

**6.2 Java Solution**

public int threeSumClosest(int[] nums, int target) {
int min = Integer.MAX_VALUE;
int result = 0;

```
Arrays.sort(nums);
```
```
for (int i = 0; i < nums.length; i++) {
int j = i + 1;
int k = nums.length - 1;
while (j < k) {
int sum = nums[i] + nums[j] + nums[k];
int diff = Math.abs(sum - target);
```
```
if(diff == 0) return sum;
```
```
if (diff < min) {
min = diff;
result = sum;
}
if (sum <= target) {
j++;
} else {
k--;
}
}
return result;
}
```


Time Complexity is O(n 2 ˆ).

26 | 677 Program Creek


## 7 Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length

of a subarray of which the sum≥s. If there isn’t one, return 0 instead.
For example, given the array [ 2 , 3 , 1 , 2 , 4 , 3 ] and s = 7 , the subarray [ 4 , 3 ] has the minimal
length of 2 under the problem constraint.

**7.1 Analysis**

We can use 2 points to mark the left and right boundaries of the sliding window. When

the sum is greater than the target, shift the left pointer; when the sum is less than the
target, shift the right pointer.

**7.2 Java Solution 1**

A simple sliding window solution.

```
public int minSubArrayLen(int s, int[] nums) {
if(nums==null || nums.length==1)
return 0;

int result = nums.length;
int start=0;
int sum=0;
int i=0;
boolean exists = false;
while(i<=nums.length){
if(sum>=s){
exists=true; //mark if there exists such a subarray
if(start==i-1){
return 1;
}
result = Math.min(result, i-start);
sum=sum-nums[start];
start++;
}else{
if(i==nums.length)
break;
```


7 Minimum Size Subarray Sum

```
sum = sum+nums[i];
i++;
}
}
```
if(exists)
return result;
else
return 0;
}

**7.3 Deprecated Java Solution**

This solution works but it is less readable.

public int minSubArrayLen(int s, int[] nums) {
if(nums == null || nums.length == 0){
return 0;
}
if(nums.length == 1 && nums[0] < s){
return 0;
}

```
// initialize min length to be the input array length
int result = nums.length;
```
```
int i = 0;
int sum = nums[0];
```
```
for(int j=0; j<nums.length; ){
if(i==j){
if(nums[i]>=s){
return 1; //if single elem is large enough
}else{
j++;
```
```
if(j<nums.length){
sum = sum + nums[j];
}else{
return result;
}
}
}else{
//if sum is large enough, move left cursor
if(sum >= s){
result = Math.min(j-i+1, result);
sum = sum - nums[i];
i++;
```
28 | 677 Program Creek


```
7 Minimum Size Subarray Sum
```
```
//if sum is not large enough, move right cursor
}else{
j++;
```
```
if(j<nums.length){
sum = sum + nums[j];
}else{
if(i==0){
return 0;
}else{
return result;
}
}
}
}
}
```
return result;
}

Program Creek 29 | 677



## 8 Remove Duplicates from Sorted Array

Given a sorted array, remove the duplicates in place such that each element appear
only once and return the new length. Do not allocate extra space for another array,
you must do this in place with constant memory.

For example, given input array A = [ 1 , 1 , 2 ], your function should return length = 2 ,
and A is now [ 1 , 2 ].

**8.1 Thoughts**

The problem is pretty straightforward. It returns the length of array with unique

elements, but the original array need to be changed also. This problem should be
reviewed with Remove Duplicates from Sorted Array II.

**8.2 Solution 1**

// Manipulate original array
public static int removeDuplicatesNaive(int[] A) {
if (A.length < 2)
return A.length;

```
int j = 0;
int i = 1;
```
```
while (i < A.length) {
if (A[i] == A[j]) {
i++;
} else {
j++;
A[j] = A[i];
i++;
}
}
```
return j + 1;
}

This method returns the number of unique elements, but does not change the orig-

inal array correctly. For example, if the input array is 1 , 2 , 2 , 3 , 3 , the array will be
changed to 1 , 2 , 3 , 3 , 3. The correct result should be 1 , 2 , 3. Because array’s size can

31 | 677


8 Remove Duplicates from Sorted Array

not be changed once created, there is no way we can return the original array with
correct results.

**8.3 Solution 2**

// Create an array with all unique elements
public static int[] removeDuplicates(int[] A) {
if (A.length < 2)
return A;

```
int j = 0;
int i = 1;
```
```
while (i < A.length) {
if (A[i] == A[j]) {
i++;
} else {
j++;
A[j] = A[i];
i++;
}
}
```
```
int[] B = Arrays.copyOf(A, j + 1);
```
return B;
}

public static void main(String[] args) {
int[] arr = { 1, 2, 2, 3, 3 };
arr = removeDuplicates(arr);
System.out.println(arr.length);
}

In this method, a new array is created and returned.

**8.4 Solution 3**

If we only want to count the number of unique elements, the following method is
good enough.

```
// Count the number of unique elements
public static int countUnique(int[] A) {
int count = 0;
for (int i = 0; i < A.length - 1; i++) {
if (A[i] == A[i + 1]) {
count++;
}

}

return (A.length - count);
}

public static void main(String[] args) {
int[] arr = { 1, 2, 2, 3, 3 };
int size = countUnique(arr);
System.out.println(size);
}

```



## 9 Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates": What if duplicates are allowed at most twice?

For example, given sorted array A = [ 1 , 1 , 1 , 2 , 2 , 3 ], your function should return length
= 5 , and A is now [ 1 , 1 , 2 , 2 , 3 ].
So this problem also requires in-place array manipulation.

**9.1 Java Solution 1**

We can not change the given array’s size, so we only change the first k elements of the array which has duplicates removed.

```
public class Solution {
public int removeDuplicates(int[] A) {
if (A == null || A.length == 0)
return 0;

int pre = A[0];
boolean flag = false;
int count = 0;
// index for updating
int o = 1;
for (int i = 1; i < A.length; i++) {
int curr = A[i];
if (curr == pre) {
if (!flag) {
flag = true;
A[o++] = curr;
continue;
} else {
count++;
}
} else {
pre = curr;
A[o++] = curr;
flag = false;

return A.length - count;
}
}
```

**9.2 Java Solution 2**

public class Solution {
public int removeDuplicates(int[] A) {
if (A.length <= 2)
return A.length;

```
int prev = 1; // point to previous
int curr = 2; // point to current
```
```
while (curr < A.length) {
if (A[curr] == A[prev] && A[curr] == A[prev - 1]) {
curr++;
} else {
prev++;
A[prev] = A[curr];
curr++;
}
}
```
return prev + 1;
}
}

36 | 677 Program Creek


## 10 Remove Element

Given an array and a value, remove all instances of that value in place and return the
new length. (Note: The order of elements can be changed. It doesn’t matter what you
leave beyond the new length.)

**10.1 Java Solution**

This problem can be solve by using two indices.

public int removeElement(int[] A, int elem) {
int i=0;
int j=0;

```
while(j < A.length){
if(A[j] != elem){
A[i] = A[j];
i++;
}
```
```
j++;
}
```
return i;
}

37 | 677



## 11 Move Zeroes

Given an array nums, write a function to move all 0 ’s to the end of it while maintaining

the relative order of the non-zero elements.
For example, given nums = [ 0 , 1 , 0 , 3 , 12 ], after calling your function, nums should
be [ 1 , 3 , 12 , 0 , 0 ].

**11.1 Java Solution 1**

public void moveZeroes(int[] nums) {
int m=-1;

for(int i=0; i<nums.length; i++){
if(nums[i]==0){
if(m==-1 || nums[m]!=0){
m=i;
}
}else{
if(m!=-1){
int temp = nums[i];
nums[i]=nums[m];
nums[m]=temp;
m++;
}
}
}
}

**11.2 Java Solution 2 - Simple**

Actually, we can use the similar code that is used to solve Remove Duplicates from
Sorted Array I, II, Remove Element. We can use almost identical code to solve those
problems!

public void moveZeroes(int[] nums) {
int i=0;
int j=0;

```
while(j<nums.length){
if(nums[j]==0){
```
39 | 677


11 Move Zeroes

```
j++;
}else{
nums[i]=nums[j];
i++;
j++;
}
}
```
while(i<nums.length){
nums[i]=0;
i++;
}
}

40 | 677 Program Creek


## 12 Container With Most Water

**12.1 Problem**

Given n non-negative integers a 1 , a 2 , ..., an, where each represents a point at coordi-
nate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai)

and (i, 0 ). Find two lines, which together with x-axis forms a container, such that the
container contains the most water.

**12.2 Analysis**

Initially we can assume the result is 0. Then we scan from both sides. If leftHeight

<rightHeight, move right and find a value that is greater than leftHeight. Similarily,
if leftHeight >rightHeight, move left and find a value that is greater than rightHeight.
Additionally, keep tracking the max value.

**12.3 Java Solution**

public int maxArea(int[] height) {
if (height == null || height.length < 2) {
return 0;
}

```
int max = 0;
int left = 0;
int right = height.length - 1;
```
```
while (left < right) {
max = Math.max(max, (right - left) *Math.min(height[left],
height[right]));
```
41 | 677


12 Container With Most Water

```
if (height[left] < height[right])
left++;
else
right--;
}
```
return max;
}

42 | 677 Program Creek


## 13 Candy

There are N children standing in a line. Each child is assigned a rating value. You are
giving candies to these children subjected to the following requirements:

1. Each child must have at least one candy. 2. Children with a higher rating get
more candies than their neighbors.

What is the minimum candies you must give?

**13.1 Analysis**

This problem can be solved in O(n) time.

We can always assign a neighbor with 1 more if the neighbor has higher a rating
value. However, to get the minimum total number, we should always start adding 1 s
in the ascending order. We can solve this problem by scanning the array from both
sides. First, scan the array from left to right, and assign values for all the ascending

pairs. Then scan from right to left and assign values to descending pairs.
This problem is similar to Trapping Rain Water.

**13.2 Java Solution**

public int candy(int[] ratings) {
if (ratings == null || ratings.length == 0) {
return 0;
}

```
int[] candies = new int[ratings.length];
candies[0] = 1;
```
```
//from let to right
for (int i = 1; i < ratings.length; i++) {
if (ratings[i] > ratings[i - 1]) {
candies[i] = candies[i - 1] + 1;
} else {
// if not ascending, assign 1
candies[i] = 1;
}
}
```
```
int result = candies[ratings.length - 1];
```
43 | 677


13 Candy

```
//from right to left
for (int i = ratings.length - 2; i >= 0; i--) {
int cur = 1;
if (ratings[i] > ratings[i + 1]) {
cur = candies[i + 1] + 1;
}
```
```
result += Math.max(cur, candies[i]);
candies[i] = cur;
}
```
return result;
}

44 | 677 Program Creek


## 14 Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each

bar is 1 , compute how much water it is able to trap after raining.
For example, given [ 0 , 1 , 0 , 2 , 1 , 0 , 1 , 3 , 2 , 1 , 2 , 1 ], return 6.

**14.1 Analysis**

This problem is similar to Candy. It can be solve by scanning from both sides and

then get the total.

**14.2 Java Solution**

public int trap(int[] height) {
int result = 0;

```
if(height==null || height.length<=2)
return result;
```
```
int left[] = new int[height.length];
int right[]= new int[height.length];
```
```
//scan from left to right
int max = height[0];
left[0] = height[0];
for(int i=1; i<height.length; i++){
if(height[i]<max){
left[i]=max;
}else{
left[i]=height[i];
max = height[i];
}
}
```
```
//scan from right to left
max = height[height.length-1];
right[height.length-1]=height[height.length-1];
for(int i=height.length-2; i>=0; i--){
if(height[i]<max){
right[i]=max;
}else{
```
45 | 677


14 Trapping Rain Water

```
right[i]=height[i];
max = height[i];
}
}
```
```
//calculate totoal
for(int i=0; i<height.length; i++){
result+= Math.min(left[i],right[i])-height[i];
}
```
return result;
}

46 | 677 Program Creek


## 15 Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges for
consecutive numbers.

For example, given [ 0 , 1 , 2 , 4 , 5 , 7 ], return [" 0 -> 2 "," 4 -> 5 "," 7 "].

**15.1 Analysis**

**15.2 Java Solution**

public List<String> summaryRanges(int[] nums) {
List<String> result = new ArrayList<String>();

```
if(nums == null || nums.length==0)
return result;
```
```
if(nums.length==1){
result.add(nums[0]+"");
}
```
```
int pre = nums[0]; // previous element
int first = pre; // first element of each range
```
```
for(int i=1; i<nums.length; i++){
if(nums[i]==pre+1){
if(i==nums.length-1){
result.add(first+"->"+nums[i]);
}
}else{
if(first == pre){
result.add(first+"");
}else{
result.add(first + "->"+pre);
}
```
```
if(i==nums.length-1){
result.add(nums[i]+"");
}
```
```
first = nums[i];
}
```
47 | 677


15 Summary Ranges

```
pre = nums[i];
}
```
return result;
}

48 | 677 Program Creek


## 16 One Edit Distance

Given two strings S and T, determine if they are both one edit distance apart.

**16.1 Java Solution**

public boolean isOneEditDistance(String s, String t) {
if(s==null || t==null)
return false;

```
int m = s.length();
int n = t.length();
```
```
if(Math.abs(m-n)>1){
return false;
}
```
```
int i=0;
int j=0;
int count=0;
```
```
while(i<m&&j<n){
if(s.charAt(i)==t.charAt(j)){
i++;
j++;
}else{
count++;
if(count>1)
return false;
```
```
if(m>n){
i++;
}else if(m<n){
j++;
}else{
i++;
j++;
}
}
}
```
```
if(i<m||j<n){
count++;
```

```
if(count==1)
return true;
return false;
}
```


## 17 Merge Sorted Array

Given two sorted integer arrays A and B, merge B into A as one sorted array.
Note: You may assume that A has enough space to hold additional elements from
B. The number of elements initialized in A and B are m and n respectively.

**17.1 Analysis**

The key to solve this problem is moving element of A and B backwards. If B has some
elements left after A is done, also need to handle that case.

The takeaway message from this problem is that the loop condition. This kind of
condition is also used for merging two sorted linked list.

**17.2 Java Solution 1**

public class Solution {
public void merge(int A[], int m, int B[], int n) {

```
while(m > 0 && n > 0){
if(A[m-1] > B[n-1]){
A[m+n-1] = A[m-1];
m--;
}else{
A[m+n-1] = B[n-1];
n--;
}
}
```
while(n > 0){
A[m+n-1] = B[n-1];
n--;
}
}
}

**17.3 Java Solution 2**

The loop condition also can use m+n like the following.

51 | 677


17 Merge Sorted Array

public void merge(int A[], int m, int B[], int n) {
int i = m - 1;
int j = n - 1;
int k = m + n - 1;

while (k >= 0) {
if (j < 0 || (i >= 0 && A[i] > B[j]))
A[k--] = A[i--];
else
A[k--] = B[j--];
}
}

52 | 677 Program Creek


## 18 Shortest Word Distance

Given a list of words and two words word 1 and word 2 , return the shortest distance
between these two words in the list.
For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word 1 = “coding”, word 2 = “practice”, return 3. Given word 1 = "makes",

word 2 = "coding", return 1.

**18.1 Java Solution**

public int shortestDistance(String[] words, String word1, String word2) {
int m=-1;
int n=-1;

```
int min = Integer.MAX_VALUE;
```
```
for(int i=0; i<words.length; i++){
String s = words[i];
if(word1.equals(s)){
m = i;
if(n!=-1)
min = Math.min(min, m-n);
}else if(word2.equals(s)){
n = i;
if(m!=-1)
min = Math.min(min, n-m);
}
}
```
return min;
}

53 | 677



## 19 Shortest Word Distance II

This is a follow up of Shortest Word Distance. The only difference is now you are
given the list of words and your method will be called repeatedly many times with
different parameters. How would you optimize it?
Design a class which receives a list of words in the constructor, and implements

a method that takes two words word 1 and word 2 and return the shortest distance
between these two words in the list.
For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word 1 = “coding”, word 2 = “practice”, return 3. Given word 1 = "makes",

word 2 = "coding", return 1.

**19.1 Java Solution**

public class WordDistance {
HashMap<String, ArrayList<Integer>> map;
public WordDistance(String[] words) {
map = new HashMap<String, ArrayList<Integer>>();
for(int i=0; i<words.length; i++){
if(map.containsKey(words[i])){
map.get(words[i]).add(i);
}else{
ArrayList<Integer> list = new ArrayList<Integer>();
list.add(i);
map.put(words[i], list);
}
}
}

```
public int shortest(String word1, String word2) {
```
```
ArrayList<Integer> l1 = map.get(word1);
ArrayList<Integer> l2 = map.get(word2);
```
```
int result = Integer.MAX_VALUE;
for(int i1: l1){
for(int i2: l2){
result = Math.min(result, Math.abs(i1-i2));
}
}
return result;
}
```

The time complexity for shortest method is O(N 2 ˆ), because there are two for loops.
This should be improved. The following is the solution:

public int shortest(String word1, String word2) {

```
ArrayList<Integer> l1 = map.get(word1);
ArrayList<Integer> l2 = map.get(word2);
```
```
int result = Integer.MAX_VALUE;
int i=0;
int j=0;
while(i<l1.size() && j<l2.size()){
result = Math.min(result, Math.abs(l1.get(i)-l2.get(j)));
if(l1.get(i)<l2.get(j)){
i++;
}else{
j++;
}
}
```
return result;
}

56 | 677 Program Creek


## 20 Shortest Word Distance III

This is a follow-up problem of Shortest Word Distance. The only difference is now
word 1 could be the same as word 2.

Given a list of words and two words word 1 and word 2 , return the shortest distance
between these two words in the list.

word 1 and word 2 may be the same and they represent two individual words in the
list.

For example, Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word 1 = “makes”, word 2 = “coding”, return 1. Given word 1 = "makes",
word 2 = "makes", return 3.

**20.1 Java Solution**

In this problem, word 1 and word 2 can be the same. The two variables used to track
indices should take turns to update.

public int shortestWordDistance(String[] words, String word1, String word2) {
if(words==null || words.length<1 || word1==null || word2==null)
return 0;

```
int m=-1;
int n=-1;
```
```
int min = Integer.MAX_VALUE;
int turn=0;
if(word1.equals(word2))
turn = 1;
```
```
for(int i=0; i<words.length; i++){
String s = words[i];
if(word1.equals(s) && (turn ==1 || turn==0)){
m = i;
if(turn==1) turn=2;
if(n!=-1)
min = Math.min(min, m-n);
}else if(word2.equals(s) && (turn==2 || turn==0)){
n = i;
if(turn==2) turn =1;
if(m!=-1)
min = Math.min(min, n-m);
}

}

return min;
}

```


## 21 Intersection of Two Arrays Contents

Given two arrays, write a function to compute their intersection.

**21.1 Java Solution 1 - HashSet**

Time = O(n). Space = O(n).

public int[] intersection(int[] nums1, int[] nums2) {
HashSet<Integer> set1 = new HashSet<Integer>();
for(int i: nums1){
set1.add(i);
}

```
HashSet<Integer> set2 = new HashSet<Integer>();
for(int i: nums2){
if(set1.contains(i)){
set2.add(i);
}
}
```
```
int[] result = new int[set2.size()];
int i=0;
for(int n: set2){
result[i++] = n;
}
```
return result;
}

**21.2 Java Solution 2 - Binary Search**

Time = O(nlog(n)). Space = O(n).

public int[] intersection(int[] nums1, int[] nums2) {
Arrays.sort(nums1);
Arrays.sort(nums2);

```
ArrayList<Integer> list = new ArrayList<Integer>();
for(int i=0; i<nums1.length; i++){
if(i==0 || (i>0 && nums1[i]!=nums1[i-1])){
if(Arrays.binarySearch(nums2, nums1[i])>-1){
```
59 | 677


21 Intersection of Two Arrays

```
list.add(nums1[i]);
}
}
}
```
```
int[] result = new int[list.size()];
int k=0;
for(int i: list){
result[k++] = i;
}
```
return result;
}

**21.3 Any improvement?**

60 | 677 Program Creek


## 22 Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.

Example: Given nums 1 = [ 1 , 2 , 2 , 1 ], nums 2 = [ 2 , 2 ], return [ 2 , 2 ].

**22.1 Java Solution**

public int[] intersect(int[] nums1, int[] nums2) {
HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
for(int i: nums1){
if(map.containsKey(i)){
map.put(i, map.get(i)+1);
}else{
map.put(i, 1);
}
}

```
ArrayList<Integer> list = new ArrayList<Integer>();
for(int i: nums2){
if(map.containsKey(i)){
if(map.get(i)>1){
map.put(i, map.get(i)-1);
}else{
map.remove(i);
}
list.add(i);
}
}
```
```
int[] result = new int[list.size()];
int i =0;
while(i<list.size()){
result[i]=list.get(i);
i++;
}
```
return result;
}

61 | 677


22 Intersection of Two Arrays II

**22.2 Java Solution 2**

If the arrays are sorted, then we can use two points.

public int[] intersect(int[] nums1, int[] nums2) {
Arrays.sort(nums1);
Arrays.sort(nums2);
ArrayList<Integer> list = new ArrayList<Integer>();
int p1=0, p2=0;
while(p1<nums1.length && p2<nums2.length){
if(nums1[p1]<nums2[p2]){
p1++;
}else if(nums1[p1]>nums2[p2]){
p2++;
}else{
list.add(nums1[p1]);
p1++;
p2++;

```
}
}
```
int[] result = new int[list.size()];
int i=0;
while(i<list.size()){
result[i]=list.get(i);
i++;
}
return result;
}

62 | 677 Program Creek


## 23 Median of Two Sorted Arrays

```
There are two sorted arrays A and B of size m and n respectively. Find the median of the
two sorted arrays. The overall run time complexity should be O(log (m+n)).
```
**23.1 Java Solution**

If we see log(n), we should think about using binary something.
This problem can be converted to the problem of finding kth element, k is (A’s
length + B’ Length)/ 2.

If any of the two arrays is empty, then the kth element is the non-empty array’s kth
element. If k == 0 , the kth element is the first element of A or B.
For normal cases(all other cases), we need to move the pointer at the pace of half of
an array length to get log(n) time.

public static double findMedianSortedArrays(int A[], int B[]) {
int m = A.length;
int n = B.length;

if ((m + n) % 2 != 0) // odd
return (double) findKth(A, B, (m + n) / 2, 0, m - 1, 0, n - 1);
else { // even
return (findKth(A, B, (m + n) / 2, 0, m - 1, 0, n - 1)
+ findKth(A, B, (m + n) / 2 - 1, 0, m - 1, 0, n - 1))*0.5;
}
}

public static int findKth(int A[], int B[], int k,
int aStart, int aEnd, int bStart, int bEnd) {

```
int aLen = aEnd - aStart + 1;
int bLen = bEnd - bStart + 1;
```
```
// Handle special cases
if (aLen == 0)
return B[bStart + k];
if (bLen == 0)
return A[aStart + k];
if (k == 0)
return A[aStart] < B[bStart]? A[aStart] : B[bStart];
```
```
int aMid = aLen *k / (aLen + bLen); // a’s middle count
int bMid = k - aMid - 1; // b’s middle count
```
63 | 677


23 Median of Two Sorted Arrays

```
// make aMid and bMid to be array index
aMid = aMid + aStart;
bMid = bMid + bStart;
```
```
if (A[aMid] > B[bMid]) {
k = k - (bMid - bStart + 1);
aEnd = aMid;
bStart = bMid + 1;
} else {
k = k - (aMid - aStart + 1);
bEnd = bMid;
aStart = aMid + 1;
}
```
return findKth(A, B, k, aStart, aEnd, bStart, bEnd);
}

64 | 677 Program Creek


## 24 Search Insert Position

Given a sorted array and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order. You may assume no
duplicates in the array.

Here are few examples.

[1,3,5,6], 5 -> 2
[1,3,5,6], 2 -> 1
[1,3,5,6], 7 -> 4
[1,3,5,6], 0 -> 0

**24.1 Solution 1**

Naively, we can just iterate the array and compare target with ith and (i+ 1 )th element.
Time complexity is O(n)

public class Solution {
public int searchInsert(int[] A, int target) {

```
if(A==null) return 0;
```
```
if(target <= A[0]) return 0;
```
```
for(int i=0; i<A.length-1; i++){
if(target > A[i] && target <= A[i+1]){
return i+1;
}
}
```
return A.length;
}
}

**24.2 Solution 2**

This also looks like a binary search problem. We should try to make the complexity to

be O(log(n)).

public class Solution {
public int searchInsert(int[] A, int target) {

65 | 677


24 Search Insert Position

```
if(A==null||A.length==0)
return 0;
```
```
return searchInsert(A,target,0,A.length-1);
}
```
```
public int searchInsert(int[] A, int target, int start, int end){
int mid=(start+end)/2;
```
if(target==A[mid])
return mid;
else if(target<A[mid])
return start<mid?searchInsert(A,target,start,mid-1):start;
else
return end>mid?searchInsert(A,target,mid+1,end):(end+1);
}
}

**24.3 Java Solution 3**

public int searchInsert(int[] nums, int target) {
int i=0;
int j=nums.length-1;

```
while(i<=j){
int mid = (i+j)/2;
```
```
if(target > nums[mid]){
i=mid+1;
}else if(target < nums[mid]){
j=mid-1;
}else{
return mid;
}
}
```
return i;
}

66 | 677 Program Creek


## 25 Find Minimum in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e.,0 1

2 4 5 6 7might become4 5 6 7 0 1 2).
Find the minimum element.You may assume no duplicate exists in the array.

**25.1 Analysis**

This problem is a binary search and the key is breaking the array to two parts, so that
we only need to work on half of the array each time.

If we pick the middle element, we can compare the middle element with the leftmost
(or rightmost) element. If the middle element is less than leftmost, the left half should
be selected; if the middle element is greater than the leftmost (or rightmost), the right
half should be selected. Using recursion or iteration, this problem can be solved in
time log(n).

In addition, in any rotated sorted array, the rightmost element should be less than
the left-most element, otherwise, the sorted array is not rotated and we can simply
pick the leftmost element as the minimum.

**25.2 Java Solution 1 - Recursion**

Define a helper function, otherwise, we will need to use Arrays.copyOfRange() func-
tion, which may be expensive for large arrays.

public int findMin(int[] num) {
return findMin(num, 0, num.length - 1);
}

public int findMin(int[] num, int left, int right) {
if (left == right)
return num[left];
if ((right - left) == 1)
return Math.min(num[left], num[right]);

```
int middle = left + (right - left) / 2;
```
```
// not rotated
if (num[left] < num[right]) {
return num[left];
```
67 | 677


25 Find Minimum in Rotated Sorted Array

```
// go right side
} else if (num[middle] > num[left]) {
return findMin(num, middle, right);
```
// go left side
} else {
return findMin(num, left, middle);
}
}

**25.3 Java Solution 2 - Iteration**

public int findMin(int[] nums) {
if(nums==null || nums.length==0)
return -1;

```
if(nums.length==1)
return nums[0];
```
```
int left=0;
int right=nums.length-1;
```
```
//not rotated
if(nums[left]<nums[right])
return nums[left];
```
```
while(left <= right){
if(right-left==1){
return nums[right];
}
```
```
int m = left + (right-left)/2;
```
```
if(nums[m] > nums[right])
left = m;
else
right = m;
}
```
return nums[left];
}

Or

/*
To understand the boundaries, use the following 3 examples:
[2,1], [2,3,1], [3,1,2]

68 | 677 Program Creek


```
25 Find Minimum in Rotated Sorted Array
```
### */

public int findMin(int[] nums) {
if(nums==null || nums.length==0)
return -1;

```
int i=0;
int j=nums.length-1;
```
```
while(i<=j){
if(nums[i]<=nums[j])
return nums[i];
```
```
int m=(i+j)/2;
```
```
if(nums[m]>=nums[i]){
i=m+1;
}else{
j=m;
}
}
```
return -1;
}

Program Creek 69 | 677



## 26 Find Minimum in Rotated Sorted Array II

Follow up for "Find Minimum in Rotated Sorted Array": What if duplicates are al-
lowed?

Would this affect the run-time complexity? How and why?

**26.1 Java Solution 1 - Recursion**

This is a follow-up problem of finding minimum element in rotated sorted array with-
out duplicate elements. We only need to add one more condition, which checks if
the left-most element and the right-most element are equal. If they are we can simply

drop one of them. In my solution below, I drop the left element whenever the left-most
equals to the right-most.

public int findMin(int[] num) {
return findMin(num, 0, num.length-1);
}

public int findMin(int[] num, int left, int right){
if(right==left){
return num[left];
}
if(right == left +1){
return Math.min(num[left], num[right]);
}
// 3 3 1 3 3 3

```
int middle = (right-left)/2 + left;
// already sorted
if(num[right] > num[left]){
return num[left];
//right shift one
}else if(num[right] == num[left]){
return findMin(num, left+1, right);
//go right
}else if(num[middle] >= num[left]){
return findMin(num, middle, right);
//go left
}else{
return findMin(num, left, middle);
}
}
```

**26.2 Java Solution 2 - Iteration**

public int findMin(int[] nums) {
int i=0;
int j=nums.length-1;

```
while(i<=j){
```
```
//handle cases like [3, 1, 3]
while(nums[i]==nums[j] && i!=j){
i++;
}
```
```
if(nums[i]<=nums[j]){
return nums[i];
}
```
```
int m=(i+j)/2;
if(nums[m]>=nums[i]){
i=m+1;
}else{
j=m;
}
}
```
return -1;
}

72 | 677 Program Creek


## 27 Search for a Range

Given a sorted array of integers, find the starting and ending position of a given target

value. Your algorithm’s runtime complexity must be in the order of O(log n). If the
target is not found in the array, return [- 1 , - 1 ]. For example, given [ 5 , 7 , 7 , 8 , 8 , 10 ] and
target value 8 , return [ 3 , 4 ].

**27.1 Analysis**

Based on the requirement of O(log n), this is a binary search problem apparently.

**27.2 Java Solution**

public int[] searchRange(int[] nums, int target) {
if(nums == null || nums.length == 0){
return null;
}

```
int[] arr= new int[2];
arr[0]=-1;
arr[1]=-1;
```
```
binarySearch(nums, 0, nums.length-1, target, arr);
```
return arr;
}

public void binarySearch(int[] nums, int left, int right, int target, int[]
arr){
if(right<left)
return;

```
if(nums[left]==nums[right] && nums[left]==target){
arr[0]=left;
arr[1]=right;
return;
}
```
```
int mid = left+(right-left)/2;
```
73 | 677


27 Search for a Range

```
if(nums[mid]<target){
binarySearch(nums, mid+1, right, target, arr);
}else if(nums[mid]>target){
binarySearch(nums, left, mid-1, target, arr);
}else{
arr[0]=mid;
arr[1]=mid;
```
```
//handle duplicates - left
int t1 = mid;
while(t1 >left && nums[t1]==nums[t1-1]){
t1--;
arr[0]=t1;
}
```
//handle duplicates - right
int t2 = mid;
while(t2 < right&& nums[t2]==nums[t2+1]){
t2++;
arr[1]=t2;
}
return;
}
}

74 | 677 Program Creek


## 28 Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I’ll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results (- 1 , 1 , or
0 ):

- 1 : My number is lower 1 : My number is higher 0 : Congrats! You got it! Example:
n = 10 , I pick 6.
Return 6.

**28.1 Java Solution**

This is a typical binary search problem. Here is a Java solution.

public int guessNumber(int n) {
int low=1;
int high=n;

```
while(low <= high){
int mid = low+((high-low)/2);
int result = guess(mid);
if(result==0){
return mid;
}else if(result==1){
low = mid+1;
}else{
high=mid-1;
}
}
```
return -1;
}

**28.2 What we learn from this problem?**

low+(high-low)/ 2 yields the same value with (low+high)/ 2. However, the first expres-
sion is less expensive. In addition, the following expression can be used:

low+((high-low)>>1)
(low+high)>>>1

75 | 677


28 Guess Number Higher or Lower

Under the assumption that high and low are both non-negative, we know for sure
that the upper-most bit (the sign-bit) is zero.

So both high and low are in fact 31 -bit integers.

high = 0100 0000 0000 0000 0000 0000 0000 0000 = 1073741824
low = 0100 0000 0000 0000 0000 0000 0000 0000 = 1073741824

When you add them together they may "spill" over into the top-bit.

high + low = 1000 0000 0000 0000 0000 0000 0000 0000
= 2147483648 as unsigned 32-bit integer
= -2147483648 as signed 32-bit integer

(high + low) / 2 = 1100 0000 0000 0000 0000 0000 0000 0000 = -1073741824
(high + low) >>> 1 = 0100 0000 0000 0000 0000 0000 0000 0000 = 1073741824

76 | 677 Program Creek


## 29 First Bad Version

You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check. Since each
version is developed based on the previous version, all the versions after a bad version
are also bad.

Suppose you have n versions [ 1 , 2 , ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version
is bad. Implement a function to find the first bad version. You should minimize the
number of calls to the API.

**29.1 Java Solution 1 - Recurisve**

public int firstBadVersion(int n) {
return helper(1, n);
}

public int helper(int i, int j){
int m = i + (j-i)/2;

```
if(i>=j)
return i;
```
if(isBadVersion(m)){
return helper(i, m);
}else{
return helper(m+1, j); //not bad, left --> m+1
}
}

**29.2 Java Solution 2 - Iterative**

public int firstBadVersion(int n) {
int i = 1, j = n;
while (i < j) {
int m = i + (j-i) / 2;
if (isBadVersion(m)) {
j = m;

77 | 677


29 First Bad Version

```
} else {
i = m+1;
}
}
```
```
if (isBadVersion(i)) {
return i;
}
```
return j;
}

78 | 677 Program Creek


## 30 Search in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e.,0 1
2 4 5 6 7might become4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, other-
wise return - 1. You may assume no duplicate exists in the array.

**30.1 Java Solution 1- Recusive**

public int search(int[] nums, int target) {
return binarySearch(nums, 0, nums.length-1, target);
}

public int binarySearch(int[] nums, int left, int right, int target){
if(left>right)
return -1;

```
int mid = left + (right-left)/2;
```
```
if(target == nums[mid])
return mid;
```
if(nums[left] <= nums[mid]){
if(nums[left]<=target && target<nums[mid]){
return binarySearch(nums,left, mid-1, target);
}else{
return binarySearch(nums, mid+1, right, target);
}
}else {
if(nums[mid]<target&& target<=nums[right]){
return binarySearch(nums,mid+1, right, target);
}else{
return binarySearch(nums, left, mid-1, target);
}
}
}

**30.2 Java Solution 2 - Iterative**

public int search(int[] nums, int target) {

79 | 677


30 Search in Rotated Sorted Array

```
int left = 0;
int right= nums.length-1;
```
```
while(left<=right){
int mid = left + (right-left)/2;
if(target==nums[mid])
return mid;
```
```
if(nums[left]<=nums[mid]){
if(nums[left]<=target&& target<nums[mid]){
right=mid-1;
}else{
left=mid+1;
}
}else{
if(nums[mid]<target&& target<=nums[right]){
left=mid+1;
}else{
right=mid-1;
}
}
}
```
return -1;
}

80 | 677 Program Creek


## 31 Search in Rotated Sorted Array II

Follow up for "Search in Rotated Sorted Array": what if duplicates are allowed? Write
a function to determine if a given target is in the array.

**31.1 Java Solution**

public boolean search(int[] nums, int target) {
int left=0;
int right=nums.length-1;

```
while(left<=right){
int mid = (left+right)/2;
if(nums[mid]==target)
return true;
```
```
if(nums[left]<nums[mid]){
if(nums[left]<=target&& target<nums[mid]){
right=mid-1;
}else{
left=mid+1;
}
}else if(nums[left]>nums[mid]){
if(nums[mid]<target&&target<=nums[right]){
left=mid+1;
}else{
right=mid-1;
}
}else{
left++;
}
}
```
return false;
}

81 | 677



## 32 Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid op-

erators are +, -, *, /. Each operand may be an integer or another expression. For
example:

["2", "1", "+", "3", "*"] -> ((2 + 1)* 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

**32.1 Naive Approach**

This problem can be solved by using a stack. We can loop through each element in the

given array. When it is a number, push it to the stack. When it is an operator, pop two
numbers from the stack, do the calculation, and push back the result.

The following is the code. However, this code contains compilation errors in leet-
code. Why?

public class Test {

```
public static void main(String[] args) throws IOException {
String[] tokens = new String[] { "2", "1", "+", "3", "*" };
System.out.println(evalRPN(tokens));
}
```
83 | 677


32 Evaluate Reverse Polish Notation

```
public static int evalRPN(String[] tokens) {
int returnValue = 0;
String operators = "+-*/";
```
```
Stack<String> stack = new Stack<String>();
```
```
for (String t : tokens) {
if (!operators.contains(t)) { //push to stack if it is a number
stack.push(t);
} else {//pop numbers from stack if it is an operator
int a = Integer.valueOf(stack.pop());
int b = Integer.valueOf(stack.pop());
switch (t) {
case "+":
stack.push(String.valueOf(a + b));
break;
case "-":
stack.push(String.valueOf(b - a));
break;
case "*":
stack.push(String.valueOf(a* b));
break;
case "/":
stack.push(String.valueOf(b / a));
break;
}
}
}
```
```
returnValue = Integer.valueOf(stack.pop());
```
return returnValue;
}
}

The problem is that switch string statement is only available from JDK 1. 7. Leetcode
apparently use a JDK version below 1. 7.

**32.2 Accepted Solution**

If you want to use switch statement, you can convert the above by using the following
code which use the index of a string "+-*/".

public class Solution {
public int evalRPN(String[] tokens) {

```
int returnValue = 0;
```
84 | 677 Program Creek


```
32 Evaluate Reverse Polish Notation
```
```
String operators = "+-*/";
```
```
Stack<String> stack = new Stack<String>();
```
```
for(String t : tokens){
if(!operators.contains(t)){
stack.push(t);
}else{
int a = Integer.valueOf(stack.pop());
int b = Integer.valueOf(stack.pop());
int index = operators.indexOf(t);
switch(index){
case 0:
stack.push(String.valueOf(a+b));
break;
case 1:
stack.push(String.valueOf(b-a));
break;
case 2:
stack.push(String.valueOf(a*b));
break;
case 3:
stack.push(String.valueOf(b/a));
break;
}
}
}
```
```
returnValue = Integer.valueOf(stack.pop());
```
```
return returnValue;
```
}
}

Program Creek 85 | 677



## 33 Valid Parentheses

```
Given a string containing just the characters ’(’, ’)’, ’’, ’’, ’[’ and ’]’, determine if the
input string is valid. The brackets must close in the correct order, "()" and "()[]" are all
valid but "(]" and "([)]" are not.
```
**33.1 Analysis**

A typical problem which can be solved by using a stack data structure.

**33.2 Java Solution**

public static boolean isValid(String s) {
HashMap<Character, Character> map = new HashMap<Character, Character>();
map.put(’(’, ’)’);
map.put(’[’, ’]’);
map.put(’{’, ’}’);

```
Stack<Character> stack = new Stack<Character>();
```
```
for (int i = 0; i < s.length(); i++) {
char curr = s.charAt(i);
```
```
if (map.keySet().contains(curr)) {
stack.push(curr);
} else if (map.values().contains(curr)) {
if (!stack.empty() && map.get(stack.peek()) == curr) {
stack.pop();
} else {
return false;
}
}
}
```
return stack.empty();
}

87 | 677



## 34 Longest Valid Parentheses

Given a string containing just the characters ’(’ and ’)’, find the length of the longest
valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2. An-
other example is ")()())", where the longest valid parentheses substring is "()()", which
has length = 4.

**34.1 Analysis**

This problem is similar with Valid Parentheses, which can be solved by using a stack.

**34.2 Java Solution**

public static int longestValidParentheses(String s) {
Stack<int[]> stack = new Stack<int[]>();
int result = 0;

```
for(int i=0; i<=s.length()-1; i++){
char c = s.charAt(i);
if(c==’(’){
int[] a = {i,0};
stack.push(a);
}else{
if(stack.empty()||stack.peek()[1]==1){
int[] a = {i,1};
stack.push(a);
}else{
stack.pop();
int currentLen=0;
if(stack.empty()){
currentLen = i+1;
}else{
currentLen = i-stack.peek()[0];
}
result = Math.max(result, currentLen);
}
}
}
return result;
}
```

90 | 677 Program Creek


## 35 Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric charac-
ters and ignoring cases.
For example, "Red rum, sir, is murder" is a palindrome, while "Programcreek is
awesome" is not.

Note: Have you consider that the string might be empty? This is a good question to
ask during an interview.
For the purpose of this problem, we define empty string as valid palindrome.

**35.1 Thoughts**

From start and end loop though the string, i.e., char array. If it is not alpha or num-
ber, increase or decrease pointers. Compare the alpha and numeric characters. The
solution below is pretty straightforward.

**35.2 Java Solution 1 - Naive**

public class Solution {

```
public boolean isPalindrome(String s) {
```
```
if(s == null) return false;
if(s.length() < 2) return true;
```
```
char[] charArray = s.toCharArray();
int len = s.length();
```
```
int i=0;
int j=len-1;
```
```
while(i<j){
char left, right;
```
```
while(i<len-1 && !isAlpha(left) && !isNum(left)){
i++;
left = charArray[i];
}
```
```
while(j>0 && !isAlpha(right) && !isNum(right)){
j--;
```
91 | 677


35 Valid Palindrome

```
right = charArray[j];
}
```
```
if(i >= j)
break;
```
```
left = charArray[i];
right = charArray[j];
```
```
if(!isSame(left, right)){
return false;
}
```
```
i++;
j--;
}
return true;
}
```
```
public boolean isAlpha(char a){
if((a >= ’a’ && a <= ’z’) || (a >= ’A’ && a <= ’Z’)){
return true;
}else{
return false;
}
}
```
```
public boolean isNum(char a){
if(a >= ’0’ && a <= ’9’){
return true;
}else{
return false;
}
}
```
public boolean isSame(char a, char b){
if(isNum(a) && isNum(b)){
return a == b;
}else if(Character.toLowerCase(a) == Character.toLowerCase(b)){
return true;
}else{
return false;
}
}
}

92 | 677 Program Creek


```
35 Valid Palindrome
```
**35.3 Java Solution 2 - Using Stack**

This solution removes the special characters first. (Thanks to Tia)

public boolean isPalindrome(String s) {
s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();

```
int len = s.length();
if (len < 2)
return true;
```
```
Stack<Character> stack = new Stack<Character>();
```
```
int index = 0;
while (index < len / 2) {
stack.push(s.charAt(index));
index++;
}
```
```
if (len % 2 == 1)
index++;
```
```
while (index < len) {
if (stack.empty())
return false;
```
```
char temp = stack.pop();
if (s.charAt(index) != temp)
return false;
else
index++;
}
```
return true;
}

**35.4 Java Solution 3 - Using Two Pointers**

In the discussion below, April and Frank use two pointers to solve this problem. This
solution looks really simple.

public class ValidPalindrome {
public static boolean isValidPalindrome(String s){
if(s==null||s.length()==0) return false;

```
s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
System.out.println(s);
```
Program Creek 93 | 677


35 Valid Palindrome

```
for(int i = 0; i < s.length() ; i++){
if(s.charAt(i) != s.charAt(s.length() - 1 - i)){
return false;
}
}
```
```
return true;
}
```
```
public static void main(String[] args) {
String str = "A man, a plan, a canal: Panama";
```
System.out.println(isValidPalindrome(str));
}
}

94 | 677 Program Creek


## 36 Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in
constant time.

push(x) – Push element x onto stack. pop() – Removes the element on top of the
stack. top() – Get the top element. getMin() – Retrieve the minimum element in the
stack.

**36.1 Java Solution**

To make constant time of getMin(), we need to keep track of the minimum element
for each element in the stack. Define an element class that holds element value, min

value, and pointer to elements below it.

class Elem{
public int value;
public int min;
public Elem next;

public Elem(int value, int min){
this.value = value;
this.min = min;
}
}

public class MinStack {
public Elem top;

```
/**initialize your data structure here. */
public MinStack() {
```
```
}
```
```
public void push(int x) {
if(top == null){
top = new Elem(x, x);
}else{
Elem e = new Elem(x, Math.min(x,top.min));
e.next = top;
top = e;
}
```
```
}
```
95 | 677


36 Min Stack

```
public void pop() {
if(top == null)
return;
Elem temp = top.next;
top.next = null;
top = temp;
```
```
}
```
```
public int top() {
if(top == null)
return -1;
return top.value;
}
```
public int getMin() {
if(top == null)
return -1;
return top.min;
}
}

96 | 677 Program Creek


## 37 Largest Rectangle in Histogram

Given n non-negative integers representing the histogram’s bar height where the width
of each bar is 1 , find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1 , given height = [ 2 , 1 , 5 , 6 , 2 , 3 ].

For example, given height = [ 2 , 1 , 5 , 6 , 2 , 3 ], return 10.

**37.1 Analysis**

The key to solve this problem is to maintain a stack to store bars’ indexes. The stack

only keeps the increasing bars.

97 | 677


37 Largest Rectangle in Histogram

**37.2 Java Solution**

public int largestRectangleArea(int[] height) {
if (height == null || height.length == 0) {
return 0;
}

```
Stack<Integer> stack = new Stack<Integer>();
```
```
int max = 0;
int i = 0;
```
```
while (i < height.length) {
//push index to stack when the current height is larger than the previous
one
if (stack.isEmpty() || height[i] >= height[stack.peek()]) {
stack.push(i);
i++;
} else {
//calculate max value when the current height is less than the previous
one
int p = stack.pop();
int h = height[p];
int w = stack.isEmpty()? i : i - stack.peek() - 1;
max = Math.max(h* w, max);
}
```
```
}
```
```
while (!stack.isEmpty()) {
int p = stack.pop();
int h = height[p];
int w = stack.isEmpty()? i : i - stack.peek() - 1;
max = Math.max(h *w, max);
}
```
return max;
}

98 | 677 Program Creek


## 38 Maximal Rectangle

Given a 2 D binary matrix filled with 0 ’s and 1 ’s, find the largest rectangle containing

all ones and return its area.

**38.1 Analysis**

This problem can be converted to the "Largest Rectangle in Histogram" problem.

**38.2 Java Solution**

public int maximalRectangle(char[][] matrix) {
int m = matrix.length;
int n = m == 0? 0 : matrix[0].length;
int[][] height = new int[m][n + 1];

```
int maxArea = 0;
for (int i = 0; i < m; i++) {
for (int j = 0; j < n; j++) {
if (matrix[i][j] == ’0’) {
height[i][j] = 0;
} else {
height[i][j] = i == 0? 1 : height[i - 1][j] + 1;
}
}
}
```
```
for (int i = 0; i < m; i++) {
int area = maxAreaInHist(height[i]);
if (area > maxArea) {
maxArea = area;
}
}
```
return maxArea;
}

private int maxAreaInHist(int[] height) {
Stack<Integer> stack = new Stack<Integer>();

```
int i = 0;
int max = 0;
```
99 | 677


38 Maximal Rectangle

```
while (i < height.length) {
if (stack.isEmpty() || height[stack.peek()] <= height[i]) {
stack.push(i++);
} else {
int t = stack.pop();
max = Math.max(max, height[t]
* (stack.isEmpty()? i : i - stack.peek() - 1));
}
}
```
return max;
}

100 | 677 Program Creek


## 39 Valid Anagram

Given two strings s and t, write a function to determine if t is an anagram of s.

**39.1 Java Solution 1**

Assuming the string contains only lowercase alphabets, here is a simple solution.

public boolean isAnagram(String s, String t) {
if(s==null || t==null)
return false;

```
if(s.length()!=t.length())
return false;
```
```
int[] arr = new int[26];
for(int i=0; i<s.length(); i++){
arr[s.charAt(i)-’a’]++;
arr[t.charAt(i)-’a’]--;
}
```
```
for(int i: arr){
if(i!=0)
return false;
}
```
return true;
}

**39.2 Java Solution 2**

If the inputs contain unicode characters, an array with length of 26 is not enough.

public boolean isAnagram(String s, String t) {
if(s.length()!=t.length())
return false;

```
HashMap<Character, Integer> map = new HashMap<Character, Integer>();
```
```
for(int i=0; i<s.length(); i++){
char c1 = s.charAt(i);
if(map.containsKey(c1)){
```
101 | 677


39 Valid Anagram

```
map.put(c1, map.get(c1)+1);
}else{
map.put(c1,1);
}
}
```
```
for(int i=0; i<s.length(); i++){
char c2 = t.charAt(i);
if(map.containsKey(c2)){
if(map.get(c2)==1){
map.remove(c2);
}else{
map.put(c2, map.get(c2)-1);
}
}else{
return false;
}
}
```
```
if(map.size()>0)
return false;
```
return true;
}

102 | 677 Program Creek


## 40 Group Shifted Strings

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc"
->"bcd". We can keep "shifting" which forms the sequence: "abc" ->"bcd" ->... ->"xyz".
Given a list of strings which contains only lowercase alphabets, group all strings
that belong to the same shifting sequence, return:

[
["abc","bcd","xyz"],
["az","ba"],
["acef"],
["a","z"]
]

**40.1 Java Solution**

public List<List<String>> groupStrings(String[] strings) {
List<List<String>> result = new ArrayList<List<String>>();
HashMap<String, ArrayList<String>> map
= new HashMap<String, ArrayList<String>>();

```
for(String s: strings){
char[] arr = s.toCharArray();
if(arr.length>0){
int diff = arr[0]-’a’;
for(int i=0; i<arr.length; i++){
if(arr[i]-diff<’a’){
arr[i] = (char) (arr[i]-diff+26);
}else{
arr[i] = (char) (arr[i]-diff);
}
```
```
}
}
```
```
String ns = new String(arr);
if(map.containsKey(ns)){
map.get(ns).add(s);
}else{
ArrayList<String> al = new ArrayList<String>();
al.add(s);
map.put(ns, al);

}

}

for(Map.Entry<String, ArrayList<String>> entry: map.entrySet()){
Collections.sort(entry.getValue());
}
result.addAll(map.values());
return result;
}
```



## 41 Palindrome Pairs

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list, so

that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1 : Given words = ["bat", "tab", "cat"] Return [[ 0 , 1 ], [ 1 , 0 ]] The palindromes
are ["battab", "tabbat"]

**41.1 Java Solution**

public List<List<Integer>> palindromePairs(String[] words) {
List<List<Integer>> result = new ArrayList<List<Integer>>();

```
HashMap<String, Integer> map = new HashMap<String, Integer>();
for(int i=0; i<words.length; i++){
map.put(words[i], i);
}
```
```
for(int i=0; i<words.length; i++){
String s = words[i];
```
```
//if the word is a palindrome, get index of ""
if(isPalindrome(s)){
if(map.containsKey("")){
if(map.get("")!=i){
ArrayList<Integer> l = new ArrayList<Integer>();
l.add(i);
l.add(map.get(""));
result.add(l);
```
```
l = new ArrayList<Integer>();
```
```
l.add(map.get(""));
l.add(i);
result.add(l);
}
```
```
}
}
```
```
//if the reversed word exists, it is a palindrome
String reversed = new StringBuilder(s).reverse().toString();
if(map.containsKey(reversed)){
```
105 | 677


41 Palindrome Pairs

```
if(map.get(reversed)!=i){
ArrayList<Integer> l = new ArrayList<Integer>();
l.add(i);
l.add(map.get(reversed));
result.add(l);
}
}
```
```
for(int k=1; k<s.length(); k++){
String left = s.substring(0, k);
String right= s.substring(k);
```
```
//if left part is palindrome, find reversed right part
if(isPalindrome(left)){
String reversedRight = new
StringBuilder(right).reverse().toString();
if(map.containsKey(reversedRight)){
if(map.get(reversedRight)!=i){
ArrayList<Integer> l = new ArrayList<Integer>();
l.add(map.get(reversedRight));
l.add(i);
result.add(l);
}
}
}
```
```
//if right part is a palindrome, find reversed left part
if(isPalindrome(right)){
String reversedLeft = new
StringBuilder(left).reverse().toString();
if(map.containsKey(reversedLeft)){
if(map.get(reversedLeft)!=i){
```
```
ArrayList<Integer> l = new ArrayList<Integer>();
l.add(i);
l.add(map.get(reversedLeft));
result.add(l);
}
}
}
}
}
```
return result;
}

public boolean isPalindrome(String s){

```
int i=0;
```
106 | 677 Program Creek


```
41 Palindrome Pairs
```
```
int j=s.length()-1;
```
```
while(i<j){
if(s.charAt(i)!=s.charAt(j)){
return false;
}
```
i++;
j--;
}
return true;
}

Program Creek 107 | 677



## 42 Insert Delete GetRandom O(1)

Design a data structure that supports all following operations in O( 1 ) time.
insert(val): Inserts an item val to the set if not already present. remove(val): Re-
moves an item val from the set if present. getRandom: Returns a random element

from current set of elements. Each element must have the same probability of being
returned.

**42.1 Java Solution**

We can use two hashmaps to solve this problem. One uses value as keys and the other
uses index as the keys.

import java.util.Random;

public class RandomizedSet {

```
HashMap<Integer, Integer> map1;
HashMap<Integer, Integer> map2;
Random rand;
```
```
/**Initialize your data structure here. */
public RandomizedSet() {
map1 = new HashMap<Integer, Integer>();
map2 = new HashMap<Integer, Integer>();
rand = new Random(System.currentTimeMillis());
}
```
```
/**Inserts a value to the set. Returns true if the set did not already
contain the specified element. */
public boolean insert(int val) {
if(map1.containsKey(val)){
return false;
}else{
map1.put(val, map1.size());
map2.put(map2.size(), val);
}
return true;
}
```
```
/**Removes a value from the set. Returns true if the set contained the
specified element.*/
public boolean remove(int val) {
```
109 | 677


42 Insert Delete GetRandom O(1)

```
if(map1.containsKey(val)){
int index = map1.get(val);
```
```
//remove the entry from both maps
map1.remove(val);
map2.remove(index);
```
```
if(map1.size()==0){
return true;
}
```
```
//if last is deleted, do nothing
if(index==map1.size()){
return true;
}
```
```
//update the last element’s index
int key1 = map2.get(map2.size());
```
```
map1.put(key1, index);
map2.remove(map2.size());
map2.put(index, key1);
```
```
}else{
return false;
}
```
```
return true;
}
```
```
/**Get a random element from the set. */
public int getRandom() {
if(map1.size()==0){
return -1;
}
```
```
if(map1.size()==1){
return map2.get(0);
}
```
return map2.get(new Random().nextInt(map1.size()));
//return 0;
}
}

110 | 677 Program Creek


## 43 Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.
For example, the longest substring without repeating letters for "abcabcbb" is "abc",

which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

**43.1 Java Solution 1**

The first solution is like the problem of "determine if a string has all unique characters"
in CC 150. We can use a flag array to track the existing characters for the longest

substring without repeating characters.

public int lengthOfLongestSubstring(String s) {
if(s==null)
return 0;
boolean[] flag = new boolean[256];

```
int result = 0;
int start = 0;
char[] arr = s.toCharArray();
```
```
for (int i = 0; i < arr.length; i++) {
char current = arr[i];
if (flag[current]) {
result = Math.max(result, i - start);
// the loop update the new start point
// and reset flag array
// for example, abccab, when it comes to 2nd c,
// it update start from 0 to 3, reset flag for a,b
for (int k = start; k < i; k++) {
if (arr[k] == current) {
start = k + 1;
break;
}
flag[arr[k]] = false;
}
} else {
flag[current] = true;
}
}
```
111 | 677


43 Longest Substring Without Repeating Characters

```
result = Math.max(arr.length - start, result);
```
return result;
}

**43.2 Java Solution 2**

This solution is from Tia. It is easier to understand than the first solution.
The basic idea is using a hash table to track existing characters and their posi-

tion. When a repeated character occurs, check from the previously repeated character.
However, the time complexity is higher - O(n).

public static int lengthOfLongestSubstring(String s) {
if(s==null)
return 0;
char[] arr = s.toCharArray();
int pre = 0;

```
HashMap<Character, Integer> map = new HashMap<Character, Integer>();
```
```
for (int i = 0; i < arr.length; i++) {
if (!map.containsKey(arr[i])) {
map.put(arr[i], i);
} else {
pre = Math.max(pre, map.size());
i = map.get(arr[i]);
map.clear();
}
}
```
return Math.max(pre, map.size());
}

**43.3 Java Solution 3**

public int lengthOfLongestSubstring(String s) {
if(s==null){
return 0;
}

```
int max = 0;
```
```
HashMap<Character, Integer> map = new HashMap<Character, Integer>();
int start=0;
```
112 | 677 Program Creek


```
43 Longest Substring Without Repeating Characters
```
```
for(int i=0; i<s.length(); i++){
char c = s.charAt(i);
if(map.containsKey(c)){
max = Math.max(max, map.size());
while(map.containsKey(c)){
map.remove(s.charAt(start));
start++;
}
```
```
map.put(c, i);
}else{
map.put(c, i);
}
}
```
```
max = Math.max(max, map.size());
```
return max;
}

Program Creek 113 | 677



## 44 Longest Substring with At Most K Distinct Characters

This is a problem asked by Google.

Given a string, find the longest substring that contains only two unique charac-
ters. For example, given "abcbbbbcccbdddadacb", the longest substring that contains

2 unique character is "bcbbbbcccb".

**44.1 Longest Substring Which Contains 2 Unique**

**Characters**

In this solution, a hashmap is used to track the unique elements in the map. When a

third character is added to the map, the left pointer needs to move right.
You can use "abac" to walk through this solution.

public int lengthOfLongestSubstringTwoDistinct(String s) {
int max=0;
HashMap<Character,Integer> map = new HashMap<Character, Integer>();
int start=0;

```
for(int i=0; i<s.length(); i++){
char c = s.charAt(i);
if(map.containsKey(c)){
map.put(c, map.get(c)+1);
}else{
map.put(c,1);
}
```
```
if(map.size()>2){
max = Math.max(max, i-start);
```
```
while(map.size()>2){
char t = s.charAt(start);
int count = map.get(t);
if(count>1){
map.put(t, count-1);
}else{
map.remove(t);
}
start++;
}

}

}

max = Math.max(max, s.length()-start);
return max;
}
```

Now if this question is extended to be "the longest substring that contains k unique
characters", what should we do?

**44.2 Solution for K Unique Characters**

UPDATE ON 7 / 21 / 2016.

The following solution is corrected. Given "abcadcacacaca" and 3 , it returns "cadca-
cacaca".

public int lengthOfLongestSubstringKDistinct(String s, int k) {
if(k==0 || s==null || s.length()==0)
return 0;

```
if(s.length()<k)
return s.length();
```
```
HashMap<Character, Integer> map = new HashMap<Character, Integer>();
```
```
int maxLen=k;
int left=0;
for(int i=0; i<s.length(); i++){
char c = s.charAt(i);
if(map.containsKey(c)){
map.put(c, map.get(c)+1);
}else{
map.put(c, 1);
}
```
```
if(map.size()>k){
maxLen=Math.max(maxLen, i-left);
```
```
while(map.size()>k){
```
```
char fc = s.charAt(left);
if(map.get(fc)==1){
map.remove(fc);
}else{
map.put(fc, map.get(fc)-1);
}
left++;
}

}

}

maxLen = Math.max(maxLen, s.length()-left);
return maxLen;
}
```

Time is O(n).

Program Creek 117 | 677



## 45 Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length.

Find all starting indices of substring(s) in s that is a concatenation of each word in
words exactly once and without any intervening characters.
For example, given: s="barfoothefoobarman" & words=["foo", "bar"], return [ 0 , 9 ].

**45.1 Analysis**

This problem is similar (almost the same) to Longest Substring Which Contains 2
Unique Characters.
Since each word in the dictionary has the same length, each of them can be treated

as a single character.

**45.2 Java Solution**

public List<Integer> findSubstring(String s, String[] words) {
ArrayList<Integer> result = new ArrayList<Integer>();
if(s==null||s.length()==0||words==null||words.length==0){
return result;
}

```
//frequency of words
HashMap<String, Integer> map = new HashMap<String, Integer>();
for(String w: words){
if(map.containsKey(w)){
map.put(w, map.get(w)+1);
}else{
map.put(w, 1);
}
}
```
```
int len = words[0].length();
```
```
for(int j=0; j<len; j++){
HashMap<String, Integer> currentMap = new HashMap<String, Integer>();
int start = j;//start index of start
int count = 0;//count totoal qualified words so far
```
119 | 677


45 Substring with Concatenation of All Words

```
for(int i=j; i<=s.length()-len; i=i+len){
String sub = s.substring(i, i+len);
if(map.containsKey(sub)){
//set frequency in current map
if(currentMap.containsKey(sub)){
currentMap.put(sub, currentMap.get(sub)+1);
}else{
currentMap.put(sub, 1);
}
```
```
count++;
```
```
while(currentMap.get(sub)>map.get(sub)){
String left = s.substring(start, start+len);
currentMap.put(left, currentMap.get(left)-1);
```
```
count--;
start = start + len;
}
```
```
if(count==words.length){
result.add(start); //add to result
```
```
//shift right and reset currentMap, count & start point
String left = s.substring(start, start+len);
currentMap.put(left, currentMap.get(left)-1);
count--;
start = start + len;
}
}else{
currentMap.clear();
start = i+len;
count = 0;
}
}
}
```
return result;
}

120 | 677 Program Creek


## 46 Minimum Window Substring Contents

Given a string S and a string T, find the minimum window in S which will contain all
the characters in T in complexity O(n).

For example, S = "ADOBECODEBANC", T = "ABC", Minimum window is "BANC".

**46.1 Java Solution**

public String minWindow(String s, String t) {
if(t.length()>s.length())
return "";
String result = "";

```
//character counter for t
HashMap<Character, Integer> target = new HashMap<Character, Integer>();
for(int i=0; i<t.length(); i++){
char c = t.charAt(i);
if(target.containsKey(c)){
target.put(c,target.get(c)+1);
}else{
target.put(c,1);
}
}
```
```
// character counter for s
HashMap<Character, Integer> map = new HashMap<Character, Integer>();
int left = 0;
int minLen = s.length()+1;
```
```
int count = 0; // the total of mapped characters
```
```
for(int i=0; i<s.length(); i++){
char c = s.charAt(i);
```
```
if(target.containsKey(c)){
if(map.containsKey(c)){
if(map.get(c)<target.get(c)){
count++;
}
map.put(c,map.get(c)+1);
}else{
map.put(c,1);
count++;

}

}

if(count == t.length()){
char sc = s.charAt(left);
while (!map.containsKey(sc) || map.get(sc) > target.get(sc)) {
if (map.containsKey(sc) && map.get(sc) > target.get(sc))
map.put(sc, map.get(sc) - 1);
left++;
sc = s.charAt(left);
}
if (i - left + 1 < minLen) {
result = s.substring(left, i + 1);
minLen = i - left + 1;
}
}
}
return result;
}
```

## 47 Isomorphic Strings

Given two strings s and t, determine if they are isomorphic. Two strings are isomor-
phic if the characters in s can be replaced to get t.
For example,"egg" and "add" are isomorphic, "foo" and "bar" are not.

**47.1 Analysis**

We can define a map which tracks the char-char mappings. If a value is already
mapped, it can not be mapped again.

**47.2 Java Solution**

public boolean isIsomorphic(String s, String t) {
if(s==null||t==null)
return false;

```
if(s.length()!=t.length())
return false;
```
```
HashMap<Character, Character> map = new HashMap<Character, Character>();
```
```
for(int i=0; i<s.length(); i++){
char c1 = s.charAt(i);
char c2 = t.charAt(i);
```
```
if(map.containsKey(c1)){
if(map.get(c1)!=c2)// if not consistant with previous ones
return false;
}else{
if(map.containsValue(c2)) //if c2 is already being mapped
return false;
map.put(c1, c2);
}
}
```
return true;
}

Time is O(n).

123 | 677



## 48 Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements
sequence.
For example, given [ 100 , 4 , 200 , 1 , 3 , 2 ], the longest consecutive elements sequence
should be [ 1 , 2 , 3 , 4 ]. Its length is 4.

Your algorithm should run in O(n) complexity.

**48.1 Java Solution 1**

Because it requires O(n) complexity, we can not solve the problem by sorting the array
first. Sorting takes at least O(nlogn) time.
We can use a HashSet to add and remove elements. HashSet is implemented by

using a hash table. Elements are not ordered. The add, remove and contains methods
have constant time complexity O( 1 ).

public static int longestConsecutive(int[] num) {
// if array is empty, return 0
if (num.length == 0) {
return 0;
}

```
Set<Integer> set = new HashSet<Integer>();
int max = 1;
```
```
for (int e : num)
set.add(e);
for (int e : num) {
int left = e - 1;
int right = e + 1;
int count = 1;
while (set.contains(left)) {
count++;
set.remove(left);
left--;
}
while (set.contains(right)) {
count++;
set.remove(right);
right++;
}

max = Math.max(count, max);
}
return max;
}
```

**48.2 Java Solution 2**

We can also project the arrays to a new array with length to be the largest element in

the array. Then iterate over the array and get the longest consecutive sequence. If the
largest number is too large, then the time would be bad. This is just another thought.

126 | 677 Program Creek


## 49 Majority Element

Given an array of size n, find the majority element. The majority element is the element

that appears more thanbn/ 2 ctimes. (assume that the array is non-empty and the
majority element always exist in the array.)

**49.1 Java Solution 1 - Naive**

We can sort the array first, which takes time of nlog(n). Then scan once to find the
longest consecutive substrings.

public class Solution {
public int majorityElement(int[] num) {
if(num.length==1){
return num[0];
}

```
Arrays.sort(num);
```
```
int prev=num[0];
int count=1;
for(int i=1; i<num.length; i++){
if(num[i] == prev){
count++;
if(count > num.length/2) return num[i];
}else{
count=1;
prev = num[i];
}
}
```
return 0;
}
}

**49.2 Java Solution 2 - Much Simpler**

Thanks to SK. His/her solution is much efficient and simpler. Since the majority al-
ways take more than a half space, the middle element is guaranteed to be the majority.
Sorting array takes nlog(n). So the time complexity of this solution is nlog(n). Cheers!

127 | 677


49 Majority Element

public int majorityElement(int[] num) {
if (num.length == 1) {
return num[0];
}

Arrays.sort(num);
return num[num.length / 2];
}

**49.3 Java Solution 3 - Linear Time Majority Vote Algorithm**

public int majorityElement(int[] nums) {
int result = 0, count = 0;

```
for(int i = 0; i<nums.length; i++ ) {
if(count == 0){
result = nums[ i ];
count = 1;
}else if(result == nums[i]){
count++;
}else{
count--;
}
}
```
return result;
}

128 | 677 Program Creek


## 50 Majority Element II

Given an integer array of size n, find all elements that appear more thanbn/ 3 ctimes.
The algorithm should run in linear time and in O( 1 ) space.

**50.1 Java Solution 1 - Using a Counter**

Time = O(n) and Space = O(n)

public List<Integer> majorityElement(int[] nums) {
HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
for(int i: nums){
if(map.containsKey(i)){
map.put(i, map.get(i)+1);
}else{
map.put(i, 1);
}
}

```
List<Integer> result = new ArrayList<Integer>();
```
```
for(Map.Entry<Integer, Integer> entry: map.entrySet()){
if(entry.getValue() > nums.length/3){
result.add(entry.getKey());
}
}
```
return result;
}

**50.2 Java Solution 2**

Time = O(n) and Space = O( 1 )
Check out Majority Element I.

public List<Integer> majorityElement(int[] nums) {
List<Integer> result = new ArrayList<Integer>();

```
Integer n1=null, n2=null;
int c1=0, c2=0;
```
```
for(int i: nums){
```
129 | 677


50 Majority Element II

```
if(n1!=null && i==n1.intValue()){
c1++;
}else if(n2!=null && i==n2.intValue()){
c2++;
}else if(c1==0){
c1=1;
n1=i;
}else if(c2==0){
c2=1;
n2=i;
}else{
c1--;
c2--;
}
}
```
```
c1=c2=0;
```
```
for(int i: nums){
if(i==n1.intValue()){
c1++;
}else if(i==n2.intValue()){
c2++;
}
}
```
```
if(c1>nums.length/3)
result.add(n1);
if(c2>nums.length/3)
result.add(n2);
```
return result;
}

130 | 677 Program Creek


## 51 Increasing Triplet Subsequence

Given an unsorted array return whether an increasing subsequence of length 3 exists
or not in the array.
Examples: Given [ 1 , 2 , 3 , 4 , 5 ], return true.
Given [ 5 , 4 , 3 , 2 , 1 ], return false.

**51.1 Analysis**

This problem can be converted to be finding if there is a sequence such that the_smallest_so_far
<the_second_smallest_so_far <current. We use x, y and z to denote the 3 number re-

spectively.

**51.2 Java Solution**

public boolean increasingTriplet(int[] nums) {
int x = Integer.MAX_VALUE;
int y = Integer.MAX_VALUE;

```
for (int i = 0; i < nums.length; i++) {
int z = nums[i];
```
```
if (x >= z) {
x = z;// update x to be a smaller value
} else if (y >= z) {
y = z; // update y to be a smaller value
} else {
return true;
}
}
```
return false;
}

131 | 677



## 52 Rotate Array in Java

**52.1 Problem**

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3 , the array [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ] is rotated to [ 5 , 6 , 7 , 1 , 2 , 3 , 4 ].
How many different ways do you know to solve this problem?

**52.2 Solution 1 - Intermediate Array**

In a straightforward way, we can create a new array and then copy elements to the
new array. Then change the original array by using System.arraycopy().

public void rotate(int[] nums, int k) {
if(k > nums.length)
k=k%nums.length;

```
int[] result = new int[nums.length];
```
```
for(int i=0; i < k; i++){
result[i] = nums[nums.length-k+i];
}
```
```
int j=0;
for(int i=k; i<nums.length; i++){
result[i] = nums[j];
j++;
}
```
System.arraycopy( result, 0, nums, 0, nums.length );
}

Space is O(n) and time is O(n). You can check out the difference between Sys-

tem.arraycopy() and Arrays.copyOf().

**52.3 Solution 2 - Bubble Rotate**

Can we do this in O( 1 ) space?

This solution is like a bubble sort.

public static void rotate(int[] arr, int order) {
if (arr == null || order < 0) {

133 | 677


52 Rotate Array in Java

```
throw new IllegalArgumentException("Illegal argument!");
}
```
for (int i = 0; i < order; i++) {
for (int j = arr.length - 1; j > 0; j--) {
int temp = arr[j];
arr[j] = arr[j - 1];
arr[j - 1] = temp;
}
}
}

```
However, the time is O(n*k).
Here is an example (length= 7 , order= 3 ):
```
i=0
0 1 2 3 4 5 6
0 1 2 3 4 6 5
...
6 0 1 2 3 4 5
i=1
6 0 1 2 3 5 4
...
5 6 0 1 2 3 4
i=2
5 6 0 1 2 4 3
...
4 5 6 0 1 2 3

**52.4 Solution 3 - Reversal**

Can we do this in O( 1 ) space and in O(n) time? The following solution does.
Assuming we are given 1 , 2 , 3 , 4 , 5 , 6 and order 2. The basic idea is:

1. Divide the array two parts: 1,2,3,4 and 5, 6
2. Reverse first part: 4,3,2,1,5,6
3. Reverse second part: 4,3,2,1,6,5
4. Reverse the whole array: 5,6,1,2,3,4

public static void rotate(int[] arr, int order) {
if (arr == null || arr.length==0 || order < 0) {
throw new IllegalArgumentException("Illegal argument!");
}

```
if(order > arr.length){
order = order %arr.length;
}
```
134 | 677 Program Creek


```
52 Rotate Array in Java
```
```
//length of first part
int a = arr.length - order;
```
```
reverse(arr, 0, a-1);
reverse(arr, a, arr.length-1);
reverse(arr, 0, arr.length-1);
```
}

public static void reverse(int[] arr, int left, int right){
if(arr == null || arr.length == 1)
return;

while(left < right){
int temp = arr[left];
arr[left] = arr[right];
arr[right] = temp;
left++;
right--;
}
}

Program Creek 135 | 677



## 53 Reverse Words in a String II

Given an input string, reverse the string word by word. A word is defined as a se-
quence of non-space characters.
The input string does not contain leading or trailing spaces and the words are always
separated by a single space.

```
For example, Given s = "the sky is blue", return "blue is sky the".
Could you do it in-place without allocating extra space?
```
**53.1 Java Solution**

public void reverseWords(char[] s) {
int i=0;
for(int j=0; j<s.length; j++){
if(s[j]==’ ’){
reverse(s, i, j-1);
i=j+1;
}
}

```
reverse(s, i, s.length-1);
```
reverse(s, 0, s.length-1);
}

public void reverse(char[] s, int i, int j){
while(i<j){
char temp = s[i];
s[i]=s[j];
s[j]=temp;
i++;
j--;
}
}

137 | 677



## 54 Group Anagrams

Given an array of strings, return all groups of strings that are anagrams.

**54.1 Analysis**

```
An anagram is a type of word play, the result of rearranging the letters of a word or
phrase to produce a new word or phrase, using all the original letters exactly once; for
example, Torchwood can be rearranged into Doctor Who.
If two strings are anagram to each other, their sorted sequence is the same.
Updated on 5 / 1 / 2016.
```
**54.2 Java Solution**

public List<List<String>> groupAnagrams(String[] strs) {
List<List<String>> result = new ArrayList<List<String>>();

```
HashMap<String, ArrayList<String>> map = new HashMap<String,
ArrayList<String>>();
for(String str: strs){
char[] arr = new char[26];
for(int i=0; i<str.length(); i++){
arr[str.charAt(i)-’a’]++;
}
String ns = new String(arr);
```
```
if(map.containsKey(ns)){
map.get(ns).add(str);
}else{
ArrayList<String> al = new ArrayList<String>();
al.add(str);
map.put(ns, al);
}
}
```
```
result.addAll(map.values());
```
return result;
}

139 | 677


54 Group Anagrams

**54.3 Time Complexity**

If the average length of verbs is m and array length is n, then the time is O(n*m).

140 | 677 Program Creek


## 55 Wildcard Matching

Implement wildcard pattern matching with support for ’?’ and ’*’.

**55.1 Java Solution**

To understand this solution, you can use s="aab" and p="*ab".

public boolean isMatch(String s, String p) {
int i = 0;
int j = 0;
int starIndex = -1;
int iIndex = -1;

```
while (i < s.length()) {
if (j < p.length() && (p.charAt(j) == ’?’ || p.charAt(j) == s.charAt(i)))
{
++i;
++j;
} else if (j < p.length() && p.charAt(j) == ’*’) {
starIndex = j;
iIndex = i;
j++;
} else if (starIndex != -1) {
j = starIndex + 1;
i = iIndex+1;
iIndex++;
} else {
return false;
}
}
```
```
while (j < p.length() && p.charAt(j) == ’*’) {
++j;
}
```
return j == p.length();
}

141 | 677



## 56 Regular Expression Matching in Java

Implement regular expression matching with support for ’.’ and ’*’.

’.’ Matches any single character. ’*’ Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
The function prototype should be: bool isMatch(const char *s, const char *p)
Some examples: isMatch("aa","a") return false isMatch("aa","aa") return true isMatch("aaa","aa")
return false isMatch("aa", "a*") return true isMatch("aa", ".*") return true isMatch("ab",
".*") return true isMatch("aab", "c*a*b") return true

**56.1 Analysis**

First of all, this is one of the most difficulty problems. It is hard to think through all

different cases. The problem should be simplified to handle 2 basic cases:

- the second char of pattern is "*"
- the second char of pattern is not "*"

For the 1 st case, if the first char of pattern is not ".", the first char of pattern and
string should be the same. Then continue to match the remaining part.

For the 2 nd case, if the first char of pattern is "." or first char of pattern == the first i
char of string, continue to match the remaining part.

**56.2 Java Solution 1 (Short)**

The following Java solution is accepted.

public class Solution {
public boolean isMatch(String s, String p) {

```
if(p.length() == 0)
return s.length() == 0;
```
```
//p’s length 1 is special case
if(p.length() == 1 || p.charAt(1) != ’*’){
if(s.length() < 1 || (p.charAt(0) != ’.’ && s.charAt(0) !=
p.charAt(0)))
return false;
return isMatch(s.substring(1), p.substring(1));
```
```
}else{
```
143 | 677


56 Regular Expression Matching in Java

```
int len = s.length();
```
int i = -1;
while(i<len && (i < 0 || p.charAt(0) == ’.’ || p.charAt(0) ==
s.charAt(i))){
if(isMatch(s.substring(i+1), p.substring(2)))
return true;
i++;
}
return false;
}
}
}

**56.3 Java Solution 2 (More Readable)**

public boolean isMatch(String s, String p) {
// base case
if (p.length() == 0) {
return s.length() == 0;
}

```
// special case
if (p.length() == 1) {
```
```
// if the length of s is 0, return false
if (s.length() < 1) {
return false;
}
```
```
//if the first does not match, return false
else if ((p.charAt(0) != s.charAt(0)) && (p.charAt(0) != ’.’)) {
return false;
}
```
```
// otherwise, compare the rest of the string of s and p.
else {
return isMatch(s.substring(1), p.substring(1));
}
}
```
```
// case 1: when the second char of p is not ’*’
if (p.charAt(1) != ’*’) {
if (s.length() < 1) {
return false;
}
if ((p.charAt(0) != s.charAt(0)) && (p.charAt(0) != ’.’)) {
```
144 | 677 Program Creek


```
56 Regular Expression Matching in Java
```
```
return false;
} else {
return isMatch(s.substring(1), p.substring(1));
}
}
```
```
// case 2: when the second char of p is ’*’, complex case.
else {
//case 2.1: a char & ’*’ can stand for 0 element
if (isMatch(s, p.substring(2))) {
return true;
}
```
//case 2.2: a char & ’*’ can stand for 1 or more preceding element,
//so try every sub string
int i = 0;
while (i<s.length() && (s.charAt(i)==p.charAt(0) || p.charAt(0)==’.’)){
if (isMatch(s.substring(i + 1), p.substring(2))) {
return true;
}
i++;
}
return false;
}
}

Program Creek 145 | 677



## 57 Get Target Number Using Number List and Arithmetic Operations

Given a list of numbers and a target number, write a program to determine whether
the target number can be calculated by applying "+-*/" operations to the number list?

You can assume () is automatically added when necessary.
For example, given 1 , 2 , 3 , 4 and 21 , return true. Because ( 1 + 2 )*( 3 + 4 )= 21

**57.1 Analysis**

This is a partition problem which can be solved by using depth first search.

**57.2 Java Solution**

public static boolean isReachable(ArrayList<Integer> list, int target) {
if (list == null || list.size() == 0)
return false;

```
int i = 0;
int j = list.size() - 1;
```
```
ArrayList<Integer> results = getResults(list, i, j, target);
```
```
for (int num : results) {
if (num == target) {
return true;
}
}
```
return false;
}

public static ArrayList<Integer> getResults(ArrayList<Integer> list,
int left, int right, int target) {
ArrayList<Integer> result = new ArrayList<Integer>();

```
if (left > right) {
return result;
} else if (left == right) {
result.add(list.get(left));
```
147 | 677


57 Get Target Number Using Number List and Arithmetic Operations

```
return result;
}
```
```
for (int i = left; i < right; i++) {
```
```
ArrayList<Integer> result1 = getResults(list, left, i, target);
ArrayList<Integer> result2 = getResults(list, i + 1, right, target);
```
```
for (int x : result1) {
for (int y : result2) {
result.add(x + y);
result.add(x - y);
result.add(x * y);
if (y != 0)
result.add(x / y);
}
}
}
```
return result;
}

148 | 677 Program Creek


## 58 Flip Game

You are playing the following Flip Game with your friend: Given a string that con-
tains only these two characters: + and -, you and your friend take turns to flip two
consecutive "++" into "–". The game ends when a person can no longer make a move
and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

**58.1 Java Solution**

public List<String> generatePossibleNextMoves(String s) {
List<String> result = new ArrayList<String>();

```
if(s==null)
return result;
```
```
char[] arr = s.toCharArray();
for(int i=0; i<arr.length-1; i++){
if(arr[i]==arr[i+1] && arr[i]==’+’){
arr[i]=’-’;
arr[i+1]=’-’;
result.add(new String(arr));
arr[i]=’+’;
arr[i+1]=’+’;
}
}
```
return result;
}

149 | 677



## 59 Flip Game II

You are playing the following Flip Game with your friend: Given a string that con-

tains only these two characters: + and -, you and your friend take turns to flip two
consecutive "++" into "–". The game ends when a person can no longer make a move
and therefore the other person will be the winner.
Write a function to determine if the starting player can guarantee a win.
For example, given s = "++++", return true. The starting player can guarantee a win
by flipping the middle "++" to become "+–+".

**59.1 Java Solution**

This problem is solved by backtracking.

public boolean canWin(String s) {
if(s==null||s.length()==0){
return false;
}

return canWinHelper(s.toCharArray());
}

public boolean canWinHelper(char[] arr){
for(int i=0; i<arr.length-1;i++){
if(arr[i]==’+’&&arr[i+1]==’+’){
arr[i]=’-’;
arr[i+1]=’-’;

```
boolean win = canWinHelper(arr);
```
```
arr[i]=’+’;
arr[i+1]=’+’;
```
```
//if there is a flip which makes the other player lose, the first
play wins
if(!win){
return true;
}
}
}
```
return false;
}

151 | 677


59 Flip Game II

**59.2 Time Complexity**

Roughly, the time is n*n*...n, which is O(nn). The reason is each recursion takes O(n)ˆ
and there are totally n recursions.

152 | 677 Program Creek


## 60 Word Pattern

Given a pattern and a string str, find if str follows the same pattern. Here follow means
a full match, such that there is a bijection between a letter in pattern and a non-empty
word in str.

**60.1 Java Solution**

public boolean wordPattern(String pattern, String str) {
String[] arr = str.split(" ");

```
//prevent out of boundary problem
if(arr.length != pattern.length())
return false;
```
```
HashMap<Character, String> map = new HashMap<Character, String>();
for(int i=0; i<pattern.length(); i++){
char c = pattern.charAt(i);
if(map.containsKey(c)){
String value = map.get(c);
if(!value.equals(arr[i])){
return false;
}
}else if (map.containsValue(arr[i])){
return false;
}
map.put(c, arr[i]);
}
```
return true;
}

153 | 677



## 61 Word Pattern II

This is the extension problem of Word Pattern I.
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in
pattern and a non-empty substring in str.
Examples: pattern = "abab", str = "redblueredblue" should return true. pattern =

"aaaa", str = "asdasdasdasd" should return true. pattern = "aabb", str = "xyzabcxzyabc"
should return false.

**61.1 Java Solution**

public boolean wordPatternMatch(String pattern, String str) {
if(pattern.length()==0 && str.length()==0)
return true;
if(pattern.length()==0)
return false;

```
HashMap<Character, String> map = new HashMap<Character, String>();
```
return helper(pattern, str, 0, 0, map);
}

public boolean helper(String pattern, String str, int i, int j,
HashMap<Character, String> map){
if(i==pattern.length() && j==str.length()){
return true;
}

```
if(i>=pattern.length() || j>=str.length())
return false;
```
```
char c = pattern.charAt(i);
for(int k=j+1; k<=str.length(); k++){
String sub = str.substring(j, k);
if(!map.containsKey(c) && !map.containsValue(sub)){
map.put(c, sub);
if(helper(pattern, str, i+1, k, map))
return true;
map.remove(c);
}else if(map.containsKey(c) && map.get(c).equals(sub)){
if(helper(pattern, str, i+1, k, map))
```
155 | 677


61 Word Pattern II

```
return true;
}
}
```
return false;
}

Since containsValue() method is used here, the time complexity is O(n). We can use

another set to track the value set which leads to time complexity of O( 1 ):

public boolean wordPatternMatch(String pattern, String str) {
if(pattern.length()==0 && str.length()==0)
return true;
if(pattern.length()==0)
return false;

HashMap<Character, String> map = new HashMap<Character, String>();
HashSet<String> set = new HashSet<String>();
return helper(pattern, str, 0, 0, map, set);
}

public boolean helper(String pattern, String str, int i, int j,
HashMap<Character, String> map, HashSet<String> set){
if(i==pattern.length() && j==str.length()){
return true;
}

```
if(i>=pattern.length() || j>=str.length())
return false;
```
```
char c = pattern.charAt(i);
for(int k=j+1; k<=str.length(); k++){
String sub = str.substring(j, k);
if(!map.containsKey(c) && !set.contains(sub)){
map.put(c, sub);
set.add(sub);
if(helper(pattern, str, i+1, k, map, set))
return true;
map.remove(c);
set.remove(sub);
}else if(map.containsKey(c) && map.get(c).equals(sub)){
if(helper(pattern, str, i+1, k, map, set))
return true;
}
}
```
return false;
}

The time complexity then is f(n) = n*(n- 1 )*... * 1 =nn.ˆ

156 | 677 Program Creek


## 62 Scramble String

Given two strings s 1 and s 2 of the same length, determine if s 2 is a scrambled string
of s 1.

**62.1 Java Solution**

public boolean isScramble(String s1, String s2) {
if(s1.length()!=s2.length())
return false;

```
if(s1.length()==0 || s1.equals(s2))
return true;
```
```
char[] arr1 = s1.toCharArray();
char[] arr2 = s2.toCharArray();
Arrays.sort(arr1);
Arrays.sort(arr2);
if(!new String(arr1).equals(new String(arr2))){
return false;
}
```
```
for(int i=1; i<s1.length(); i++){
String s11 = s1.substring(0, i);
String s12 = s1.substring(i, s1.length());
String s21 = s2.substring(0, i);
String s22 = s2.substring(i, s2.length());
String s23 = s2.substring(0, s2.length()-i);
String s24 = s2.substring(s2.length()-i, s2.length());
```
```
if(isScramble(s11, s21) && isScramble(s12, s22))
return true;
if(isScramble(s11, s24) && isScramble(s12, s23))
return true;
}
```
return false;
}

157 | 677



## 63 Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string
valid. Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).
Examples: "()())()" ->["()()()", "(())()"] "(a)())()" ->["(a)()()", "(a())()"] ")(" ->[""]

**63.1 Java Solution**

This problem can be solve by using DFS.

public class Solution {
ArrayList<String> result = new ArrayList<String>();
int max=0;

```
public List<String> removeInvalidParentheses(String s) {
if(s==null)
return result;
```
```
dfs(s, "", 0, 0);
if(result.size()==0){
result.add("");
}
```
```
return result;
}
```
```
public void dfs(String left, String right, int countLeft, int maxLeft){
if(left.length()==0){
if(countLeft==0 && right.length()!=0){
if(maxLeft > max){
max = maxLeft;
}
```
```
if(maxLeft==max && !result.contains(right)){
result.add(right);
}
}
```
```
return;
}
```
```
if(left.charAt(0)==’(’){
```
159 | 677


63 Remove Invalid Parentheses

```
dfs(left.substring(1), right+"(", countLeft+1, maxLeft+1);//keep (
dfs(left.substring(1), right, countLeft, maxLeft);//drop (
}else if(left.charAt(0)==’)’){
if(countLeft>0){
dfs(left.substring(1), right+")", countLeft-1, maxLeft);
}
```
```
dfs(left.substring(1), right, countLeft, maxLeft);
```
}else{
dfs(left.substring(1), right+String.valueOf(left.charAt(0)),
countLeft, maxLeft);
}
}
}

160 | 677 Program Creek


## 64 Shortest Palindrome

Given a string S, you are allowed to convert it to a palindrome by adding characters in
front of it. Find and return the shortest palindrome you can find by performing this
transformation.

For example, given "aacecaaa", return "aaacecaaa"; given "abcd", return "dcbabcd".

**64.1 Java Solution 1**

public String shortestPalindrome(String s) {
int i=0;
int j=s.length()-1;

```
while(j>=0){
if(s.charAt(i)==s.charAt(j)){
i++;
}
j--;
}
```
```
if(i==s.length())
return s;
```
String suffix = s.substring(i);
String prefix = new StringBuilder(suffix).reverse().toString();
String mid = shortestPalindrome(s.substring(0, i));
return prefix+mid+suffix;
}

**64.2 Java Solution 2**

We can solve this problem by using one of the methods which is used to solve the
longest palindrome substring problem.
Specifically, we can start from the center and scan two sides. If read the left bound-

ary, then the shortest palindrome is identified.

public String shortestPalindrome(String s) {
if (s == null || s.length() <= 1)
return s;

161 | 677


64 Shortest Palindrome

```
String result = null;
```
```
int len = s.length();
int mid = len / 2;
```
```
for (int i = mid; i >= 1; i--) {
if (s.charAt(i) == s.charAt(i - 1)) {
if ((result = scanFromCenter(s, i - 1, i)) != null)
return result;
} else {
if ((result = scanFromCenter(s, i - 1, i - 1)) != null)
return result;
}
}
```
return result;
}

private String scanFromCenter(String s, int l, int r) {
int i = 1;

```
//scan from center to both sides
for (; l - i >= 0; i++) {
if (s.charAt(l - i) != s.charAt(r + i))
break;
}
```
```
//if not end at the beginning of s, return null
if (l - i >= 0)
return null;
```
```
StringBuilder sb = new StringBuilder(s.substring(r + i));
sb.reverse();
```
return sb.append(s).toString();
}

162 | 677 Program Creek


## 65 Word Ladder

Given two words (start and end), and a dictionary, find the length of shortest transfor-
mation sequence from start to end, such that only one letter can be changed at a time
and each intermediate word must exist in the dictionary. For example, given:

start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

One shortest transformation is "hit" ->"hot" ->"dot" ->"dog" ->"cog", the program
should return its length 5.

**65.1 Analysis**

UPDATED on 06 / 07 / 2015.
So we quickly realize that this is a search problem, and breath-first search guarantees
the optimal solution.

**65.2 Java Solution**

class WordNode{
String word;
int numSteps;

public WordNode(String word, int numSteps){
this.word = word;
this.numSteps = numSteps;
}
}

163 | 677


65 Word Ladder

public class Solution {
public int ladderLength(String beginWord, String endWord, Set<String>
wordDict) {
LinkedList<WordNode> queue = new LinkedList<WordNode>();
queue.add(new WordNode(beginWord, 1));

```
wordDict.add(endWord);
```
```
while(!queue.isEmpty()){
WordNode top = queue.remove();
String word = top.word;
```
```
if(word.equals(endWord)){
return top.numSteps;
}
```
```
char[] arr = word.toCharArray();
for(int i=0; i<arr.length; i++){
for(char c=’a’; c<=’z’; c++){
char temp = arr[i];
if(arr[i]!=c){
arr[i]=c;
}
```
```
String newWord = new String(arr);
if(wordDict.contains(newWord)){
queue.add(new WordNode(newWord, top.numSteps+1));
wordDict.remove(newWord);
}
```
```
arr[i]=temp;
}
}
}
```
return 0;
}
}

164 | 677 Program Creek


## 66 Word Ladder II

Given two words (start and end), and a dictionary, find all shortest transformation

sequence(s) from start to end, such that: 1 ) Only one letter can be changed at a time,
2 ) Each intermediate word must exist in the dictionary.
For example, given: start = "hit", end = "cog", and dict = ["hot","dot","dog","lot","log"],
return:

[
["hit","hot","dot","dog","cog"],
["hit","hot","lot","log","cog"]
]

**66.1 Analysis**

This is an extension of Word Ladder.

The idea is the same. To track the actual ladder, we need to add a pointer that points
to the previous node in the WordNode class.
In addition, the used word can not directly removed from the dictionary. The used

word is only removed when steps change.

**66.2 Java Solution**

class WordNode{
String word;
int numSteps;
WordNode pre;

public WordNode(String word, int numSteps, WordNode pre){
this.word = word;
this.numSteps = numSteps;
this.pre = pre;
}
}

public class Solution {
public List<List<String>> findLadders(String start, String end,
Set<String> dict) {
List<List<String>> result = new ArrayList<List<String>>();

165 | 677


66 Word Ladder II

```
LinkedList<WordNode> queue = new LinkedList<WordNode>();
queue.add(new WordNode(start, 1, null));
```
```
dict.add(end);
```
```
int minStep = 0;
```
```
HashSet<String> visited = new HashSet<String>();
HashSet<String> unvisited = new HashSet<String>();
unvisited.addAll(dict);
```
```
int preNumSteps = 0;
```
```
while(!queue.isEmpty()){
WordNode top = queue.remove();
String word = top.word;
int currNumSteps = top.numSteps;
```
```
if(word.equals(end)){
if(minStep == 0){
minStep = top.numSteps;
}
```
```
if(top.numSteps == minStep && minStep !=0){
//nothing
ArrayList<String> t = new ArrayList<String>();
t.add(top.word);
while(top.pre !=null){
t.add(0, top.pre.word);
top = top.pre;
}
result.add(t);
continue;
}
```
```
}
```
```
if(preNumSteps < currNumSteps){
unvisited.removeAll(visited);
}
```
```
preNumSteps = currNumSteps;
```
```
char[] arr = word.toCharArray();
for(int i=0; i<arr.length; i++){
for(char c=’a’; c<=’z’; c++){
char temp = arr[i];
if(arr[i]!=c){
arr[i]=c;
}
String newWord = new String(arr);
if(unvisited.contains(newWord)){
queue.add(new WordNode(newWord, top.numSteps+1, top));
visited.add(newWord);
}
arr[i]=temp;
}
}
}

return result;
}
}
```


## 67 Kth Largest Element in an Array

Find the kth largest element in an unsorted array. Note that it is the kth largest element
in the sorted order, not the kth distinct element.

```
For example, given [ 3 , 2 , 1 , 5 , 6 , 4 ] and k = 2 , return 5.
Note: You may assume k is always valid, 1 ≤k≤array’s length.
```
**67.1 Java Solution 1 - Sorting**

public int findKthLargest(int[] nums, int k) {
Arrays.sort(nums);
return nums[nums.length-k];
}

Time is O(nlog(n))

**67.2 Java Solution 2 - Quick Sort**

This problem can also be solve by using the quickselect approach, which is similar to

quicksort.

public int findKthLargest(int[] nums, int k) {
if (k < 1 || nums == null) {
return 0;
}

return getKth(nums.length - k +1, nums, 0, nums.length - 1);
}

public int getKth(int k, int[] nums, int start, int end) {

```
int pivot = nums[end];
```
```
int left = start;
int right = end;
```
```
while (true) {
```
```
while (nums[left] < pivot && left < right) {
left++;
}
```
169 | 677


67 Kth Largest Element in an Array

```
while (nums[right] >= pivot && right > left) {
right--;
}
```
```
if (left == right) {
break;
}
```
```
swap(nums, left, right);
}
```
```
swap(nums, left, end);
```
if (k == left + 1) {
return pivot;
} else if (k < left + 1) {
return getKth(k, nums, start, left - 1);
} else {
return getKth(k, nums, left + 1, end);
}
}

public void swap(int[] nums, int n1, int n2) {
int tmp = nums[n1];
nums[n1] = nums[n2];
nums[n2] = tmp;
}

Average case time is O(n), worst case time is O(n 2 ˆ).

**67.3 Java Solution 3 - Heap**

We can use a min heap to solve this problem. The heap stores the top k elements.
Whenever the size is greater than k, delete the min. Time complexity is O(nlog(k)).
Space complexity is O(k) for storing the top k numbers.

public int findKthLargest(int[] nums, int k) {
PriorityQueue<Integer> q = new PriorityQueue<Integer>(k);
for(int i: nums){
q.offer(i);

```
if(q.size()>k){
q.poll();
}
}
```
return q.peek();
}

170 | 677 Program Creek


## 68 Top K Frequent Elements

Given a non-empty array of integers, return the k most frequent elements.

**68.1 Java Solution 1 - Using HashMap and Heap**

Time is O(n*log(k)).

class Pair{
int num;
int count;
public Pair(int num, int count){
this.num=num;
this.count=count;
}
}

public class Solution {
public List<Integer> topKFrequent(int[] nums, int k) {
//count the frequency for each element
HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
for(int num: nums){
if(map.containsKey(num)){
map.put(num, map.get(num)+1);
}else{
map.put(num, 1);
}
}

```
// create a min heap
PriorityQueue<Pair> queue = new PriorityQueue<Pair>(new
Comparator<Pair>(){
public int compare(Pair a, Pair b){
return a.count-b.count;
}
});
```
```
//maintain a heap of size k.
for(Map.Entry<Integer, Integer> entry: map.entrySet()){
Pair p = new Pair(entry.getKey(), entry.getValue());
queue.offer(p);
if(queue.size()>k){
queue.poll();
}
//get all elements from the heap
List<Integer> result = new ArrayList<Integer>();
while(queue.size()>0){
result.add(queue.poll().num);
}
//reverse the order
Collections.reverse(result);
return result;
}
}
```

**68.2 Java Solution 2 - Bucket Sort**

Time is O(n).

public List<Integer> topKFrequent(int[] nums, int k) {
//count the frequency for each element
HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
for(int num: nums){
if(map.containsKey(num)){
map.put(num, map.get(num)+1);
}else{
map.put(num, 1);
}
}

```
//get the max frequency
int max = 0;
for(Map.Entry<Integer, Integer> entry: map.entrySet()){
max = Math.max(max, entry.getValue());
}
```
```
//initialize an array of ArrayList. index is frequency, value is list of
numbers
ArrayList<Integer>[] arr = (ArrayList<Integer>[]) new ArrayList[max+1];
for(int i=1; i<=max; i++){
arr[i]=new ArrayList<Integer>();
}
```
```
for(Map.Entry<Integer, Integer> entry: map.entrySet()){
int count = entry.getValue();
int number = entry.getKey();
arr[count].add(number);
}
```
172 | 677 Program Creek


```
68 Top K Frequent Elements
```
```
List<Integer> result = new ArrayList<Integer>();
```
```
//add most frequent numbers to result
for(int j=max; j>=1; j--){
if(arr[j].size()>0){
for(int a: arr[j]){
result.add(a);
}
}
```
```
if(result.size()==k)
break;
}
```
return result;
}

**68.3 Java Solution 3 - A Regular Counter (Deprecated)**

We can solve this problem by using a regular counter, and then sort the counter by
value.

public class Solution {
public List<Integer> topKFrequent(int[] nums, int k) {
List<Integer> result = new ArrayList<Integer>();

```
HashMap<Integer, Integer> counter = new HashMap<Integer, Integer>();
```
```
for(int i: nums){
if(counter.containsKey(i)){
counter.put(i, counter.get(i)+1);
}else{
counter.put(i, 1);
}
}
```
```
TreeMap<Integer, Integer> sortedMap = new TreeMap<Integer, Integer>(new
ValueComparator(counter));
sortedMap.putAll(counter);
```
```
int i=0;
for(Map.Entry<Integer, Integer> entry: sortedMap.entrySet()){
result.add(entry.getKey());
i++;
if(i==k)
break;
}
```
Program Creek 173 | 677


68 Top K Frequent Elements

return result;
}
}

class ValueComparator implements Comparator<Integer>{
HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

```
public ValueComparator(HashMap<Integer, Integer> m){
map.putAll(m);
}
```
```
public int compare(Integer i1, Integer i2){
int diff = map.get(i2)-map.get(i1);
```
if(diff==0){
return 1;
}else{
return diff;
}
}
}

174 | 677 Program Creek


## 69 Meeting Rooms II

Given an array of meeting time intervals consisting of start and end times [[s 1 ,e 1 ],[s 2 ,e 2 ],...]
find the minimum number of conference rooms required.

**69.1 Java Solution**

public int minMeetingRooms(Interval[] intervals) {
if(intervals==null||intervals.length==0)
return 0;

```
Arrays.sort(intervals, new Comparator<Interval>(){
public int compare(Interval i1, Interval i2){
return i1.start-i2.start;
}
});
```
```
PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
int count=1;
queue.offer(intervals[0].end);
```
```
for(int i=1; i<intervals.length; i++){
if(intervals[i].start<queue.peek()){
count++;
```
```
}else{
queue.poll();
}
```
```
queue.offer(intervals[i].end);
}
```
return count;
}

175 | 677



## 70 Meeting Rooms

**70.1 Given an array of meeting time intervals consisting of**

```
start and end times [[s1,e1],[s2,e2],...] (si <ei),
determine if a person could attend all meetings. For
example, Given [[0, 30],[5, 10],[15, 20]], return false.
Java Solution
```
If a person can attend all meetings, there must not be any overlaps between any meet-
ings. After sorting the intervals, we can compare the current end and next start.

public boolean canAttendMeetings(Interval[] intervals) {
Arrays.sort(intervals, new Comparator<Interval>(){
public int compare(Interval a, Interval b){
return a.start-b.start;
}
});

```
for(int i=0; i<intervals.length-1; i++){
if(intervals[i].end>intervals[i+1].start){
return false;
}
}
```
return true;
}

177 | 677



## 71 Range Addition Contents

Assume you have an array of length n initialized with all 0 ’s and are given k update
operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which incre-
ments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex

inclusive) with inc.
Return the modified array after all k operations were executed.

**71.1 Java Solution 1 - Using a heap**

public int[] getModifiedArray(int length, int[][] updates) {
int result[] = new int[length];
if(updates==null || updates.length==0)
return result;

```
//sort updates by starting index
Arrays.sort(updates, new Comparator<int[]>(){
public int compare(int[] a, int [] b){
return a[0]-b[0];
}
});
```
```
ArrayList<int[]> list = new ArrayList<int[]>();
```
```
//create a heap sorted by ending index
PriorityQueue<Integer> queue = new PriorityQueue<Integer>(new
Comparator<Integer>(){
public int compare(Integer a, Integer b){
return updates[a][1]-updates[b][1];
}
});
```
```
int sum=0;
int j=0;
for(int i=0; i<length; i++){
//substract value from sum when ending index is reached
while(!queue.isEmpty() && updates[queue.peek()][1] < i){
int top = queue.poll();
sum -= updates[top][2];
}
```
179 | 677


71 Range Addition

```
//add value to sum when starting index is reached
while(j<updates.length && updates[j][0] <= i){
sum = sum+updates[j][2];
queue.offer(j);
j++;
}
```
```
result[i]=sum;
}
```
return result;
}

Time complexity is O(nlog(n)).

**71.2 Java Solution 2**

public int[] getModifiedArray(int length, int[][] updates) {
int[] result = new int[length];
if(updates==null||updates.length==0)
return result;

```
for(int i=0; i<updates.length; i++){
result[updates[i][0]] += updates[i][2];
if(updates[i][1]<length-1){
result[updates[i][1]+1] -=updates[i][2];
}
}
```
```
int v=0;
for(int i=0; i<length; i++){
v += result[i];
result[i]=v;
}
```
return result;
}

Time complexity is O(n).

180 | 677 Program Creek


## 72 Merge K Sorted Arrays in Java

This is a classic interview question. Another similar problem is "merge k sorted lists".

This problem can be solved by using a heap. The time is O(nlog(n)).
Given m arrays, the minimum elements of all arrays can form a heap. It takes
O(log(m)) to insert an element to the heap and it takes O( 1 ) to delete the minimum

element.

class ArrayContainer implements Comparable<ArrayContainer> {
int[] arr;
int index;

```
public ArrayContainer(int[] arr, int index) {
this.arr = arr;
this.index = index;
}
```
@Override
public int compareTo(ArrayContainer o) {
return this.arr[this.index] - o.arr[o.index];
}
}

public class KSortedArray {
public static int[] mergeKSortedArray(int[][] arr) {
//PriorityQueue is heap in Java
PriorityQueue<ArrayContainer> queue = new PriorityQueue<ArrayContainer>();
int total=0;

```
//add arrays to heap
for (int i = 0; i < arr.length; i++) {
queue.add(new ArrayContainer(arr[i], 0));
total = total + arr[i].length;
}
```
```
int m=0;
int result[] = new int[total];
```
```
//while heap is not empty
while(!queue.isEmpty()){
ArrayContainer ac = queue.poll();
result[m++]=ac.arr[ac.index];
```
181 | 677


72 Merge K Sorted Arrays in Java

```
if(ac.index < ac.arr.length-1){
queue.add(new ArrayContainer(ac.arr, ac.index+1));
}
}
```
```
return result;
}
```
```
public static void main(String[] args) {
int[] arr1 = { 1, 3, 5, 7 };
int[] arr2 = { 2, 4, 6, 8 };
int[] arr3 = { 0, 9, 10, 11 };
```
int[] result = mergeKSortedArray(new int[][] { arr1, arr2, arr3 });
System.out.println(Arrays.toString(result));
}
}

182 | 677 Program Creek


## 73 Merge k Sorted Lists

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its

complexity.

**73.1 Analysis**

The simplest solution is using PriorityQueue. The elements of the priority queue
are ordered according to their natural ordering, or by a comparator provided at the

construction time (in this case).

**73.2 Java Solution**

public ListNode mergeKLists(ListNode[] lists) {
if(lists==null||lists.length==0)
return null;

```
PriorityQueue<ListNode> queue = new PriorityQueue<ListNode>(new
Comparator<ListNode>(){
public int compare(ListNode l1, ListNode l2){
return l1.val - l2.val;
}
});
```
```
ListNode head = new ListNode(0);
ListNode p = head;
```
```
for(ListNode list: lists){
if(list!=null)
queue.offer(list);
}
```
```
while(!queue.isEmpty()){
ListNode n = queue.poll();
p.next = n;
p=p.next;
```
```
if(n.next!=null)
queue.offer(n.next);
}
```
183 | 677


73 Merge k Sorted Lists

```
return head.next;
```
}

Time: log(k) * n. k is number of list and n is number of total elements.

184 | 677 Program Creek


## 74 Contains Duplicate

Given an array of integers, find if the array contains any duplicates. Your function
should return true if any value appears at least twice in the array, and it should return
false if every element is distinct.

**74.1 Java Solution**

public boolean containsDuplicate(int[] nums) {
if(nums==null || nums.length==0)
return false;

```
HashSet<Integer> set = new HashSet<Integer>();
for(int i: nums){
if(!set.add(i)){
return true;
}
}
```
return false;
}

185 | 677



## 75 Contains Duplicate II

Given an array of integers and an integer k, return true if and only if there are two

distinct indices i and j in the array such that nums[i] = nums[j] and the difference
between i and j is at most k.

**75.1 Java Solution 1**

public boolean containsNearbyDuplicate(int[] nums, int k) {
HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
int min = Integer.MAX_VALUE;

```
for(int i=0; i<nums.length; i++){
if(map.containsKey(nums[i])){
int preIndex = map.get(nums[i]);
int gap = i-preIndex;
min = Math.min(min, gap);
}
map.put(nums[i], i);
}
```
if(min <= k){
return true;
}else{
return false;
}
}

**75.2 Java Solution 2 - Simplified**

public boolean containsNearbyDuplicate(int[] nums, int k) {
HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

```
for(int i=0; i<nums.length; i++){
if(map.containsKey(nums[i])){
int pre = map.get(nums[i]);
if(i-pre<=k)
return true;
}
```
187 | 677


75 Contains Duplicate II

```
map.put(nums[i], i);
}
```
return false;
}

public boolean containsNearbyDuplicate(int[] nums, int k) {
if(nums==null || nums.length<2 || k==0)
return false;

```
int i=0;
```
```
HashSet<Integer> set = new HashSet<Integer>();
```
```
for(int j=0; j<nums.length; j++){
if(!set.add(nums[j])){
return true;
}
```
```
if(set.size()>=k+1){
set.remove(nums[i++]);
}
}
```
return false;
}

188 | 677 Program Creek


## 76 Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in
the array such that the difference between nums[i] and nums[j] is at most t and the
difference between i and j is at most k.

**76.1 Java Solution 1 - Simple**

This solution simple. Its time complexity is O(nlog(k)).

public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
if(nums==null||nums.length<2||k<0||t<0)
return false;

```
TreeSet<Long> set = new TreeSet<Long>();
for(int i=0; i<nums.length; i++){
long curr = (long) nums[i];
```
```
long leftBoundary = (long) curr-t;
long rightBoundary = (long) curr+t+1; //right boundary is exclusive, so
+1
SortedSet<Long> sub = set.subSet(leftBoundary, rightBoundary);
if(sub.size()>0)
return true;
```
```
set.add(curr);
```
```
if(i>=k){ // or if(set.size()>=k+1)
set.remove((long)nums[i-k]);
}
}
```
return false;
}

189 | 677


76 Contains Duplicate III

**76.2 Java Solution 2 - Deprecated**

public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
if (k < 1 || t < 0)
return false;

```
TreeSet<Integer> set = new TreeSet<Integer>();
```
```
for (int i = 0; i < nums.length; i++) {
int c = nums[i];
if ((set.floor(c) != null && c <= set.floor(c) + t)
|| (set.ceiling(c) != null && c >= set.ceiling(c) -t))
return true;
```
```
set.add(c);
```
```
if (i >= k)
set.remove(nums[i - k]);
}
```
return false;
}

190 | 677 Program Creek


## 77 Missing Number

Given an array containing n distinct numbers taken from 0 , 1 , 2 , ..., n, find the one that
is missing from the array. For example, given nums = [ 0 , 1 , 3 ] return 2.

**77.1 Java Solution 1 - Math**

public int missingNumber(int[] nums) {
int sum=0;
for(int i=0; i<nums.length; i++){
sum+=nums[i];
}

int n=nums.length;
return n*(n+1)/2-sum;
}

**77.2 Java Solution 2 - Bit**

public int missingNumber(int[] nums) {

```
int miss=0;
for(int i=0; i<nums.length; i++){
miss ^= (i+1) ^nums[i];
}
```
return miss;
}

**77.3 Java Solution 3 - Binary Search**

public int missingNumber(int[] nums) {
Arrays.sort(nums);
int l=0, r=nums.length;
while(l<r){
int m = (l+r)/2;
if(nums[m]>m){
r=m;

191 | 677


77 Missing Number

```
}else{
l=m+1;
}
}
```
return r;
}

192 | 677 Program Creek


## 78 Find the Duplicate Number

Given an array nums containing n + 1 integers where each integer is between 1 and n
(inclusive), prove that at least one duplicate number must exist. Assume that there is

only one duplicate number, find the duplicate one.
Note: You must not modify the array (assume the array is read only). You must use
only constant, O( 1 ) extra space. Your runtime complexity should be less than O(n 2 ).

There is only one duplicate number in the array, but it could be repeated more than
once.

**78.1 Java Solution 1 - Wrong**

This solution is wrong, but the same idea is used in Solution 3.

public int findDuplicate(int[] arr) {
for(int i=0; i<arr.length; i++){
while(arr[i]!=i+1){
if(arr[i]==arr[arr[i]-1])
return arr[i];

```
int t = arr[arr[i]-1];
arr[arr[i]-1]=arr[i];
arr[i]=t;
}
}
```
return -1;
}

**78.2 Java Solution 2 - Binary Search**

```
public int findDuplicate(int[] nums) {
int l=1,r=nums.length-1;
while(l<r){
int m=(l+r)/2;
int c=0;

for(int i: nums){
if(i<=m){
c++;

}

}

//if c < m,
if(c>m){
r=m;
}else{
l=m+1;
}
}
return r;
}
```

**78.3 Java Solution 3 - Finding Cycle**

public int findDuplicate(int[] nums) {
int slow = 0;
int fast = 0;

```
do{
slow = nums[slow];
fast = nums[nums[fast]];
} while(slow != fast);
```
```
int find = 0;
```
while(find != slow){
slow = nums[slow];
find = nums[find];
}
return find;
}

194 | 677 Program Creek


## 79 First Missing Positive

Given an unsorted integer array, find the first missing positive integer. For example,
given [ 1 , 2 , 0 ] return 3 and [ 3 , 4 ,- 1 , 1 ] return 2.
Your algorithm should run in O(n) time and uses constant space.

**79.1 Analysis**

This problem can solve by using a bucket-sort like algorithm. Let’s consider finding
first missing positive and 0 first. The key fact is that the ith element should be i, so we
have: i==A[i] A[i]==A[A[i]]

For example, given an array 1 , 2 , 0 , 4 , the algorithm does the following:

int firstMissingPositiveAnd0(int A[]) {
int n = A.length;
for (int i = 0; i < n; i++) {
// when the ith element is not i
while (A[i] != i) {
// no need to swap when ith element is out of range [0,n]
if (A[i] < 0 || A[i] >= n)
break;

```
//handle duplicate elements
if(A[i]==A[A[i]])
break;
// swap elements
int temp = A[i];
```
195 | 677


79 First Missing Positive

```
A[i] = A[temp];
A[temp] = temp;
}
}
```
```
for (int i = 0; i < n; i++) {
if (A[i] != i)
return i;
}
```
return n;
}

**79.2 Java Solution**

This problem only considers positive numbers, so we need to shift 1 offset. The ith
element is i+ 1.

public int firstMissingPositive(int[] A) {
int n = A.length;

```
for (int i = 0; i < n; i++) {
while (A[i] != i + 1) {
if (A[i] <= 0 || A[i] >= n)
break;
```
```
if(A[i]==A[A[i]-1])
break;
```
```
int temp = A[i];
A[i] = A[temp - 1];
A[temp - 1] = temp;
}
}
```
```
for (int i = 0; i < n; i++){
if (A[i] != i + 1){
return i + 1;
}
}
```
return n + 1;
}

196 | 677 Program Creek


## 80 HIndex

Given an array of citations (each citation is a non-negative integer) of a researcher,
write a function to compute the researcher’s h-index. A scientist has index h if h of
his/her N papers have at least h citations each, and the other N−h papers have no
more than h citations each.

For example, given citations = [ 3 , 0 , 6 , 1 , 5 ], which means the researcher has 5
papers in total and each of them had received 3 , 0 , 6 , 1 , 5 citations respectively. Since
the researcher has 3 papers with at least 3 citations each and the remaining two with
no more than 3 citations each, his h-index is 3.

**80.1 Java Solution**

public int hIndex(int[] citations) {
Arrays.sort(citations);

```
int result = 0;
for(int i=0; i<citations.length; i++){
int smaller = Math.min(citations[i], citations.length-i);
result = Math.max(result, smaller);
}
```
return result;
}

197 | 677



## 81 HIndex II

Follow up for H-Index: What if the citations array is sorted in ascending order? Could
you optimize your algorithm?

**81.1 Java Solution**

public int hIndex(int[] citations) {
if(citations==null || citations.length==0)
return 0;

```
int result = 0;
```
```
for(int i=0; i<citations.length; i++){
int smaller = Math.min(citations[i], citations.length-i);
result = Math.max(result, smaller);
}
```
return result;
}

199 | 677



## 82 Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the
very left of the array to the very right. You can only see the k numbers in the window.

Each time the sliding window moves right by one position.

**82.1 Java Solution**

201 | 677


82 Sliding Window Maximum

public int[] maxSlidingWindow(int[] nums, int k) {
if(nums==null||nums.length==0)
return new int[0];

```
int[] result = new int[nums.length-k+1];
```
```
LinkedList<Integer> deque = new LinkedList<Integer>();
for(int i=0; i<nums.length; i++){
if(!deque.isEmpty()&&deque.peekFirst()==i-k)
deque.poll();
```
```
while(!deque.isEmpty()&&nums[deque.peekLast()]<nums[i]){
deque.removeLast();
}
```
```
deque.offer(i);
```
```
if(i+1>=k)
result[i+1-k]=nums[deque.peek()];
}
```
return result;
}

202 | 677 Program Creek


## 83 Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of all
integers in the sliding window.

**83.1 Java Solution**

This problem is solved by using a queue.

public class MovingAverage {
LinkedList<Integer> queue;
int size;
double avg;

```
/**Initialize your data structure here. */
public MovingAverage(int size) {
this.queue = new LinkedList<Integer>();
this.size = size;
}
```
```
public double next(int val) {
if(queue.size()<this.size){
queue.offer(val);
int sum=0;
for(int i: queue){
sum+=i;
}
avg = (double)sum/queue.size();
```
return avg;
}else{
int head = queue.poll();
double minus = (double)head/this.size;
queue.offer(val);
double add = (double)val/this.size;
avg = avg + add - minus;
return avg;
}
}
}

203 | 677



## 84 Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even,
there is no middle value. So the median is the mean of the two middle value.

**84.1 Analysis**

First of all, it seems that the best time complexity we can get for this problem is
O(log(n)) of add() and O( 1 ) of getMedian(). This data structure seems highly likely to

be a tree.
We can use heap to solve this problem. In Java, the PriorityQueue class is a priority
heap. We can use two heaps to store the lower half and the higher half of the data

stream. The size of the two heaps differs at most 1.

**84.2 Java Solution**

class MedianFinder {
PriorityQueue<Integer> maxHeap;//lower half
PriorityQueue<Integer> minHeap;//higher half

```
public MedianFinder(){
maxHeap = new PriorityQueue<Integer>(Collections.reverseOrder());
minHeap = new PriorityQueue<Integer>();
}
```
205 | 677


84 Find Median from Data Stream

```
// Adds a number into the data structure.
public void addNum(int num) {
maxHeap.offer(num);
minHeap.offer(maxHeap.poll());
```
```
if(maxHeap.size() < minHeap.size()){
maxHeap.offer(minHeap.poll());
}
}
```
// Returns the median of current data stream
public double findMedian() {
if(maxHeap.size()==minHeap.size()){
return (double)(maxHeap.peek()+(minHeap.peek()))/2;
}else{
return maxHeap.peek();
}
}
}

206 | 677 Program Creek


## 85 Data Stream as Disjoint Intervals

Given a data stream input of non-negative integers a 1 , a 2 , ..., an, ..., summarize the

numbers seen so far as a list of disjoint intervals.
For example, suppose the integers from the data stream are 1 , 3 , 7 , 2 , 6 , ..., then the
summary will be:

[ 1 , 1 ] [ 1 , 1 ], [ 3 , 3 ] [ 1 , 1 ], [ 3 , 3 ], [ 7 , 7 ] [ 1 , 3 ], [ 7 , 7 ] [ 1 , 3 ], [ 6 , 7 ] Follow up: What if there
are lots of merges and the number of disjoint intervals are small compared to the data
stream’s size?

**85.1 Analysis**

We can store the interval in an array and each time iterator over the array and merge
the new value to an existing interval. This takes time O(n). If there are a lot of merges,
we want to do it in log(n).
We can solve this problem using a tree set. The floor() method returns the greatest

element in this set less than or equal to the given element, or null if there is no such
element. The higher() method returns the least element in this set strictly greater than
the given element, or null if there is no such element. Note: we use higher() instead of
ceiling() to exclude the given element.

**85.2 Java Solution**

public class SummaryRanges {

```
TreeSet<Interval> set;
```
```
/**Initialize your data structure here. */
public SummaryRanges() {
set = new TreeSet<Interval>(new Comparator<Interval>(){
public int compare(Interval a, Interval b){
return a.start-b.start;
}
});
}
```
```
public void addNum(int val) {
Interval t = new Interval(val, val);
```
```
Interval floor = set.floor(t);
```
207 | 677


85 Data Stream as Disjoint Intervals

```
if(floor!=null){
if(val<=floor.end){
return;
}else if(val == floor.end+1){
t.start = floor.start;
set.remove(floor);
}
}
```
```
Interval ceil = set.higher(t);
if(ceil!=null){
if(ceil.start==val+1){
t.end = ceil.end;
set.remove(ceil);
}
}
```
```
set.add(t);
}
```
public List<Interval> getIntervals() {
return Arrays.asList(set.toArray(new Interval[0]));
}
}

208 | 677 Program Creek


## 86 Largest Number

Given a list of non negative integers, arrange them such that they form the largest
number.
For example, given [ 3 , 30 , 34 , 5 , 9 ], the largest formed number is 9534330. (Note:
The result may be very large, so you need to return a string instead of an integer.)

**86.1 Analysis**

This problem can be solve by simply sorting strings, not sorting integer. Define a
comparator to compare strings by concat() right-to-left or left-to-right.

**86.2 Java Solution**

public String largestNumber(int[] nums) {
String[] strs = new String[nums.length];
for(int i=0; i<nums.length; i++){
strs[i] = String.valueOf(nums[i]);
}

```
Arrays.sort(strs, new Comparator<String>(){
public int compare(String s1, String s2){
String leftRight = s1+s2;
String rightLeft = s2+s1;
return -leftRight.compareTo(rightLeft);
```
```
}
});
```
```
StringBuilder sb = new StringBuilder();
for(String s: strs){
sb.append(s);
}
```
```
while(sb.charAt(0)==’0’ && sb.length()>1){
sb.deleteCharAt(0);
}
```
return sb.toString();
}

209 | 677



## 87 Sort List

LeetCode - Sort List:
Sort a linked list in O(n log n) time using constant space complexity.

**87.1 Keys for solving the problem**

- Break the list to two in the middle
- Recursively sort the two sub lists
- Merge the two sub lists

This is my accepted answer for the problem.

package algorithm.sort;

class ListNode {
int val;
ListNode next;

ListNode(int x) {
val = x;
next = null;
}
}

public class SortLinkedList {

```
// merge sort
public static ListNode mergeSortList(ListNode head) {
```
```
if (head == null || head.next == null)
return head;
```
```
// count total number of elements
int count = 0;
ListNode p = head;
while (p != null) {
count++;
p = p.next;
}
```
```
// break up to two list
int middle = count / 2;
```
211 | 677


87 Sort List

```
ListNode l = head, r = null;
ListNode p2 = head;
int countHalf = 0;
while (p2 != null) {
countHalf++;
ListNode next = p2.next;
```
```
if (countHalf == middle) {
p2.next = null;
r = next;
}
p2 = next;
}
```
```
// now we have two parts l and r, recursively sort them
ListNode h1 = mergeSortList(l);
ListNode h2 = mergeSortList(r);
```
```
// merge together
ListNode merged = merge(h1, h2);
```
```
return merged;
}
```
```
public static ListNode merge(ListNode l, ListNode r) {
ListNode p1 = l;
ListNode p2 = r;
```
```
ListNode fakeHead = new ListNode(100);
ListNode pNew = fakeHead;
```
```
while (p1 != null || p2 != null) {
```
```
if (p1 == null) {
pNew.next = new ListNode(p2.val);
p2 = p2.next;
pNew = pNew.next;
} else if (p2 == null) {
pNew.next = new ListNode(p1.val);
p1 = p1.next;
pNew = pNew.next;
} else {
if (p1.val < p2.val) {
// if(fakeHead)
pNew.next = new ListNode(p1.val);
p1 = p1.next;
pNew = pNew.next;
} else if (p1.val == p2.val) {
pNew.next = new ListNode(p1.val);
```
212 | 677 Program Creek


```
87 Sort List
```
```
pNew.next.next = new ListNode(p1.val);
pNew = pNew.next.next;
p1 = p1.next;
p2 = p2.next;
```
```
} else {
pNew.next = new ListNode(p2.val);
p2 = p2.next;
pNew = pNew.next;
}
}
}
```
```
// printList(fakeHead.next);
return fakeHead.next;
}
```
```
public static void main(String[] args) {
ListNode n1 = new ListNode(2);
ListNode n2 = new ListNode(3);
ListNode n3 = new ListNode(4);
```
```
ListNode n4 = new ListNode(3);
ListNode n5 = new ListNode(4);
ListNode n6 = new ListNode(5);
```
```
n1.next = n2;
n2.next = n3;
n3.next = n4;
n4.next = n5;
n5.next = n6;
```
```
n1 = mergeSortList(n1);
```
```
printList(n1);
}
```
```
public static void printList(ListNode x) {
if(x != null){
System.out.print(x.val + " ");
while (x.next != null) {
System.out.print(x.next.val + " ");
x = x.next;
}
System.out.println();
}
```
}
}

Program Creek 213 | 677


87 Sort List

```
Output:
2 3 3 4 4 5
```
214 | 677 Program Creek


## 88 Quicksort Array in Java

Quicksort is a divide and conquer algorithm. It first divides a large list into two
smaller sub-lists and then recursively sort the two sub-lists. If we want to sort an array
without any extra space, quicksort is a good option. On average, time complexity is
O(n log(n)).

The basic step of sorting an array are as follows:

- Select a pivot, normally the middle one
- From both ends, swap elements and make all elements on the left less than the
    pivot and all elements on the right greater than the pivot
- Recursively sort left part and right part

Here is a very good animation of quicksort.

public class QuickSort {
public static void main(String[] args) {
int[] x = { 9, 2, 4, 7, 3, 7, 10 };
System.out.println(Arrays.toString(x));

```
int low = 0;
int high = x.length - 1;
```
```
quickSort(x, low, high);
System.out.println(Arrays.toString(x));
}
```
```
public static void quickSort(int[] arr, int low, int high) {
if (arr == null || arr.length == 0)
return;
```
```
if (low >= high)
return;
```
```
// pick the pivot
int middle = low + (high - low) / 2;
int pivot = arr[middle];
```
```
// make left < pivot and right > pivot
int i = low, j = high;
while (i <= j) {
while (arr[i] < pivot) {
i++;
}
```
215 | 677


88 Quicksort Array in Java

```
while (arr[j] > pivot) {
j--;
}
```
```
if (i <= j) {
int temp = arr[i];
arr[i] = arr[j];
arr[j] = temp;
i++;
j--;
}
}
```
```
// recursively sort two sub parts
if (low < j)
quickSort(arr, low, j);
```
if (high > i)
quickSort(arr, i, high);
}
}

```
Output:
9 2 4 7 3 7 10 2 3 4 7 7 9 10
```
216 | 677 Program Creek


## 89 Solution Sort a linked list using insertion sort in Java

Insertion Sort List:
Sort a linked list using insertion sort.
This is my accepted answer for LeetCode problem - Sort a linked list using insertion
sort in Java. It is a complete program.
Before coding for that, here is an example of insertion sort from wiki. You can get

an idea of what is insertion sort.

Code:

package algorithm.sort;

class ListNode {
int val;
ListNode next;

ListNode(int x) {
val = x;
next = null;
}
}

public class SortLinkedList {
public static ListNode insertionSortList(ListNode head) {

217 | 677


89 Solution Sort a linked list using insertion sort in Java

```
if (head == null || head.next == null)
return head;
```
```
ListNode newHead = new ListNode(head.val);
ListNode pointer = head.next;
```
```
// loop through each element in the list
while (pointer != null) {
// insert this element to the new list
```
```
ListNode innerPointer = newHead;
ListNode next = pointer.next;
```
```
if (pointer.val <= newHead.val) {
ListNode oldHead = newHead;
newHead = pointer;
newHead.next = oldHead;
} else {
while (innerPointer.next != null) {
```
```
if (pointer.val > innerPointer.val && pointer.val <=
innerPointer.next.val) {
ListNode oldNext = innerPointer.next;
innerPointer.next = pointer;
pointer.next = oldNext;
}
```
```
innerPointer = innerPointer.next;
}
```
```
if (innerPointer.next == null && pointer.val > innerPointer.val) {
innerPointer.next = pointer;
pointer.next = null;
}
}
```
```
// finally
pointer = next;
}
```
```
return newHead;
}
```
```
public static void main(String[] args) {
ListNode n1 = new ListNode(2);
ListNode n2 = new ListNode(3);
ListNode n3 = new ListNode(4);
```
```
ListNode n4 = new ListNode(3);
ListNode n5 = new ListNode(4);
```
218 | 677 Program Creek


```
89 Solution Sort a linked list using insertion sort in Java
```
```
ListNode n6 = new ListNode(5);
```
```
n1.next = n2;
n2.next = n3;
n3.next = n4;
n4.next = n5;
n5.next = n6;
```
```
n1 = insertionSortList(n1);
```
```
printList(n1);
```
```
}
```
```
public static void printList(ListNode x) {
if(x != null){
System.out.print(x.val + " ");
while (x.next != null) {
System.out.print(x.next.val + " ");
x = x.next;
}
System.out.println();
}
```
}
}

```
Output:
2 3 3 4 4 5
```
Program Creek 219 | 677


