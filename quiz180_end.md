# Coding Interview in Java

August 1 st, 2016

## 180 Search a 2D Matrix

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix
has properties:
1 ) Integers in each row are sorted from left to right. 2 ) The first integer of each row

is greater than the last integer of the previous row.
For example, consider the following matrix:

[
[1, 3, 5, 7],
[10, 11, 16, 20],
[23, 30, 34, 50]
]

Given target = 3 , return true.

**180.1 Java Solution**

This is a typical problem of binary search.

You may try to solve this problem by finding the row first and then the column.
There is no need to do that. Because of the matrix’s special features, the matrix can be
considered as a sorted array. Your goal is to find one element in this sorted array by
using binary search.

public class Solution {
public boolean searchMatrix(int[][] matrix, int target) {
if(matrix==null || matrix.length==0 || matrix[0].length==0)
return false;

```
int m = matrix.length;
int n = matrix[0].length;
```
```
int start = 0;
int end = m*n-1;
```
```
while(start<=end){
int mid=(start+end)/2;
int midX=mid/n;
int midY=mid%n;
```
```
if(matrix[midX][midY]==target)
return true;
```
439 | 677


180 Search a 2D Matrix

```
if(matrix[midX][midY]<target){
start=mid+1;
}else{
end=mid-1;
}
}
```
return false;
}
}

440 | 677 Program Creek


## 181 Search a 2D Matrix II

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix
has the following properties:

Integers in each row are sorted in ascending from left to right. Integers in each
column are sorted in ascending from top to bottom.

For example, consider the following matrix:

[
[1, 4, 7, 11, 15],
[2, 5, 8, 12, 19],
[3, 6, 9, 16, 22],
[10, 13, 14, 17, 24],
[18, 21, 23, 26, 30]
]

Given target = 5 , return true.

**181.1 Java Solution 1**

In a naive approach, we can use the matrix boundary to reduce the search space. Here

is a simple recursive implementation.

public boolean searchMatrix(int[][] matrix, int target) {
int i1=0;
int i2=matrix.length-1;
int j1=0;
int j2=matrix[0].length-1;

return helper(matrix, i1, i2, j1, j2, target);
}

public boolean helper(int[][] matrix, int i1, int i2, int j1, int j2, int
target){

```
if(i1>i2||j1>j2)
return false;
```
```
for(int j=j1;j<=j2;j++){
if(target < matrix[i1][j]){
return helper(matrix, i1, i2, j1, j-1, target);
}else if(target == matrix[i1][j]){
return true;
```
441 | 677


181 Search a 2D Matrix II

### }

### }

```
for(int i=i1;i<=i2;i++){
if(target < matrix[i][j1]){
return helper(matrix, i1, i-1, j1, j2, target);
}else if(target == matrix[i][j1]){
return true;
}
}
```
```
for(int j=j1;j<=j2;j++){
if(target > matrix[i2][j]){
return helper(matrix, i1, i2, j+1, j2, target);
}else if(target == matrix[i2][j]){
return true;
}
}
```
```
for(int i=i1;i<=i2;i++){
if(target > matrix[i][j2]){
return helper(matrix, i1, i+1, j1, j2, target);
}else if(target == matrix[i][j2]){
return true;
}
}
```
return false;
}

**181.2 Java Solution 2**

Time Complexity: O(m + n)

public boolean searchMatrix(int[][] matrix, int target) {
int m=matrix.length-1;
int n=matrix[0].length-1;

```
int i=m;
int j=0;
```
```
while(i>=0 && j<=n){
if(target < matrix[i][j]){
i--;
}else if(target > matrix[i][j]){
j++;
}else{
return true;
```
442 | 677 Program Creek


```
181 Search a 2D Matrix II
```
### }

### }

return false;
}

Program Creek 443 | 677



## 182 Set Matrix Zeroes

Given a m * n matrix, if an element is 0 , set its entire row and column to 0. Do it in
place.

**182.1 Analysis**

This problem should be solved in place, i.e., no other array should be used. We can
use the first column and the first row to track if a row/column should be set to 0.

Since we used the first row and first column to mark the zero row/column, the
original values are changed.

Step 1 : First row contains zero = true; First column contains zero = false;

445 | 677


182 Set Matrix Zeroes

**182.2 Java Solution**

public class Solution {
public void setZeroes(int[][] matrix) {
boolean firstRowZero = false;
boolean firstColumnZero = false;

```
//set first row and column zero or not
for(int i=0; i<matrix.length; i++){
if(matrix[i][0] == 0){
firstColumnZero = true;
break;
}
}
```
```
for(int i=0; i<matrix[0].length; i++){
if(matrix[0][i] == 0){
firstRowZero = true;
break;
}
}
```
446 | 677 Program Creek


```
182 Set Matrix Zeroes
```
```
//mark zeros on first row and column
for(int i=1; i<matrix.length; i++){
for(int j=1; j<matrix[0].length; j++){
if(matrix[i][j] == 0){
matrix[i][0] = 0;
matrix[0][j] = 0;
}
}
}
```
```
//use mark to set elements
for(int i=1; i<matrix.length; i++){
for(int j=1; j<matrix[0].length; j++){
if(matrix[i][0] == 0 || matrix[0][j] == 0){
matrix[i][j] = 0;
}
}
}
```
```
//set first column and row
if(firstColumnZero){
for(int i=0; i<matrix.length; i++)
matrix[i][0] = 0;
}
```
```
if(firstRowZero){
for(int i=0; i<matrix[0].length; i++)
matrix[0][i] = 0;
}
```
}
}

Program Creek 447 | 677



## 183 Spiral Matrix

Given a matrix of m x n elements (m rows, n columns), return all elements of the
matrix in spiral order.

For example, given the following matrix:

[
[ 1, 2, 3 ],
[ 4, 5, 6 ],
[ 7, 8, 9 ]
]

You should return [ 1 , 2 , 3 , 6 , 9 , 8 , 7 , 4 , 5 ].

**183.1 Java Solution 1**

If more than one row and column left, it can form a circle and we process the circle.
Otherwise, if only one row or column left, we process that column or row ONLY.

public class Solution {
public ArrayList<Integer> spiralOrder(int[][] matrix) {
ArrayList<Integer> result = new ArrayList<Integer>();

```
if(matrix == null || matrix.length == 0) return result;
```
```
int m = matrix.length;
int n = matrix[0].length;
```
```
int x=0;
int y=0;
```
```
while(m>0 && n>0){
```
```
//if one row/column left, no circle can be formed
if(m==1){
for(int i=0; i<n; i++){
result.add(matrix[x][y++]);
}
break;
}else if(n==1){
for(int i=0; i<m; i++){
result.add(matrix[x++][y]);
}
```
449 | 677


183 Spiral Matrix

```
break;
}
```
```
//below, process a circle
```
```
//top - move right
for(int i=0;i<n-1;i++){
result.add(matrix[x][y++]);
}
```
```
//right - move down
for(int i=0;i<m-1;i++){
result.add(matrix[x++][y]);
}
```
```
//bottom - move left
for(int i=0;i<n-1;i++){
result.add(matrix[x][y--]);
}
```
```
//left - move up
for(int i=0;i<m-1;i++){
result.add(matrix[x--][y]);
}
```
```
x++;
y++;
m=m-2;
n=n-2;
}
```
return result;
}
}

Similarly, we can write the solution this way:

public List<Integer> spiralOrder(int[][] matrix) {
List<Integer> result = new ArrayList<Integer>();
if(matrix==null||matrix.length==0||matrix[0].length==0)
return result;

```
int m = matrix.length;
int n = matrix[0].length;
```
```
int left=0;
int right=n-1;
int top = 0;
int bottom = m-1;
```
450 | 677 Program Creek


```
183 Spiral Matrix
```
```
while(result.size()<m*n){
for(int j=left; j<=right; j++){
result.add(matrix[top][j]);
}
top++;
```
```
for(int i=top; i<=bottom; i++){
result.add(matrix[i][right]);
}
right--;
```
```
//prevent duplicate row
if(bottom<top)
break;
```
```
for(int j=right; j>=left; j--){
result.add(matrix[bottom][j]);
}
bottom--;
```
```
// prevent duplicate column
if(right<left)
break;
```
```
for(int i=bottom; i>=top; i--){
result.add(matrix[i][left]);
}
left++;
}
```
return result;
}

**183.2 Java Solution 2**

We can also recursively solve this problem. The solution’s performance is not better
than Solution 1. Therefore, Solution 1 should be preferred.

public class Solution {
public ArrayList<Integer> spiralOrder(int[][] matrix) {
if(matrix==null || matrix.length==0)
return new ArrayList<Integer>();

```
return spiralOrder(matrix,0,0,matrix.length,matrix[0].length);
}
```
```
public ArrayList<Integer> spiralOrder(int [][] matrix, int x, int y, int
```
Program Creek 451 | 677


183 Spiral Matrix

```
m, int n){
ArrayList<Integer> result = new ArrayList<Integer>();
```
```
if(m<=0||n<=0)
return result;
```
```
//only one element left
if(m==1&&n==1) {
result.add(matrix[x][y]);
return result;
}
```
```
//top - move right
for(int i=0;i<n-1;i++){
result.add(matrix[x][y++]);
}
```
```
//right - move down
for(int i=0;i<m-1;i++){
result.add(matrix[x++][y]);
}
```
```
//bottom - move left
if(m>1){
for(int i=0;i<n-1;i++){
result.add(matrix[x][y--]);
}
}
```
```
//left - move up
if(n>1){
for(int i=0;i<m-1;i++){
result.add(matrix[x--][y]);
}
}
```
```
if(m==1||n==1)
result.addAll(spiralOrder(matrix, x, y, 1, 1));
else
result.addAll(spiralOrder(matrix, x+1, y+1, m-2, n-2));
```
return result;
}
}

452 | 677 Program Creek


## 184 Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n 2 in spiral
order. For example, given n = 4 ,

[
[1, 2, 3, 4],
[12, 13, 14, 5],
[11, 16, 15, 6],
[10, 9, 8, 7]
]

**184.1 Java Solution 1**

public int[][] generateMatrix(int n) {
int total = n*n;
int[][] result= new int[n][n];

```
int x=0;
int y=0;
int step = 0;
```
```
for(int i=0;i<total;){
while(y+step<n){
i++;
result[x][y]=i;
y++;
```
```
}
y--;
x++;
```
```
while(x+step<n){
i++;
result[x][y]=i;
x++;
}
x--;
y--;
```
```
while(y>=0+step){
i++;
```
453 | 677


184 Spiral Matrix II

```
result[x][y]=i;
y--;
}
y++;
x--;
step++;
```
```
while(x>=0+step){
i++;
result[x][y]=i;
x--;
}
x++;
y++;
}
```
return result;
}

**184.2 Java Solution 2**

public int[][] generateMatrix(int n) {
int[][] result = new int[n][n];

```
int k=1;
int top=0;
int bottom=n-1;
int left=0;
int right=n-1;
```
```
while(k<=n*n){
for(int i=left; i<=right; i++){
result[top][i]=k;
k++;
}
top++;
```
```
for(int i=top; i<=bottom; i++){
result[i][right]=k;
k++;
}
right--;
```
```
for(int i=right; i>=left; i--){
result[bottom][i]=k;
k++;
}
```
454 | 677 Program Creek


```
184 Spiral Matrix II
```
```
bottom--;
```
```
for(int i=bottom; i>=top; i--){
result[i][left] = k;
k++;
}
left++;
}
```
return result;
}

Program Creek 455 | 677



## 185 Rotate Image

You are given an n x n 2 D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Follow up: Could you do this in-place?

**185.1 In-place Solution**

By using the relation "matrix[i][j] = matrix[n- 1 -j][i]", we can loop through the matrix.

public void rotate(int[][] matrix) {
int n = matrix.length;
for (int i = 0; i < n / 2; i++) {
for (int j = 0; j < Math.ceil(((double) n) / 2.); j++) {
int temp = matrix[i][j];
matrix[i][j] = matrix[n-1-j][i];
matrix[n-1-j][i] = matrix[n-1-i][n-1-j];
matrix[n-1-i][n-1-j] = matrix[j][n-1-i];
matrix[j][n-1-i] = temp;
}
}
}

457 | 677



## 186 Valid Sudoku

Determine if a Sudoku is valid. The Sudoku board could be partially filled, where
empty cells are filled with the character ’.’.

**186.1 Java Solution**

public boolean isValidSudoku(char[][] board) {
if (board == null || board.length != 9 || board[0].length != 9)
return false;
// check each column
for (int i = 0; i < 9; i++) {
boolean[] m = new boolean[9];
for (int j = 0; j < 9; j++) {
if (board[i][j] != ’.’) {
if (m[(int) (board[i][j] - ’1’)]) {
return false;
}
m[(int) (board[i][j] - ’1’)] = true;
}
}
}

```
//check each row
for (int j = 0; j < 9; j++) {
boolean[] m = new boolean[9];
for (int i = 0; i < 9; i++) {
```
459 | 677


186 Valid Sudoku

```
if (board[i][j] != ’.’) {
if (m[(int) (board[i][j] - ’1’)]) {
return false;
}
m[(int) (board[i][j] - ’1’)] = true;
}
}
}
```
```
//check each 3*3 matrix
for (int block = 0; block < 9; block++) {
boolean[] m = new boolean[9];
for (int i = block / 3* 3; i < block / 3* 3 + 3; i++) {
for (int j = block % 3* 3; j < block % 3* 3 + 3; j++) {
if (board[i][j] != ’.’) {
if (m[(int) (board[i][j] - ’1’)]) {
return false;
}
m[(int) (board[i][j] - ’1’)] = true;
}
}
}
}
```
return true;
}

460 | 677 Program Creek


## 187 Unique Paths II

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths
would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid. For
example, there is one obstacle in the middle of a 3 x 3 grid as illustrated below,

[
[0,0,0],
[0,1,0],
[0,0,0]
]

the total number of unique paths is 2.

**187.1 Java Solution**

public int uniquePathsWithObstacles(int[][] obstacleGrid) {
if(obstacleGrid==null||obstacleGrid.length==0)
return 0;

```
int m = obstacleGrid.length;
int n = obstacleGrid[0].length;
```
```
if(obstacleGrid[0][0]==1||obstacleGrid[m-1][n-1]==1)
return 0;
```
```
int[][] dp = new int[m][n];
dp[0][0]=1;
```
```
//left column
for(int i=1; i<m; i++){
if(obstacleGrid[i][0]==1){
dp[i][0] = 0;
}else{
dp[i][0] = dp[i-1][0];
}
}
```
```
//top row
```
461 | 677


187 Unique Paths II

```
for(int i=1; i<n; i++){
if(obstacleGrid[0][i]==1){
dp[0][i] = 0;
}else{
dp[0][i] = dp[0][i-1];
}
}
```
```
//fill up cells inside
for(int i=1; i<m; i++){
for(int j=1; j<n; j++){
if(obstacleGrid[i][j]==1){
dp[i][j]=0;
}else{
dp[i][j]=dp[i-1][j]+dp[i][j-1];
}
```
```
}
}
```
return dp[m-1][n-1];
}

462 | 677 Program Creek


## 188 Number of Islands

Given a 2 -d grid map of ’ 1 ’s (land) and ’ 0 ’s (water), count the number of islands. An
island is surrounded by water and is formed by connecting adjacent lands horizontally

or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1 :

11110
11010
11000
00000

Answer: 1

**188.1 Java Solution 1 - DFS**

The basic idea of the following solution is merging adjacent lands, and the merging
should be done recursively.

Each element is visited once only. So time is O(m*n).

public int numIslands(char[][] grid) {
if(grid==null || grid.length==0||grid[0].length==0)
return 0;

```
int m = grid.length;
int n = grid[0].length;
```
```
int count=0;
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
if(grid[i][j]==’1’){
count++;
merge(grid, i, j);
}
}
}
```
return count;
}

public void merge(char[][] grid, int i, int j){
int m=grid.length;
int n=grid[0].length;

463 | 677


188 Number of Islands

```
if(i<0||i>=m||j<0||j>=n||grid[i][j]!=’1’)
return;
```
```
grid[i][j]=’X’;
```
merge(grid, i-1, j);
merge(grid, i+1, j);
merge(grid, i, j-1);
merge(grid, i, j+1);
}

**188.2 Java Solution 2 - Union-Find**

Time is O(m*n*log(k)).

public int numIslands(char[][] grid) {
if(grid==null || grid.length==0 || grid[0].length==0)
return 0;

```
int m = grid.length;
int n = grid[0].length;
```
```
int[] dx={-1, 1, 0, 0};
int[] dy={0, 0, -1, 1};
```
```
int[] root = new int[m*n];
```
```
int count=0;
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
if(grid[i][j]==’1’){
root[i*n+j] = i*n+j;
count++;
}
}
}
```
```
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
if(grid[i][j]==’1’){
for(int k=0; k<4; k++){
int x = i+dx[k];
int y = j+dy[k];
```
```
if(x>=0&&x<m&&y>=0&&y<n&&grid[x][y]==’1’){
int cRoot = getRoot(root, i*n+j);
int nRoot = getRoot(root, x*n+y);
```
464 | 677 Program Creek


```
188 Number of Islands
```
```
if(nRoot!=cRoot){
root[cRoot]=nRoot; //update previous node’s root to be
current
count--;
} } } } } }
```
return count;
}

public int getRoot(int[] arr , int i){
while(arr[i]!=i){
i = arr[arr[i]];
}

return i;
}

Check out Number of Island II.

Program Creek 465 | 677



## 189 Number of Islands II

A 2 d grid map of m rows and n columns is initially filled with water. We may perform
an addLand operation which turns the water at position (row, col) into a land. Given a
list of positions to operate, count the number of islands after each addLand operation.
An island is surrounded by water and is formed by connecting adjacent lands hori-

zontally or vertically. You may assume all four edges of the grid are all surrounded by
water.

**189.1 Java Solution**

Use an array to track the parent node for each cell.

public List<Integer> numIslands2(int m, int n, int[][] positions) {
int[] rootArray = new int[m*n];
Arrays.fill(rootArray,-1);

```
ArrayList<Integer> result = new ArrayList<Integer>();
```
```
int[][] directions = {{-1,0},{0,1},{1,0},{0,-1}};
int count=0;
```
```
for(int k=0; k<positions.length; k++){
count++;
```
```
int[] p = positions[k];
int index = p[0]*n+p[1];
rootArray[index]=index;//set root to be itself for each node
```
```
for(int r=0;r<4;r++){
int i=p[0]+directions[r][0];
int j=p[1]+directions[r][1];
```
```
if(i>=0&&j>=0&&i<m&&j<n&&rootArray[i*n+j]!=-1){
//get neighbor’s root
int thisRoot = getRoot(rootArray, i*n+j);
if(thisRoot!=index){
rootArray[thisRoot]=index;//set previous root’s root
count--;
}
}
}
```
467 | 677


189 Number of Islands II

```
result.add(count);
}
```
return result;
}

public int getRoot(int[] arr, int i){
while(i!=arr[i]){
i=arr[i];
}
return i;
}

468 | 677 Program Creek


## 190 Number of Connected Components in an Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a
pair of nodes), write a function to find the number of connected components in an

undirected graph.
Example 1 :0 3| | 1 —2 4Given n = 5 and edges = [[ 0 , 1 ], [ 1 , 2 ], [ 3 , 4 ]], return 2.

**190.1 Java Solution - Union-find**

This problem can be solved by using union-find beautifully. Initially, there are n nodes.
The nodes that are involved in each edge is merged.

There are k loops and each loop processing the root array costs log(n). Therefore,
time complexity is O(k*log(n)).

public int countComponents(int n, int[][] edges) {
int count = n;

```
int[] root = new int[n];
// initialize each node is an island
for(int i=0; i<n; i++){
root[i]=i;
}
```
```
for(int i=0; i<edges.length; i++){
int x = edges[i][0];
int y = edges[i][1];
```
```
int xRoot = getRoot(root, x);
int yRoot = getRoot(root, y);
```
```
if(xRoot!=yRoot){
count--;
root[xRoot]=yRoot;
}
```
```
}
```
return count;
}

public int getRoot(int[] arr, int i){

469 | 677


190 Number of Connected Components in an Undirected Graph

while(arr[i]!=i){
arr[i]= arr[arr[i]];
i=arr[i];
}
return i;
}

470 | 677 Program Creek


## 191 Surrounded Regions

Given a 2 D board containing ’X’ and ’O’, capture all regions surrounded by ’X’. A
region is captured by flipping all ’O’s into ’X’s in that surrounded region.
For example,

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

**191.1 Analysis**

This problem is similar to Number of Islands. In this problem, only the cells on the
boarders can not be surrounded. So we can first merge those O’s on the boarders like

in Number of Islands and replace O’s with ’#’, and then scan the board and replace all
O’s left (if any).

**191.2 Depth-first Search**

public void solve(char[][] board) {
if(board == null || board.length==0)
return;

```
int m = board.length;
int n = board[0].length;
```
```
//merge O’s on left & right boarder
for(int i=0;i<m;i++){
if(board[i][0] == ’O’){
merge(board, i, 0);
}
```
```
if(board[i][n-1] == ’O’){
```
471 | 677


191 Surrounded Regions

```
merge(board, i,n-1);
}
}
```
```
//merge O’s on top & bottom boarder
for(int j=0; j<n; j++){
if(board[0][j] == ’O’){
merge(board, 0,j);
}
```
```
if(board[m-1][j] == ’O’){
merge(board, m-1,j);
}
}
```
//process the board
for(int i=0;i<m;i++){
for(int j=0; j<n; j++){
if(board[i][j] == ’O’){
board[i][j] = ’X’;
}else if(board[i][j] == ’#’){
board[i][j] = ’O’;
}
}
}
}

public void merge(char[][] board, int i, int j){
if(i<0 || i>=board.length || j<0 || j>=board[0].length)
return;

```
if(board[i][j] != ’O’)
return;
```
```
board[i][j] = ’#’;
```
merge(board, i-1, j);
merge(board, i+1, j);
merge(board, i, j-1);
merge(board, i, j+1);
}

This solution causes java.lang.StackOverflowError, because for a large board, too
many method calls are pushed to the stack and causes the overflow.

**191.3 Breath-first Search**

We can also use a queue to do breath-first search for this problem.

472 | 677 Program Creek


```
191 Surrounded Regions
```
public void solve(char[][] board) {
if(board==null || board.length==0 || board[0].length==0)
return;

```
int m=board.length;
int n=board[0].length;
```
```
for(int j=0; j<n; j++){
if(board[0][j]==’O’){
bfs(board, 0, j);
}
}
```
```
for(int j=0; j<n; j++){
if(board[m-1][j]==’O’){
bfs(board, m-1, j);
}
}
```
```
for(int i=0; i<m; i++){
if(board[i][0]==’O’){
bfs(board, i, 0);
}
}
```
```
for(int i=0; i<m; i++){
if(board[i][n-1]==’O’){
bfs(board, i, n-1);
}
}
```
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
if(board[i][j]==’O’){
board[i][j]=’X’;
}
if(board[i][j]==’1’){
board[i][j]=’O’;
}
}
}
}

public void bfs(char[][] board, int o, int p){
int m=board.length;
int n=board[0].length;

```
int index = o*n+p;
LinkedList<Integer> queue = new LinkedList<Integer>();
```
Program Creek 473 | 677


191 Surrounded Regions

```
queue.offer(index);
board[o][p]=’1’;
```
```
while(!queue.isEmpty()){
int top = queue.poll();
int i=top/n;
int j=top%n;
```
if(i-1>=0 && board[i-1][j]==’O’){
board[i-1][j]=’1’;
queue.offer((i-1)*n+j);
}
if(i+1<m && board[i+1][j]==’O’){
board[i+1][j]=’1’;
queue.offer((i+1)*n+j);
}
if(j-1>=0 && board[i][j-1]==’O’){
board[i][j-1]=’1’;
queue.offer(i*n+j-1);
}
if(j+1<n && board[i][j+1]==’O’){
board[i][j+1]=’1’;
queue.offer(i*n+j+1);
}
}
}

474 | 677 Program Creek


## 192 Maximal Square

Given a 2 D binary matrix filled with 0 ’s and 1 ’s, find the largest square containing all

1 ’s and return its area.
For example, given the following matrix:

1101
1101
1111

Return 4.

**192.1 Analysis**

This problem can be solved by dynamic programming. The changing condition is:
t[i][j] = min(t[i][j- 1 ], t[i- 1 ][j], t[i- 1 ][j- 1 ]) + 1. It means the square formed before this

point.

**192.2 Java Solution**

public int maximalSquare(char[][] matrix) {
if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
return 0;

```
int m = matrix.length;
int n = matrix[0].length;
```
```
int[][] t = new int[m][n];
```
```
//top row
for (int i = 0; i < m; i++) {
t[i][0] = Character.getNumericValue(matrix[i][0]);
}
```
```
//left column
for (int j = 0; j < n; j++) {
t[0][j] = Character.getNumericValue(matrix[0][j]);
}
```
```
//cells inside
for (int i = 1; i < m; i++) {
```
475 | 677


192 Maximal Square

```
for (int j = 1; j < n; j++) {
if (matrix[i][j] == ’1’) {
int min = Math.min(t[i - 1][j], t[i - 1][j - 1]);
min = Math.min(min,t[i][j - 1]);
t[i][j] = min + 1;
} else {
t[i][j] = 0;
}
}
}
```
```
int max = 0;
//get maximal length
for (int i = 0; i < m; i++) {
for (int j = 0; j < n; j++) {
if (t[i][j] > max) {
max = t[i][j];
}
}
}
```
return max* max;
}

476 | 677 Program Creek


## 193 Word Search

Given a 2 D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "ad-

jacent" cells are those horizontally or vertically neighboring. The same letter cell may
not be used more than once.

For example, given board =

[
["ABCE"],
["SFCS"],
["ADEE"]
]

word = "ABCCED", ->returns true, word = "SEE", ->returns true, word = "ABCB",
->returns false.

**193.1 Analysis**

This problem can be solve by using a typical DFS method.

**193.2 Java Solution**

public boolean exist(char[][] board, String word) {
int m = board.length;
int n = board[0].length;

```
boolean result = false;
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
if(dfs(board,word,i,j,0)){
result = true;
}
}
}
```
return result;
}

public boolean dfs(char[][] board, String word, int i, int j, int k){
int m = board.length;

477 | 677


193 Word Search

```
int n = board[0].length;
```
```
if(i<0 || j<0 || i>=m || j>=n){
return false;
}
```
```
if(board[i][j] == word.charAt(k)){
char temp = board[i][j];
board[i][j]=’#’;
if(k==word.length()-1){
return true;
}else if(dfs(board, word, i-1, j, k+1)
||dfs(board, word, i+1, j, k+1)
||dfs(board, word, i, j-1, k+1)
||dfs(board, word, i, j+1, k+1)){
return true;
}
board[i][j]=temp;
}
```
return false;
}

478 | 677 Program Creek


## 194 Word Search II

Given a 2 D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same letter cell
may not be used more than once in a word.

For example, given words = ["oath","pea","eat","rain"] and board =

[
[’o’,’a’,’a’,’n’],
[’e’,’t’,’a’,’e’],
[’i’,’h’,’k’,’r’],
[’i’,’f’,’l’,’v’]
]

Return ["eat","oath"].

**194.1 Java Solution 1**

Similar to Word Search, this problem can be solved by DFS. However, this solution
exceeds time limit.

public List<String> findWords(char[][] board, String[] words) {
ArrayList<String> result = new ArrayList<String>();

```
int m = board.length;
int n = board[0].length;
```
```
for (String word : words) {
boolean flag = false;
for (int i = 0; i < m; i++) {
for (int j = 0; j < n; j++) {
char[][] newBoard = new char[m][n];
for (int x = 0; x < m; x++)
for (int y = 0; y < n; y++)
newBoard[x][y] = board[x][y];
```
```
if (dfs(newBoard, word, i, j, 0)) {
flag = true;
}
}
}
if (flag) {
```
479 | 677


194 Word Search II

```
result.add(word);
}
}
```
return result;
}

public boolean dfs(char[][] board, String word, int i, int j, int k) {
int m = board.length;
int n = board[0].length;

```
if (i < 0 || j < 0 || i >= m || j >= n || k > word.length() - 1) {
return false;
}
```
```
if (board[i][j] == word.charAt(k)) {
char temp = board[i][j];
board[i][j] = ’#’;
```
```
if (k == word.length() - 1) {
return true;
} else if (dfs(board, word, i - 1, j, k + 1)
|| dfs(board, word, i + 1, j, k + 1)
|| dfs(board, word, i, j - 1, k + 1)
|| dfs(board, word, i, j + 1, k + 1)) {
board[i][j] = temp;
return true;
}
```
```
} else {
return false;
}
```
return false;
}

**194.2 Java Solution 2 - Trie**

If the current candidate does not exist in all words’ prefix, we can stop backtracking
immediately. This can be done by using a trie structure.

public class Solution {
Set<String> result = new HashSet<String>();

```
public List<String> findWords(char[][] board, String[] words) {
//HashSet<String> result = new HashSet<String>();
```
```
Trie trie = new Trie();
```
480 | 677 Program Creek


```
194 Word Search II
```
```
for(String word: words){
trie.insert(word);
}
```
```
int m=board.length;
int n=board[0].length;
```
```
boolean[][] visited = new boolean[m][n];
```
```
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
dfs(board, visited, "", i, j, trie);
}
}
```
```
return new ArrayList<String>(result);
}
```
```
public void dfs(char[][] board, boolean[][] visited, String str, int i,
int j, Trie trie){
int m=board.length;
int n=board[0].length;
```
```
if(i<0 || j<0||i>=m||j>=n){
return;
}
```
```
if(visited[i][j])
return;
```
```
str = str + board[i][j];
```
```
if(!trie.startsWith(str))
return;
```
```
if(trie.search(str)){
result.add(str);
}
```
visited[i][j]=true;
dfs(board, visited, str, i-1, j, trie);
dfs(board, visited, str, i+1, j, trie);
dfs(board, visited, str, i, j-1, trie);
dfs(board, visited, str, i, j+1, trie);
visited[i][j]=false;
}
}

//Trie Node

Program Creek 481 | 677


194 Word Search II

class TrieNode{
public TrieNode[] children = new TrieNode[26];
public String item = "";
}

//Trie
class Trie{
public TrieNode root = new TrieNode();

```
public void insert(String word){
TrieNode node = root;
for(char c: word.toCharArray()){
if(node.children[c-’a’]==null){
node.children[c-’a’]= new TrieNode();
}
node = node.children[c-’a’];
}
node.item = word;
}
```
```
public boolean search(String word){
TrieNode node = root;
for(char c: word.toCharArray()){
if(node.children[c-’a’]==null)
return false;
node = node.children[c-’a’];
}
if(node.item.equals(word)){
return true;
}else{
return false;
}
}
```
public boolean startsWith(String prefix){
TrieNode node = root;
for(char c: prefix.toCharArray()){
if(node.children[c-’a’]==null)
return false;
node = node.children[c-’a’];
}
return true;
}
}

482 | 677 Program Creek


## 195 Range Sum Query 2D Immutable

Given a 2 D matrix matrix, find the sum of the elements inside the rectangle defined

by its upper left corner (row 1 , col 1 ) and lower right corner (row 2 , col 2 ).

**195.1 Analysis**

Since the assumption is that there are many calls to sumRegion method, we should
use some extra space to store the intermediate results. Here we define an array sum[][]

which stores the sum value from ( 0 , 0 ) to the current cell.

**195.2 Java Solution**

public class NumMatrix {
int [][] sum;

```
public NumMatrix(int[][] matrix) {
if(matrix==null || matrix.length==0||matrix[0].length==0)
return;
```
```
int m = matrix.length;
int n = matrix[0].length;
sum = new int[m][n];
```
```
for(int i=0; i<m; i++){
int sumRow=0;
for(int j=0; j<n; j++){
if(i==0){
sumRow += matrix[i][j];
sum[i][j]=sumRow;
}else{
sumRow += matrix[i][j];
sum[i][j]=sumRow+sum[i-1][j];
}
```
```
}
}
}
```
```
public int sumRegion(int row1, int col1, int row2, int col2) {
if(this.sum==null)
```
483 | 677


195 Range Sum Query 2D Immutable

```
return 0;
```
```
int topRightX = row1;
int topRightY = col2;
```
```
int bottomLeftX=row2;
int bottomLeftY= col1;
```
```
int result=0;
```
```
if(row1==0 && col1==0){
result = sum[row2][col2];
}else if(row1==0){
result = sum[row2][col2]
-sum[bottomLeftX][bottomLeftY-1];
```
```
}else if(col1==0){
result = sum[row2][col2]
-sum[topRightX-1][topRightY];
}else{
result = sum[row2][col2]
-sum[topRightX-1][topRightY]
-sum[bottomLeftX][bottomLeftY-1]
+sum[row1-1][col1-1];
}
```
return result;
}
}

484 | 677 Program Creek


## 196 Longest Increasing Path in a Matrix Contents

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You
may NOT move diagonally or move outside of the boundary

**196.1 Java Solution 1 - DFS**

This solution is over time limit.

public class Solution {
int longest=0;

```
public int longestIncreasingPath(int[][] matrix) {
if(matrix==null||matrix.length==0||matrix[0].length==0)
return 0;
```
```
for(int i=0; i<matrix.length; i++){
for(int j=0; j<matrix[0].length; j++){
helper(matrix, i, j, 1);
}
}
```
```
return longest;
}
```
```
public void helper(int[][] matrix, int i, int j, int len){
```
```
if(i-1>=0 && matrix[i-1][j]>matrix[i][j]){
longest = Math.max(longest, len+1);
helper(matrix, i-1, j, len+1);
}
```
```
if(i+1<matrix.length && matrix[i+1][j]>matrix[i][j]){
longest = Math.max(longest, len+1);
helper(matrix, i+1, j, len+1);
}
```
```
if(j-1>=0 && matrix[i][j-1]>matrix[i][j]){
longest = Math.max(longest, len+1);
helper(matrix, i, j-1, len+1);
}
```
485 | 677


196 Longest Increasing Path in a Matrix

```
if(j+1<matrix[0].length && matrix[i][j+1]>matrix[i][j]){
longest = Math.max(longest, len+1);
helper(matrix, i, j+1, len+1);
}
```
}
}

**196.2 Java Solution - Optimized**

public class Solution {
int[] dx = {-1, 1, 0, 0};
int[] dy = {0, 0, -1, 1};

```
public int longestIncreasingPath(int[][] matrix) {
if(matrix==null||matrix.length==0||matrix[0].length==0)
return 0;
```
```
int[][] mem = new int[matrix.length][matrix[0].length];
int longest=0;
```
```
for(int i=0; i<matrix.length; i++){
for(int j=0; j<matrix[0].length; j++){
longest = Math.max(longest, dfs(matrix, i, j, mem));
}
}
```
```
return longest;
}
```
```
public int dfs(int[][] matrix, int i, int j, int[][] mem){
if(mem[i][j]!=0)
return mem[i][j];
```
```
for(int m=0; m<4; m++){
int x = i+dx[m];
int y = j+dy[m];
```
```
if(x>=0&&y>=0&&x<matrix.length&&y<matrix[0].length&&matrix[x][y]>matrix[i][j]){
mem[i][j]=Math.max(mem[i][j], dfs(matrix, x, y, mem));
}
}
```
return ++mem[i][j];
}
}

486 | 677 Program Creek


## 197 Shortest Distance from All Buildings

You want to build a house on an empty land which reaches all buildings in the shortest
amount of distance. You can only move up, down, left and right. You are given a 2 D
grid of values 0 , 1 or 2 , where:

Each 0 marks an empty land which you can pass by freely. Each 1 marks a building
which you cannot pass through. Each 2 marks an obstacle which you cannot pass
through.

For example, given three buildings at ( 0 , 0 ), ( 0 , 4 ), ( 2 , 2 ), and an obstacle at ( 0 , 2 ). The
point ( 1 , 2 ) is an ideal empty land to build a house, as the total travel distance of

3 + 3 + 1 = 7 is minimal. So return 7.

**197.1 Java Solution**

This problem can be solve by BFS. We define one matrix for tracking the distance from
each building, and another matrix for tracking the number of buildings which can be
reached.

public class Solution {

```
int[][] numReach;
int[][] distance;
```
```
public int shortestDistance(int[][] grid) {
if(grid==null||grid.length==0||grid[0].length==0)
return 0;
```
```
int m = grid.length;
int n = grid[0].length;
```
```
numReach = new int[m][n];
distance = new int[m][n];
```
```
int numBuilding = 0;
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
if(grid[i][j]==1){
boolean[][] visited = new boolean[m][n];
LinkedList<Integer> queue = new LinkedList<Integer>();
dfs(grid, i, j, i, j, 0, visited, queue);
```
487 | 677


197 Shortest Distance from All Buildings

```
numBuilding++;
}
}
}
```
```
int result=Integer.MAX_VALUE;
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
if(grid[i][j] == 0 && numReach[i][j]==numBuilding){
result = Math.min(result, distance[i][j]);
```
```
}
}
}
```
```
return result == Integer.MAX_VALUE? -1 : result;
}
```
```
public void dfs(int[][] grid, int ox, int oy, int i, int j,
int distanceSoFar, boolean[][] visited, LinkedList<Integer>
queue){
```
```
visit(grid, i, j, i, j, distanceSoFar, visited, queue);
int n = grid[0].length;
```
```
while(!queue.isEmpty()){
int size = queue.size();
distanceSoFar++;
```
```
for(int k=0; k<size; k++){
int top = queue.poll();
i=top/n;
j=top%n;
```
```
visit(grid, ox, oy, i-1, j, distanceSoFar, visited, queue);
visit(grid, ox, oy, i+1, j, distanceSoFar, visited, queue);
visit(grid, ox, oy, i, j-1, distanceSoFar, visited, queue);
visit(grid, ox, oy, i, j+1, distanceSoFar, visited, queue);
}
```
```
}
}
```
```
public void visit(int[][] grid, int ox, int oy, int i, int j, int
distanceSoFar, boolean[][] visited, LinkedList<Integer> queue){
int m = grid.length;
int n = grid[0].length;
```
```
if(i<0 || i>=m || j<0 || j>=n || visited[i][j])
return;
```
488 | 677 Program Creek


```
197 Shortest Distance from All Buildings
```
```
if((i!=ox || j!=oy) && grid[i][j]!=0){
return;
}
```
visited[i][j]=true;
numReach[i][j]++;
distance[i][j]+= distanceSoFar;
queue.offer(i*n+j);
}
}

Program Creek 489 | 677



## 198 Game of Life

Given a board with m by n cells, each cell has an initial state live ( 1 ) or dead ( 0 ).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the

following four rules:

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation. Any live
cell with more than three live neighbors dies, as if by over-population.. Any dead cell
with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its
current state.

**198.1 Java Solution 1**

Because we need to solve the problem in place, we can use the higher bit to record the
next state. And at the end, shift right a bit to get the next state for each cell.

public void gameOfLife(int[][] board) {
int m = board.length;
int n = board[0].length;

```
int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
int count = 0;
for(int k=0; k<8; k++){
int x = i+dx[k];
int y = j+dy[k];
count += getNeighbor(board, x, y);
}
//Any live cell with fewer than two live neighbors dies
if(count<2 && board[i][j]==1){
board[i][j] &= 1; // this line can be ignored, since next state
is 0 by default
}
//Any dead cell with exactly three live neighbors becomes a live cell
if(count==3 && board[i][j]==0){
board[i][j] |= 2; // e.g., ’01’ & ’10’=’11’
}
// any live cells with 2 or 3 neigbors lives on to the next
generation
```
491 | 677


198 Game of Life

```
if(count>=2 && count<=3 && board[i][j]==1){
board[i][j] |= 2;
}
//Any live cell with more than three live neighbors dies
if(count>3 && board[i][j]==1){
board[i][j] &= 1; // this line can be ignored, since next state
is 0 by default
}
}
}
```
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
board[i][j] >>= 1;
}
}
}

public int getNeighbor(int[][] board, int x, int y){
int m = board.length;
int n = board[0].length;
if(x<0||x>=m||y<0||y>=n)
return 0;
return board[x][y]&1;
}

**198.2 Java Solution 2 - Simplified**

public void gameOfLife(int[][] board) {
int m=board.length;
int n=board[0].length;

```
int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};
```
```
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
int count=0;
for(int k=0; k<8; k++){
int x=i+dx[k];
int y=j+dy[k];
if(x>=0&&x<m&&y>=0&&y<n&&(board[x][y]&1)==1){
count++;
}
}
```
```
if(count==3 && (board[i][j]&1)==0){
```
492 | 677 Program Creek


```
198 Game of Life
```
```
board[i][j]=2;
}
```
```
if(count<2 && (board[i][j]&1)==0){
board[i][j]=0;
}
```
```
if(count>=2 && count<=3 && (board[i][j]&1)==1){
board[i][j]=3;
}
```
```
if(count>3 && (board[i][j]&1)==1){
board[i][j]=1;
}
}
}
```
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
board[i][j] >>=1;
}
}
}

Program Creek 493 | 677



## 199 Paint House

There are a row of n houses, each house can be painted with one of the three colors:
red, blue or green. The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by a n x 3 cost ma-

trix. For example, costs[ 0 ][ 0 ] is the cost of painting house 0 with color red; costs[ 1 ][ 2 ]
is the cost of painting house 1 with color green, and so on... Find the minimum cost
to paint all houses.

**199.1 Java Solution**

A typical DP problem.

public int minCost(int[][] costs) {
if(costs==null||costs.length==0)
return 0;

```
for(int i=1; i<costs.length; i++){
costs[i][0] += Math.min(costs[i-1][1], costs[i-1][2]);
costs[i][1] += Math.min(costs[i-1][0], costs[i-1][2]);
costs[i][2] += Math.min(costs[i-1][0], costs[i-1][1]);
}
```
int m = costs.length-1;
return Math.min(Math.min(costs[m][0], costs[m][1]), costs[m][2]);
}

495 | 677



## 200 Paint House II

There are a row of n houses, each house can be painted with one of the k colors. The
cost of painting each house with a certain color is different. You have to paint all the
houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost
matrix. For example, costs[ 0 ][ 0 ] is the cost of painting house 0 with color 0 ; costs[ 1 ][ 2 ]
is the cost of painting house 1 with color 2 , and so on... Find the minimum cost to
paint all houses.

**200.1 Java Solution**

public int minCostII(int[][] costs) {
if(costs==null || costs.length==0)
return 0;

```
int preMin=0;
int preSecond=0;
int preIndex=-1;
```
```
for(int i=0; i<costs.length; i++){
int currMin=Integer.MAX_VALUE;
int currSecond = Integer.MAX_VALUE;
int currIndex = 0;
```
```
for(int j=0; j<costs[0].length; j++){
if(preIndex==j){
costs[i][j] += preSecond;
}else{
costs[i][j] += preMin;
}
```
```
if(currMin>costs[i][j]){
currSecond = currMin;
currMin=costs[i][j];
currIndex = j;
} else if(currSecond>costs[i][j] ){
currSecond = costs[i][j];
}
}
```
```
preMin=currMin;
```
497 | 677


200 Paint House II

```
preSecond=currSecond;
preIndex =currIndex;
}
```
int result = Integer.MAX_VALUE;
for(int j=0; j<costs[0].length; j++){
if(result>costs[costs.length-1][j]){
result = costs[costs.length-1][j];
}
}
return result;
}

498 | 677 Program Creek


## 201 Sudoku Solver

**201.1 Java Solution**

public void solveSudoku(char[][] board) {
solve(board);
}

public boolean solve(char[][] board){
for(int i=0; i<9; i++){
for(int j=0; j<9; j++){
if(board[i][j]!=’.’)
continue;

```
for(int k=1; k<=9; k++){
board[i][j] = (char) (k+’0’);
if(isValid(board, i, j) && solve(board))
return true;
board[i][j] = ’.’;
}
```
```
return false;
}
}
```
return true; // does not matter
}

public boolean isValid(char[][] board, int i, int j){
HashSet<Character> set = new HashSet<Character>();

```
for(int k=0; k<9; k++){
if(set.contains(board[i][k]))
return false;
```
```
if(board[i][k]!=’.’ ){
set.add(board[i][k]);
}
}
```
```
set.clear();
```
```
for(int k=0; k<9; k++){
```
499 | 677


201 Sudoku Solver

```
if(set.contains(board[k][j]))
return false;
```
```
if(board[k][j]!=’.’ ){
set.add(board[k][j]);
}
}
```
```
set.clear();
```
```
for(int m=0; m<3; m++){
for(int n=0; n<3; n++){
int x=i/3*3+m;
int y=j/3*3+n;
if(set.contains(board[x][y]))
return false;
```
```
if(board[x][y]!=’.’){
set.add(board[x][y]);
}
}
}
```
return true;
}

500 | 677 Program Creek


## 202 Walls and Gates

**202.1 Java Solution 1 - DFS**

public void wallsAndGates(int[][] rooms) {
if(rooms==null || rooms.length==0||rooms[0].length==0)
return;

```
int m = rooms.length;
int n = rooms[0].length;
```
```
boolean[][] visited = new boolean[m][n];
```
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
if(rooms[i][j]==0){
fill(rooms, i-1, j, 0, visited);
fill(rooms, i, j+1, 0, visited);
fill(rooms, i+1, j, 0, visited);
fill(rooms, i, j-1, 0, visited);
visited = new boolean[m][n];
}
}
}
}

public void fill(int[][] rooms, int i, int j, int start, boolean[][] visited){
int m=rooms.length;
int n=rooms[0].length;

```
if(i<0||i>=m||j<0||j>=n||rooms[i][j]<=0||visited[i][j]){
return;
}
```
```
rooms[i][j] = Math.min(rooms[i][j], start+1);
visited[i][j]=true;
```
```
fill(rooms, i-1, j, start+1, visited);
fill(rooms, i, j+1, start+1, visited);
fill(rooms, i+1, j, start+1, visited);
fill(rooms, i, j-1, start+1, visited);
```
```
visited[i][j]=false;
```
501 | 677


202 Walls and Gates

### }

The DFS solution can be simplified as the following:

public void wallsAndGates(int[][] rooms) {
if(rooms==null || rooms.length==0||rooms[0].length==0)
return;

```
int m = rooms.length;
int n = rooms[0].length;
```
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
if(rooms[i][j]==0){
fill(rooms, i, j, 0);
}
}
}
}

public void fill(int[][] rooms, int i, int j, int distance){
int m=rooms.length;
int n=rooms[0].length;

```
if(i<0||i>=m||j<0||j>=n||rooms[i][j]<distance){
return;
}
```
```
rooms[i][j] = distance;
```
fill(rooms, i-1, j, distance+1);
fill(rooms, i, j+1, distance+1);
fill(rooms, i+1, j, distance+1);
fill(rooms, i, j-1, distance+1);
}

**202.2 Java Solution 2 - BFS**

public void wallsAndGates(int[][] rooms) {
if(rooms==null || rooms.length==0||rooms[0].length==0)
return;

```
int m = rooms.length;
int n = rooms[0].length;
```
```
LinkedList<Integer> queue = new LinkedList<Integer>();
```
```
for(int i=0; i<m; i++){
```
502 | 677 Program Creek


```
202 Walls and Gates
```
```
for(int j=0; j<n; j++){
if(rooms[i][j]==0){
queue.add(i*n+j);
}
}
}
```
```
while(!queue.isEmpty()){
int head = queue.poll();
int x=head/n;
int y=head%n;
```
```
if(x>0 && rooms[x-1][y]==Integer.MAX_VALUE){
rooms[x-1][y]=rooms[x][y]+1;
queue.add((x-1)*n+y);
}
```
```
if(x<m-1 && rooms[x+1][y]==Integer.MAX_VALUE){
rooms[x+1][y]=rooms[x][y]+1;
queue.add((x+1)*n+y);
}
```
```
if(y>0 && rooms[x][y-1]==Integer.MAX_VALUE){
rooms[x][y-1]=rooms[x][y]+1;
queue.add(x*n+y-1);
}
```
if(y<n-1 && rooms[x][y+1]==Integer.MAX_VALUE){
rooms[x][y+1]=rooms[x][y]+1;
queue.add(x*n+y+1);
}
}
}

Program Creek 503 | 677



## 203 TicTacToe

Design a Tic-tac-toe game that is played between two players on a n x n grid.

**203.1 Java Solution**

public class TicTacToe {
public char[][] board;
public boolean done;

```
/**Initialize your data structure here. */
public TicTacToe(int n) {
board = new char[n][n];
}
```
```
/**Player {player} makes a move at ({row}, {col}).
@param row The row of the board.
@param col The column of the board.
@param player The player, can be either 1 or 2.
@return The current winning condition, can be either:
0: No one wins.
1: Player 1 wins.
2: Player 2 wins.*/
public int move(int row, int col, int player) {
if(done)
return -1;
```
```
if(player==1){
board[row][col]=’X’;
}else{
board[row][col]=’O’;
}
```
```
int n = board.length;
```
```
//row
int countX=0;
int countO=0;
for(int j=0; j<n; j++){
if(board[row][j]==’X’){
countX++;
}else if(board[row][j]==’O’){
countO++;
```
505 | 677


203 TicTacToe

### }

### }

```
if(countX==n||countO==n){
done = true;
return player;
}
```
```
countX=0;
countO=0;
// column
for(int i=0; i<n; i++){
if(board[i][col]==’X’){
countX++;
}else if(board[i][col]==’O’){
countO++;
}
}
```
```
if(countX==n||countO==n){
done = true;
return player;
}
```
```
if(row==col || row ==n-col-1){
//\
countX=0;
countO=0;
for(int i=0; i<n; i++){
if(board[i][i]==’X’){
countX++;
}else if(board[i][i]==’O’){
countO++;
}
}
if(countX==n||countO==n){
done = true;
return player;
}
```
```
// /
countX=0;
countO=0;
for(int i=0; i<n; i++){
if(board[i][n-i-1]==’X’){
countX++;
}else if(board[i][n-i-1]==’O’){
countO++;
}
}
```
506 | 677 Program Creek


```
203 TicTacToe
```
```
if(countX==n||countO==n){
done = true;
return player;
}
}
```
return 0;
}
}

Program Creek 507 | 677



## 204 Best Meeting Point

A group of two or more people wants to meet and minimize the total travel distance.
You are given a 2 D grid of values 0 or 1 , where each 1 marks the home of someone in

the group. The distance is calculated using Manhattan Distance, where distance(p 1 ,
p 2 ) = |p 2 .x - p 1 .x| + |p 2 .y - p 1 .y|.

For example, given three people living at ( 0 , 0 ), ( 0 , 4 ), and ( 2 , 2 ):

1 - 0 - 0 - 0 - 1
| | | | |
0 - 0 - 0 - 0 - 0
| | | | |
0 - 0 - 1 - 0 - 0

The point ( 0 , 2 ) is an ideal meeting point, as the total travel distance of 2 + 2 + 2 = 6 is

minimal. So return 6.

**204.1 Java Solution**

This problem is converted to find the median value on x-axis and y-axis.

public int minTotalDistance(int[][] grid) {
int m=grid.length;
int n=grid[0].length;

```
ArrayList<Integer> cols = new ArrayList<Integer>();
ArrayList<Integer> rows = new ArrayList<Integer>();
for(int i=0; i<m; i++){
for(int j=0; j<n; j++){
if(grid[i][j]==1){
cols.add(j);
rows.add(i);
}
}
}
```
```
int sum=0;
```
```
for(Integer i: rows){
sum += Math.abs(i - rows.get(rows.size()/2));
}
```
```
Collections.sort(cols);
```
509 | 677


204 Best Meeting Point

```
for(Integer i: cols){
sum+= Math.abs(i-cols.get(cols.size()/2));
}
```
return sum;
}

510 | 677 Program Creek


## 205 Add Two Numbers

You are given two linked lists representing two non-negative numbers. The digits are
stored in reverse order and each of their nodes contain a single digit. Add the two
numbers and return it as a linked list.
Input: ( 2 -> 4 -> 3 ) + ( 5 -> 6 -> 4 ) Output: 7 -> 0 -> 8

**205.1 Java Solution**

public class Solution {
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
int carry =0;

```
ListNode newHead = new ListNode(0);
ListNode p1 = l1, p2 = l2, p3=newHead;
```
```
while(p1 != null || p2 != null){
if(p1 != null){
carry += p1.val;
p1 = p1.next;
}
```
```
if(p2 != null){
carry += p2.val;
p2 = p2.next;
}
```
```
p3.next = new ListNode(carry%10);
p3 = p3.next;
carry /= 10;
}
```
```
if(carry==1)
p3.next=new ListNode(1);
```
return newHead.next;
}
}

```
What if the digits are stored in regular order instead of reversed order?
Answer: We can simple reverse the list, calculate the result, and reverse the result.
```
511 | 677



## 206 Reorder List

Given a singly linked list L: L 0 →L 1 →...→Ln- 1 →Ln, reorder it to: L 0 →Ln→L 1 →Ln-
1 →L 2 →Ln- 2 →...

For example, given 1 , 2 , 3 , 4 , reorder it to 1 , 4 , 2 , 3. You must do this in-place without
altering the nodes’ values.

**206.1 Analysis**

This problem is not straightforward, because it requires "in-place" operations. That

means we can only change their pointers, not creating a new list.

**206.2 Java Solution**

This problem can be solved by doing the following:

- Break list in the middle to two lists (use fast & slow pointers)
- Reverse the order of the second list
- Merge two list back together

The following code is a complete runnable class with testing.

//Class definition of ListNode
class ListNode {
int val;
ListNode next;

ListNode(int x) {
val = x;
next = null;
}
}

public class ReorderList {

```
public static void main(String[] args) {
ListNode n1 = new ListNode(1);
ListNode n2 = new ListNode(2);
ListNode n3 = new ListNode(3);
ListNode n4 = new ListNode(4);
n1.next = n2;
n2.next = n3;
```
513 | 677


206 Reorder List

```
n3.next = n4;
```
```
printList(n1);
```
```
reorderList(n1);
```
```
printList(n1);
}
```
```
public static void reorderList(ListNode head) {
```
```
if (head != null && head.next != null) {
```
```
ListNode slow = head;
ListNode fast = head;
```
```
//use a fast and slow pointer to break the link to two parts.
while (fast != null && fast.next != null && fast.next.next!= null) {
//why need third/second condition?
System.out.println("pre "+slow.val + " " + fast.val);
slow = slow.next;
fast = fast.next.next;
System.out.println("after " + slow.val + " " + fast.val);
}
```
```
ListNode second = slow.next;
slow.next = null;// need to close first part
```
```
// now should have two lists: head and fast
```
```
// reverse order for second part
second = reverseOrder(second);
```
```
ListNode p1 = head;
ListNode p2 = second;
```
```
//merge two lists here
while (p2 != null) {
ListNode temp1 = p1.next;
ListNode temp2 = p2.next;
```
```
p1.next = p2;
p2.next = temp1;
```
```
p1 = temp1;
p2 = temp2;
}
}
}
```
514 | 677 Program Creek


```
206 Reorder List
```
```
public static ListNode reverseOrder(ListNode head) {
```
```
if (head == null || head.next == null) {
return head;
}
```
```
ListNode pre = head;
ListNode curr = head.next;
```
```
while (curr != null) {
ListNode temp = curr.next;
curr.next = pre;
pre = curr;
curr = temp;
}
```
```
// set head node’s next
head.next = null;
```
```
return pre;
}
```
public static void printList(ListNode n) {
System.out.println("------");
while (n != null) {
System.out.print(n.val);
n = n.next;
}
System.out.println();
}
}

**206.3 Takeaway Messages**

The three steps can be used to solve other problems of linked list. A little diagram
may help better understand them.

Reverse List:

Program Creek 515 | 677


206 Reorder List

Merge List:

516 | 677 Program Creek


```
206 Reorder List
```
Program Creek 517 | 677



## 207 Linked List Cycle

Given a linked list, determine if it has a cycle in it.

**207.1 Analysis**

If we have 2 pointers - fast and slow. It is guaranteed that the fast one will meet the

slow one if there exists a circle.

**207.2 Java Solution**

public class Solution {
public boolean hasCycle(ListNode head) {
ListNode fast = head;
ListNode slow = head;

```
while(fast != null && fast.next != null){
slow = slow.next;
fast = fast.next.next;
```
```
if(slow == fast)
return true;
}
```
return false;
}
}

519 | 677



## 208 Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which
could point to any node in the list or null.

Return a deep copy of the list.

**208.1 Java Solution 1**

We can solve this problem by doing the following steps:

- copy every node, i.e., duplicate every node, and insert it to the list
- copy random pointers for all newly created nodes
- break the list to two

public RandomListNode copyRandomList(RandomListNode head) {

```
if (head == null)
return null;
```
```
RandomListNode p = head;
```
```
// copy every node and insert to list
while (p != null) {
RandomListNode copy = new RandomListNode(p.label);
copy.next = p.next;
p.next = copy;
p = copy.next;
}
```
```
// copy random pointer for each new node
p = head;
while (p != null) {
if (p.random != null)
p.next.random = p.random.next;
p = p.next.next;
}
```
```
// break list to two
p = head;
RandomListNode newHead = head.next;
while (p != null) {
RandomListNode temp = p.next;
```
521 | 677


208 Copy List with Random Pointer

```
p.next = temp.next;
if (temp.next != null)
temp.next = temp.next.next;
p = p.next;
}
```
return newHead;
}

The break list part above move pointer 2 steps each time, you can also move one at
a time which is simpler, like the following:

while(p != null && p.next != null){
RandomListNode temp = p.next;
p.next = temp.next;
p = temp;
}

**208.2 Java Solution 2 - Using HashMap**

From Xiaomeng’s comment below, we can use a HashMap which makes it simpler.

public RandomListNode copyRandomList(RandomListNode head) {
if (head == null)
return null;
HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode,
RandomListNode>();
RandomListNode newHead = new RandomListNode(head.label);

```
RandomListNode p = head;
RandomListNode q = newHead;
map.put(head, newHead);
```
```
p = p.next;
while (p != null) {
RandomListNode temp = new RandomListNode(p.label);
map.put(p, temp);
q.next = temp;
q = temp;
p = p.next;
}
```
```
p = head;
q = newHead;
while (p != null) {
if (p.random != null)
q.random = map.get(p.random);
else
```
522 | 677 Program Creek


```
208 Copy List with Random Pointer
```
```
q.random = null;
```
```
p = p.next;
q = q.next;
}
```
return newHead;
}

Program Creek 523 | 677



## 209 Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made
by splicing together the nodes of the first two lists.

**209.1 Analysis**

The key to solve the problem is defining a fake head. Then compare the first elements
from each list. Add the smaller one to the merged list. Finally, when one of them is
empty, simply append it to the merged list, since it is already sorted.

**209.2 Java Solution**

public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
ListNode head = new ListNode(0);
ListNode p = head;

```
while(l1!=null||l2!=null){
if(l1!=null&&l2!=null){
if(l1.val < l2.val){
p.next = l1;
l1=l1.next;
}else{
p.next=l2;
l2=l2.next;
}
p = p.next;
}else if(l1==null){
p.next = l2;
break;
}else if(l2==null){
p.next = l1;
break;
}
}
```
return head.next;
}

525 | 677



## 210 Odd Even Linked List

**210.1 Problem**

Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.
The program should run in O( 1 ) space complexity and O(nodes) time complexity.
Example:

Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

**210.2 Analysis**

This problem can be solved by using two pointers. We iterate over the link and move

the two pointers.

**210.3 Java Solution**

public ListNode oddEvenList(ListNode head) {
if(head == null)
return head;

```
ListNode result = head;
ListNode p1 = head;
ListNode p2 = head.next;
ListNode connectNode = head.next;
```
527 | 677


210 Odd Even Linked List

```
while(p1 != null && p2 != null){
ListNode t = p2.next;
if(t == null)
break;
```
```
p1.next = p2.next;
p1 = p1.next;
```
```
p2.next = p1.next;
p2 = p2.next;
}
```
```
p1.next = connectNode;
```
return result;
}

528 | 677 Program Creek


## 211 Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only
once.
For example,

Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

**211.1 Thoughts**

The key of this problem is using the right loop condition. And change what is nec-
essary in each loop. You can use different iteration conditions like the following 2
solutions.

**211.2 Solution 1**

### /**

* Definition for singly-linked list.
* public class ListNode {
* int val;
* ListNode next;
* ListNode(int x) {
* val = x;
* next = null;
* }
* }
*/
public class Solution {
public ListNode deleteDuplicates(ListNode head) {
if(head == null || head.next == null)
return head;

```
ListNode prev = head;
ListNode p = head.next;
```
```
while(p != null){
if(p.val == prev.val){
prev.next = p.next;
p = p.next;
//no change prev
```
529 | 677


211 Remove Duplicates from Sorted List

```
}else{
prev = p;
p = p.next;
}
}
```
return head;
}
}

**211.3 Solution 2**

public class Solution {
public ListNode deleteDuplicates(ListNode head) {
if(head == null || head.next == null)
return head;

```
ListNode p = head;
```
```
while( p!= null && p.next != null){
if(p.val == p.next.val){
p.next = p.next.next;
}else{
p = p.next;
}
}
```
return head;
}
}

530 | 677 Program Creek


## 212 Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only
distinct numbers from the original list.
For example, given 1 -> 1 -> 1 -> 2 -> 3 , return 2 -> 3.

**212.1 Java Solution**

public ListNode deleteDuplicates(ListNode head) {
ListNode t = new ListNode(0);
t.next = head;

```
ListNode p = t;
while(p.next!=null&&p.next.next!=null){
if(p.next.val == p.next.next.val){
int dup = p.next.val;
while(p.next!=null&&p.next.val==dup){
p.next = p.next.next;
}
}else{
p=p.next;
}
```
```
}
```
return t.next;
}

531 | 677



## 213 Partition List

Given a linked list and a value x, partition it such that all nodes less than x come
before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two
partitions.

For example, given 1 -> 4 -> 3 -> 2 -> 5 -> 2 and x = 3 , return 1 -> 2 -> 2 -> 4 -> 3 -> 5.

**213.1 Java Solution**

public class Solution {
public ListNode partition(ListNode head, int x) {
if(head == null) return null;

```
ListNode fakeHead1 = new ListNode(0);
ListNode fakeHead2 = new ListNode(0);
fakeHead1.next = head;
```
```
ListNode p = head;
ListNode prev = fakeHead1;
ListNode p2 = fakeHead2;
```
```
while(p != null){
if(p.val < x){
p = p.next;
prev = prev.next;
}else{
```
```
p2.next = p;
prev.next = p.next;
```
```
p = prev.next;
p2 = p2.next;
}
}
```
```
// close the list
p2.next = null;
```
```
prev.next = fakeHead2.next;
```
```
return fakeHead1.next;
```
533 | 677


213 Partition List

### }

### }

534 | 677 Program Creek


## 214 LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should
support the following operations: get and set.
get(key) - Get the value (will always be positive) of the key if the key exists in the
cache, otherwise return - 1. set(key, value) - Set or insert the value if the key is not

already present. When the cache reached its capacity, it should invalidate the least
recently used item before inserting a new item.

**214.1 Analysis**

The key to solve this problem is using a double linked list which enables us to quickly

move nodes.

The LRU cache is a hash table of keys and double linked nodes. The hash table

makes the time of get() to be O( 1 ). The list of double linked nodes make the nodes
adding/removal operations O( 1 ).

**214.2 Java Solution**

Define a double linked list node.

class Node{
int key;
int value;
Node pre;
Node next;

535 | 677


214 LRU Cache

public Node(int key, int value){
this.key = key;
this.value = value;
}
}

public class LRUCache {
int capacity;
HashMap<Integer, Node> map = new HashMap<Integer, Node>();
Node head=null;
Node end=null;

```
public LRUCache(int capacity) {
this.capacity = capacity;
}
```
```
public int get(int key) {
if(map.containsKey(key)){
Node n = map.get(key);
remove(n);
setHead(n);
return n.value;
}
```
```
return -1;
}
```
```
public void remove(Node n){
if(n.pre!=null){
n.pre.next = n.next;
}else{
head = n.next;
}
```
```
if(n.next!=null){
n.next.pre = n.pre;
}else{
end = n.pre;
}
```
```
}
```
```
public void setHead(Node n){
n.next = head;
n.pre = null;
```
```
if(head!=null)
head.pre = n;
```
536 | 677 Program Creek


```
214 LRU Cache
```
```
head = n;
```
```
if(end ==null)
end = head;
}
```
```
public void set(int key, int value) {
if(map.containsKey(key)){
Node old = map.get(key);
old.value = value;
remove(old);
setHead(old);
}else{
Node created = new Node(key, value);
if(map.size()>=capacity){
map.remove(end.key);
remove(end);
setHead(created);
```
```
}else{
setHead(created);
}
```
map.put(key, created);
}
}
}

Program Creek 537 | 677



## 215 Intersection of Two Linked Lists

**215.1 Problem**

Write a program to find the node at which the intersection of two singly linked lists
begins.
For example, the following two linked lists:

A: a1 -> a2
->
c1 -> c2 -> c3
->
B: b1 -> b2 -> b3

begin to intersect at node c 1.

**215.2 Java Solution**

First calculate the length of two lists and find the difference. Then start from the longer

list at the diff offset, iterate though 2 lists and find the node.

/**

* Definition for singly-linked list.
* public class ListNode {
* int val;
* ListNode next;
* ListNode(int x) {
* val = x;
* next = null;
* }
* }
*/
public class Solution {
public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
int len1 = 0;
int len2 = 0;
ListNode p1=headA, p2=headB;
if (p1 == null || p2 == null)
return null;

```
while(p1 != null){
len1++;
p1 = p1.next;
```
539 | 677


215 Intersection of Two Linked Lists

### }

```
while(p2 !=null){
len2++;
p2 = p2.next;
}
```
```
int diff = 0;
p1=headA;
p2=headB;
```
```
if(len1 > len2){
diff = len1-len2;
int i=0;
while(i<diff){
p1 = p1.next;
i++;
}
}else{
diff = len2-len1;
int i=0;
while(i<diff){
p2 = p2.next;
i++;
}
}
```
```
while(p1 != null && p2 != null){
if(p1.val == p2.val){
return p1;
}else{
```
```
}
p1 = p1.next;
p2 = p2.next;
}
```
return null;
}
}

540 | 677 Program Creek


## 216 Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.
Example

Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

**216.1 Java Solution**

The key to solve this problem is using a helper node to track the head of the list.

public ListNode removeElements(ListNode head, int val) {
ListNode helper = new ListNode(0);
helper.next = head;
ListNode p = helper;

```
while(p.next != null){
if(p.next.val == val){
ListNode next = p.next;
p.next = next.next;
}else{
p = p.next;
}
}
```
return helper.next;
}

541 | 677



## 217 Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

```
For example, given 1 -> 2 -> 3 -> 4 , you should return the list as 2 -> 1 -> 4 -> 3.
Your algorithm should use only constant space. You may not modify the values in
```
the list, only nodes itself can be changed.

**217.1 Java Solution 1**

Use two template variable to track the previous and next node of each pair.

public ListNode swapPairs(ListNode head) {
if(head == null || head.next == null)
return head;

```
ListNode h = new ListNode(0);
h.next = head;
ListNode p = h;
```
```
while(p.next != null && p.next.next != null){
//use t1 to track first node
ListNode t1 = p;
p = p.next;
t1.next = p.next;
```
```
//use t2 to track next node of the pair
ListNode t2 = p.next.next;
p.next.next = p;
p.next = t2;
}
```
return h.next;
}

**217.2 Java Solution 2**

Each time I do the same problem I often get the different solutions. Here is another

way of writing this solution.

public ListNode swapPairs(ListNode head) {
if(head==null || head.next==null)

543 | 677


217 Swap Nodes in Pairs

```
return head;
```
```
//a fake head
ListNode h = new ListNode(0);
h.next = head;
```
```
ListNode p1 = head;
ListNode p2 = head.next;
```
```
ListNode pre = h;
while(p1!=null && p2!=null){
pre.next = p2;
```
```
ListNode t = p2.next;
p2.next = p1;
pre = p1;
p1.next = t;
```
```
p1 = p1.next;
```
```
if(t!=null)
p2 = t.next;
}
```
return h.next;
}

544 | 677 Program Creek


## 218 Reverse Linked List

Reverse a singly linked list.

**218.1 Java Solution 1 - Iterative**

public ListNode reverseList(ListNode head) {
if(head==null||head.next==null)
return head;

```
ListNode p1 = head;
ListNode p2 = p1.next;
```
```
head.next = null;
while(p1!=null&& p2!=null){
ListNode t = p2.next;
p2.next = p1;
p1 = p2;
p2 = t;
}
```
return p1;
}

**218.2 Java Solution 2 - Recursive**

public ListNode reverseList(ListNode head) {
if(head==null || head.next == null)
return head;

```
//get second node
ListNode second = head.next;
//set first’s next to be null
head.next = null;
```
```
ListNode rest = reverseList(second);
second.next = head;
```
return rest;
}

545 | 677



## 219 Reverse Linked List II

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example: given 1 -> 2 -> 3 -> 4 -> 5 ->NULL, m = 2 and n = 4 , return 1 -> 4 -> 3 -> 2 -> 5 -
>NULL.

**219.1 Analysis**

**219.2 Java Solution**

public ListNode reverseBetween(ListNode head, int m, int n) {
if(m==n) return head;

```
ListNode prev = null;//track (m-1)th node
ListNode first = new ListNode(0);//first’s next points to mth
ListNode second = new ListNode(0);//second’s next points to (n+1)th
```
```
int i=0;
ListNode p = head;
while(p!=null){
i++;
if(i==m-1){
prev = p;
}
```
```
if(i==m){
first.next = p;
}
```
```
if(i==n){
second.next = p.next;
p.next = null;
}
```
```
p= p.next;
}
if(first.next == null)
return head;
```
```
// reverse list [m, n]
ListNode p1 = first.next;
ListNode p2 = p1.next;
```
547 | 677


219 Reverse Linked List II

```
p1.next = second.next;
```
```
while(p1!=null && p2!=null){
ListNode t = p2.next;
p2.next = p1;
p1 = p2;
p2 = t;
}
```
```
//connect to previous part
if(prev!=null)
prev.next = p1;
else
return p1;
```
return head;
}

548 | 677 Program Creek


## 220 Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example, given linked list 1 -> 2 -> 3 -> 4 -> 5 and n = 2 , the result is 1 -> 2 -> 3 -> 5.

**220.1 Java Solution 1 - Naive Two Passes**

Calculate the length first, and then remove the nth from the beginning.

public ListNode removeNthFromEnd(ListNode head, int n) {
if(head == null)
return null;

```
//get length of list
ListNode p = head;
int len = 0;
while(p != null){
len++;
p = p.next;
}
```
```
//if remove first node
int fromStart = len-n+1;
if(fromStart==1)
return head.next;
```
```
//remove non-first node
p = head;
int i=0;
while(p!=null){
i++;
if(i==fromStart-1){
p.next = p.next.next;
}
p=p.next;
}
```
return head;
}

549 | 677


220 Remove Nth Node From End of List

**220.2 Java Solution 2 - One Pass**

Use fast and slow pointers. The fast pointer is n steps ahead of the slow pointer. When
the fast reaches the end, the slow pointer points at the previous element of the target

element.

public ListNode removeNthFromEnd(ListNode head, int n) {
if(head == null)
return null;

```
ListNode fast = head;
ListNode slow = head;
```
```
for(int i=0; i<n; i++){
fast = fast.next;
}
```
```
//if remove the first node
if(fast == null){
head = head.next;
return head;
}
```
```
while(fast.next != null){
fast = fast.next;
slow = slow.next;
}
```
```
slow.next = slow.next.next;
```
return head;
}

550 | 677 Program Creek


## 221 Palindrome Linked List Contents

Given a singly linked list, determine if it is a palindrome.

**221.1 Java Solution 1**

We can create a new list in reversed order and then compare each node. The time and
space are O(n).

public boolean isPalindrome(ListNode head) {
if(head == null)
return true;

```
ListNode p = head;
ListNode prev = new ListNode(head.val);
```
```
while(p.next != null){
ListNode temp = new ListNode(p.next.val);
temp.next = prev;
prev = temp;
p = p.next;
}
```
```
ListNode p1 = head;
ListNode p2 = prev;
```
```
while(p1!=null){
if(p1.val != p2.val)
return false;
```
```
p1 = p1.next;
p2 = p2.next;
}
```
return true;
}

**221.2 Java Solution 2**

We can use a fast and slow pointer to get the center of the list, then reverse the second
list and compare two sublists. The time is O(n) and space is O( 1 ).

551 | 677


221 Palindrome Linked List

public boolean isPalindrome(ListNode head) {

```
if(head == null || head.next==null)
return true;
```
```
//find list center
ListNode fast = head;
ListNode slow = head;
```
```
while(fast.next!=null && fast.next.next!=null){
fast = fast.next.next;
slow = slow.next;
}
```
```
ListNode secondHead = slow.next;
slow.next = null;
```
```
//reverse second part of the list
ListNode p1 = secondHead;
ListNode p2 = p1.next;
```
```
while(p1!=null && p2!=null){
ListNode temp = p2.next;
p2.next = p1;
p1 = p2;
p2 = temp;
}
```
```
secondHead.next = null;
```
```
//compare two sublists now
ListNode p = (p2==null?p1:p2);
ListNode q = head;
while(p!=null){
if(p.val != q.val)
return false;
```
```
p = p.next;
q = q.next;
```
```
}
```
return true;
}

552 | 677 Program Creek


## 222 Delete Node in a Linked List

Write a function to delete a node (except the tail) in a singly linked list, given only
access to that node.
Supposed the linked list is 1 -> 2 -> 3 -> 4 and you are given the third node with value
3 , the linked list should become 1 -> 2 -> 4 after calling your function.

**222.1 Java Solution**

public void deleteNode(ListNode node) {
node.val = node.next.val;
node.next = node.next.next;
}

Is this problem too easy? Or I’m doing it wrong.

553 | 677



## 223 Reverse Nodes in kGroup

Given a linked list, reverse the nodes of a linked list k at a time and return its modified
list.
If the number of nodes is not a multiple of k then left-out nodes in the end should
remain as it is.

```
You may not alter the values in the nodes, only nodes itself may be changed.
Only constant memory is allowed.
For example, Given this linked list: 1 -> 2 -> 3 -> 4 -> 5
For k = 2 , you should return: 2 -> 1 -> 4 -> 3 -> 5
For k = 3 , you should return: 3 -> 2 -> 1 -> 4 -> 5
```
**223.1 Java Solution**

public ListNode reverseKGroup(ListNode head, int k) {
if(head==null||k==1)
return head;

```
ListNode fake = new ListNode(0);
fake.next = head;
ListNode pre = fake;
int i=0;
```
```
ListNode p = head;
while(p!=null){
i++;
if(i%k==0){
pre = reverse(pre, p.next);
p = pre.next;
}else{
p = p.next;
}
}
```
return fake.next;
}

/*
* 0->1->2->3->4->5->6
* | |
* pre next
*

555 | 677


223 Reverse Nodes in kGroup

* after calling pre = reverse(pre, next)
*
* 0->3->2->1->4->5->6
* | |
* pre next
*/
public ListNode reverse(ListNode pre, ListNode next){
ListNode last = pre.next;
ListNode curr = last.next;

```
while(curr != next){
last.next = curr.next;
curr.next = pre.next;
pre.next = curr;
curr = last.next;
}
```
return last;
}

556 | 677 Program Creek


## 224 Binary Tree Preorder Traversal

**224.1 Analysis**

Preorder binary tree traversal is a classic interview problem about trees. The key to
solve this problem is to understand the following:

- What is preorder? (parent node is processed before its children)
- Use Stack from Java Core library

The key is using a stack to store left and right children, and push right child first so

that it is processed after the left child.

**224.2 Java Solution**

public class TreeNode {
int val;
TreeNode left;
TreeNode right;
TreeNode(int x) { val = x; }
}

public class Solution {
public ArrayList<Integer> preorderTraversal(TreeNode root) {
ArrayList<Integer> returnList = new ArrayList<Integer>();

```
if(root == null)
return returnList;
```
```
Stack<TreeNode> stack = new Stack<TreeNode>();
stack.push(root);
```
```
while(!stack.empty()){
TreeNode n = stack.pop();
returnList.add(n.val);
```
```
if(n.right != null){
stack.push(n.right);
}
if(n.left != null){
stack.push(n.left);
}
```
557 | 677


224 Binary Tree Preorder Traversal

### }

return returnList;
}
}

558 | 677 Program Creek


## 225 Binary Tree Inorder Traversal

There are 3 solutions for solving this problem.

**225.1 Java Solution 1 - Iterative**

The key to solve inorder traversal of binary tree includes the following:

- The order of "inorder" is: left child ->parent ->right child
- Use a stack to track nodes
- Understand when to push node into the stack and when to pop node out of the
    stack

//Definition for binary tree
public class TreeNode {
int val;
TreeNode left;
TreeNode right;
TreeNode(int x) { val = x; }
}

public class Solution {
public ArrayList<Integer> inorderTraversal(TreeNode root) {
// IMPORTANT: Please reset any member data you declared, as
// the same Solution instance will be reused for each test case.

559 | 677


225 Binary Tree Inorder Traversal

```
ArrayList<Integer> lst = new ArrayList<Integer>();
```
```
if(root == null)
return lst;
```
```
Stack<TreeNode> stack = new Stack<TreeNode>();
//define a pointer to track nodes
TreeNode p = root;
```
```
while(!stack.empty() || p != null){
```
```
// if it is not null, push to stack
//and go down the tree to left
if(p != null){
stack.push(p);
p = p.left;
```
```
// if no left child
// pop stack, process the node
// then let p point to the right
}else{
TreeNode t = stack.pop();
lst.add(t.val);
p = t.right;
}
}
```
return lst;
}
}

**225.2 Java Solution 2 - Recursive**

The recursive solution is trivial.

public class Solution {
List<Integer> result = new ArrayList<Integer>();

```
public List<Integer> inorderTraversal(TreeNode root) {
if(root !=null){
helper(root);
}
```
```
return result;
}
```
```
public void helper(TreeNode p){
if(p.left!=null)
```
560 | 677 Program Creek


```
225 Binary Tree Inorder Traversal
```
```
helper(p.left);
```
```
result.add(p.val);
```
if(p.right!=null)
helper(p.right);
}
}

**225.3 Java Solution 3 - Simple**

Updated on 4 / 28 / 2016

public List<Integer> inorderTraversal(TreeNode root) {
List<Integer> result = new ArrayList<Integer>();
if(root==null)
return result;
Stack<TreeNode> stack = new Stack<TreeNode>();
stack.push(root);

```
while(!stack.isEmpty()){
TreeNode top = stack.peek();
if(top.left!=null){
stack.push(top.left);
top.left=null;
}else{
result.add(top.val);
stack.pop();
if(top.right!=null){
stack.push(top.right);
}
}
}
```
return result;
}

Program Creek 561 | 677



## 226 Binary Tree Postorder Traversal

Among preoder, inorder and postorder binary tree traversal problems, postorder traver-

sal is the most complicated one.

**226.1 Java Solution 1**

The key to to iterative postorder traversal is the following:

- The order of "Postorder" is: left child ->right child ->parent node.
- Find the relation between the previously visited node and the current node
- Use a stack to track nodes

As we go down the tree to the lft, check the previously visited node. If the current
node is the left or right child of the previous node, then keep going down the tree, and
add left/right node to stack when applicable. When there is no children for current

node, i.e., the current node is a leaf, pop it from the stack. Then the previous node
become to be under the current node for next loop. You can using an example to walk
through the code.

//Definition for binary tree
public class TreeNode {
int val;
TreeNode left;
TreeNode right;
TreeNode(int x) { val = x; }
}

public class Solution {
public ArrayList<Integer> postorderTraversal(TreeNode root) {

```
ArrayList<Integer> lst = new ArrayList<Integer>();
```
563 | 677


226 Binary Tree Postorder Traversal

```
if(root == null)
return lst;
```
```
Stack<TreeNode> stack = new Stack<TreeNode>();
stack.push(root);
```
```
TreeNode prev = null;
while(!stack.empty()){
TreeNode curr = stack.peek();
```
```
// go down the tree.
//check if current node is leaf, if so, process it and pop stack,
//otherwise, keep going down
if(prev == null || prev.left == curr || prev.right == curr){
//prev == null is the situation for the root node
if(curr.left != null){
stack.push(curr.left);
}else if(curr.right != null){
stack.push(curr.right);
}else{
stack.pop();
lst.add(curr.val);
}
```
```
//go up the tree from left node
//need to check if there is a right child
//if yes, push it to stack
//otherwise, process parent and pop stack
}else if(curr.left == prev){
if(curr.right != null){
stack.push(curr.right);
}else{
stack.pop();
lst.add(curr.val);
}
```
```
//go up the tree from right node
//after coming back from right node, process parent node and pop
stack.
}else if(curr.right == prev){
stack.pop();
lst.add(curr.val);
}
```
```
prev = curr;
}
```
return lst;
}
}

564 | 677 Program Creek


```
226 Binary Tree Postorder Traversal
```
**226.2 Java Solution 2 - Simple!**

Thanks to Edmond. This solution is superior!

public List<Integer> postorderTraversal(TreeNode root) {
List<Integer> res = new ArrayList<Integer>();

```
if(root==null) {
return res;
}
```
```
Stack<TreeNode> stack = new Stack<TreeNode>();
stack.push(root);
```
```
while(!stack.isEmpty()) {
TreeNode temp = stack.peek();
if(temp.left==null && temp.right==null) {
TreeNode pop = stack.pop();
res.add(pop.val);
}
else {
if(temp.right!=null) {
stack.push(temp.right);
temp.right = null;
}
```
```
if(temp.left!=null) {
stack.push(temp.left);
temp.left = null;
}
}
}
```
return res;
}

Program Creek 565 | 677



## 227 Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left

to right, level by level).
For example: Given binary tree 3 , 9 , 20 ,#,#, 15 , 7 ,

3
/ \
9 20
/ \
15 7

return its level order traversal as [[ 3 ], [ 9 , 20 ], [ 15 , 7 ]]

**227.1 Analysis**

It is obvious that this problem can be solve by using a queue. However, if we use one
queue we can not track when each level starts. So we use two queues to track the

current level and the next level.

**227.2 Java Solution**

public ArrayList<ArrayList<Integer>> levelOrder(TreeNode root) {
ArrayList<ArrayList<Integer>> al = new ArrayList<ArrayList<Integer>>();
ArrayList<Integer> nodeValues = new ArrayList<Integer>();
if(root == null)
return al;

```
LinkedList<TreeNode> current = new LinkedList<TreeNode>();
LinkedList<TreeNode> next = new LinkedList<TreeNode>();
current.add(root);
```
```
while(!current.isEmpty()){
TreeNode node = current.remove();
```
```
if(node.left != null)
next.add(node.left);
if(node.right != null)
next.add(node.right);
```
```
nodeValues.add(node.val);
```
567 | 677


227 Binary Tree Level Order Traversal

```
if(current.isEmpty()){
current = next;
next = new LinkedList<TreeNode>();
al.add(nodeValues);
nodeValues = new ArrayList();
}
```
}
return al;
}

568 | 677 Program Creek


## 228 Binary Tree Level Order Traversal II

Given a binary tree, return the bottom-up level order traversal of its nodes’ values.
For example, given binary tree 3 , 9 , 20 ,#,#, 15 , 7 ,

3
/ \
9 20
/ \
15 7

return its level order traversal as [[ 15 , 7 ], [ 9 , 20 ],[ 3 ]]

**228.1 Java Solution**

public List<ArrayList<Integer>> levelOrderBottom(TreeNode root) {
ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();

```
if(root == null){
return result;
}
```
```
LinkedList<TreeNode> current = new LinkedList<TreeNode>();
LinkedList<TreeNode> next = new LinkedList<TreeNode>();
current.offer(root);
```
```
ArrayList<Integer> numberList = new ArrayList<Integer>();
```
```
// need to track when each level starts
while(!current.isEmpty()){
TreeNode head = current.poll();
```
```
numberList.add(head.val);
```
```
if(head.left != null){
next.offer(head.left);
}
if(head.right!= null){
next.offer(head.right);
}
```
```
if(current.isEmpty()){
current = next;
```
569 | 677


228 Binary Tree Level Order Traversal II

```
next = new LinkedList<TreeNode>();
result.add(numberList);
numberList = new ArrayList<Integer>();
}
}
```
```
//return Collections.reverse(result);
ArrayList<ArrayList<Integer>> reversedResult = new
ArrayList<ArrayList<Integer>>();
for(int i=result.size()-1; i>=0; i--){
reversedResult.add(result.get(i));
}
```
return reversedResult;
}

570 | 677 Program Creek


## 229 Binary Tree Vertical Order Traversal

Given a binary tree, return the vertical order traversal of its nodes’ values. (ie, from

top to bottom, column by column).

**229.1 Java Solution**

For each node, its left child’s degree is - 1 and is right child’s degree is + 1. We can do

a level order traversal and save the degree information.

public List<List<Integer>> verticalOrder(TreeNode root) {
List<List<Integer>> result = new ArrayList<List<Integer>>();
if(root==null)
return result;

```
// level and list
HashMap<Integer, ArrayList<Integer>> map = new HashMap<Integer,
ArrayList<Integer>>();
```
```
LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
LinkedList<Integer> level = new LinkedList<Integer>();
```
```
queue.offer(root);
level.offer(0);
```
```
int minLevel=0;
int maxLevel=0;
```
```
while(!queue.isEmpty()){
TreeNode p = queue.poll();
int l = level.poll();
```
```
//track min and max levels
minLevel=Math.min(minLevel, l);
maxLevel=Math.max(maxLevel, l);
```
```
if(map.containsKey(l)){
map.get(l).add(p.val);
}else{
ArrayList<Integer> list = new ArrayList<Integer>();
list.add(p.val);
map.put(l, list);
}
```
571 | 677


229 Binary Tree Vertical Order Traversal

```
if(p.left!=null){
queue.offer(p.left);
level.offer(l-1);
}
```
```
if(p.right!=null){
queue.offer(p.right);
level.offer(l+1);
}
}
```
```
for(int i=minLevel; i<=maxLevel; i++){
if(map.containsKey(i)){
result.add(map.get(i));
}
}
```
return result;
}

572 | 677 Program Creek


## 230 Invert Binary Tree

Google: _90_

**230.1 Java Solution 1 - Recursive**

public TreeNode invertTree(TreeNode root) {
if(root!=null){
helper(root);
}

return root;
}

public void helper(TreeNode p){

```
TreeNode temp = p.left;
p.left = p.right;
p.right = temp;
```
```
if(p.left!=null)
helper(p.left);
```
if(p.right!=null)
helper(p.right);
}

**230.2 Java Solution 2 - Iterative**

public TreeNode invertTree(TreeNode root) {
LinkedList<TreeNode> queue = new LinkedList<TreeNode>();

```
if(root!=null){
queue.add(root);
}
```
```
while(!queue.isEmpty()){
TreeNode p = queue.poll();
if(p.left!=null)
queue.add(p.left);
```
573 | 677


230 Invert Binary Tree

```
if(p.right!=null)
queue.add(p.right);
```
```
TreeNode temp = p.left;
p.left = p.right;
p.right = temp;
}
```
return root;
}

574 | 677 Program Creek


## 231 Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest ele-
ment in it. ( 1 ≤k≤BST’s total elements)

**231.1 Java Solution 1 - Inorder Traversal**

We can inorder traverse the tree and get the kth smallest element. Time is O(n).

public int kthSmallest(TreeNode root, int k) {
Stack<TreeNode> stack = new Stack<TreeNode>();

```
TreeNode p = root;
int result = 0;
```
```
while(!stack.isEmpty() || p!=null){
if(p!=null){
stack.push(p);
p = p.left;
}else{
TreeNode t = stack.pop();
k--;
if(k==0)
result = t.val;
p = t.right;
}
}
```
return result;
}

Similarly, we can also write the inorder traversal as the following:

public int kthSmallest(TreeNode root, int k) {
Stack<TreeNode> stack = new Stack<TreeNode>();
TreeNode p = root;
while(p!=null){
stack.push(p);
p=p.left;
}
int i=0;
while(!stack.isEmpty()){
TreeNode t = stack.pop();
i++;

575 | 677


231 Kth Smallest Element in a BST

```
if(i==k)
return t.val;
```
```
TreeNode r = t.right;
while(r!=null){
stack.push(r);
r=r.left;
}
```
```
}
```
return -1;
}

**231.2 Java Solution 2 - Extra Data Structure**

We can let each node track the order, i.e., the number of elements that are less than
itself. Time is O(log(n)).

576 | 677 Program Creek


## 232 Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in
the tree along the parent-child connections. The longest consecutive path need to be

from parent to child (cannot be the reverse).

**232.1 Java Solution 1 - Queue**

public int longestConsecutive(TreeNode root) {
if(root==null)
return 0;

```
LinkedList<TreeNode> nodeQueue = new LinkedList<TreeNode>();
LinkedList<Integer> sizeQueue = new LinkedList<Integer>();
```
```
nodeQueue.offer(root);
sizeQueue.offer(1);
int max=1;
```
```
while(!nodeQueue.isEmpty()){
TreeNode head = nodeQueue.poll();
int size = sizeQueue.poll();
```
```
if(head.left!=null){
int leftSize=size;
if(head.val==head.left.val-1){
leftSize++;
max = Math.max(max, leftSize);
}else{
leftSize=1;
}
```
```
nodeQueue.offer(head.left);
sizeQueue.offer(leftSize);
}
```
```
if(head.right!=null){
int rightSize=size;
if(head.val==head.right.val-1){
```
577 | 677


232 Binary Tree Longest Consecutive Sequence

```
rightSize++;
max = Math.max(max, rightSize);
}else{
rightSize=1;
}
```
```
nodeQueue.offer(head.right);
sizeQueue.offer(rightSize);
}
```
### }

return max;
}

**232.2 Java Solution 2 - Recursion**

public class Solution {
int max=0;

```
public int longestConsecutive(TreeNode root) {
helper(root);
return max;
}
```
```
public int helper(TreeNode root) {
if(root==null)
return 0;
```
```
int l = helper(root.left);
int r = helper(root.right);
```
```
int fromLeft = 0;
int fromRight= 0;
```
```
if(root.left==null){
fromLeft=1;
}else if(root.left.val-1==root.val){
fromLeft = l+1;
}else{
fromLeft=1;
}
```
```
if(root.right==null){
fromRight=1;
}else if(root.right.val-1==root.val){
```
578 | 677 Program Creek


```
232 Binary Tree Longest Consecutive Sequence
```
```
fromRight = r+1;
}else{
fromRight=1;
}
```
```
max = Math.max(max, fromLeft);
max = Math.max(max, fromRight);
```
```
return Math.max(fromLeft, fromRight);
}
```
}

Program Creek 579 | 677



## 233 Validate Binary Search Tree

```
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
```
- The left subtree of a node contains only nodes with keys less than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s
    key.
- Both the left and right subtrees must also be binary search trees.

**233.1 Java Solution 1 - Recursive**

All values on the left sub tree must be less than root, and all values on the right sub

tree must be greater than root. So we just check the boundaries for each node.

public boolean isValidBST(TreeNode root) {
return isValidBST(root, Double.NEGATIVE_INFINITY,
Double.POSITIVE_INFINITY);
}

public boolean isValidBST(TreeNode p, double min, double max){
if(p==null)
return true;

```
if(p.val <= min || p.val >= max)
return false;
```
return isValidBST(p.left, min, p.val) && isValidBST(p.right, p.val, max);
}

This solution also goes to the left subtree first. If the violation occurs close to the
root but on the right subtree, the method still cost O(n). The second solution below

can handle violations close to root node faster.
This solution can also be written as the following:

public boolean isValidBST(TreeNode root) {
if(root==null)
return true;

return helper(root, Double.NEGATIVE_INFINITY, Double.POSITIVE_INFINITY);
}

581 | 677


233 Validate Binary Search Tree

public boolean helper(TreeNode root, double low, double high){

```
if(root.val<=low || root.val>=high)
return false;
```
```
if(root.left!=null && !helper(root.left, low, root.val)){
return false;
}
```
```
if(root.right!=null && !helper(root.right, root.val, high)){
return false;
}
```
return true;
}

**233.2 Java Solution 2 - Iterative**

public class Solution {
public boolean isValidBST(TreeNode root) {
if(root == null)
return true;

LinkedList<BNode> queue = new LinkedList<BNode>();
queue.add(new BNode(root, Double.NEGATIVE_INFINITY,
Double.POSITIVE_INFINITY));
while(!queue.isEmpty()){
BNode b = queue.poll();
if(b.n.val <= b.left || b.n.val >=b.right){
return false;
}
if(b.n.left!=null){
queue.offer(new BNode(b.n.left, b.left, b.n.val));
}
if(b.n.right!=null){
queue.offer(new BNode(b.n.right, b.n.val, b.right));
}
}
return true;
}
}
//define a BNode class with TreeNode and it’s boundaries
class BNode{
TreeNode n;
double left;
double right;
public BNode(TreeNode n, double left, double right){

582 | 677 Program Creek


```
233 Validate Binary Search Tree
```
this.n = n;
this.left = left;
this.right = right;
}
}

Program Creek 583 | 677



## 234 Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.
For example, Given

1
/ \
2 5
/ \ \
3 4 6

The flattened tree should look like:

1 \ 2 \ 3 \ 4 \ 5 \ 6

**234.1 Thoughts**

Go down through the left, when right is not null, push right to stack.

**234.2 Java Solution**

### /**

* Definition for binary tree
* public class TreeNode {
* int val;
* TreeNode left;
* TreeNode right;
* TreeNode(int x) { val = x; }
* }
*/
public class Solution {

585 | 677


234 Flatten Binary Tree to Linked List

```
public void flatten(TreeNode root) {
Stack<TreeNode> stack = new Stack<TreeNode>();
TreeNode p = root;
```
```
while(p != null || !stack.empty()){
```
```
if(p.right != null){
stack.push(p.right);
}
```
```
if(p.left != null){
p.right = p.left;
p.left = null;
}else if(!stack.empty()){
TreeNode temp = stack.pop();
p.right=temp;
}
```
p = p.right;
}
}
}

586 | 677 Program Creek


## 235 Path Sum

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that
adding up all the values along the path equals the given sum.

For example: Given the below binary tree and sum = 22 ,

5
/ \
4 8
/ / \
11 13 4
/ \ \
7 2 1

return true, as there exist a root-to-leaf path 5 -> 4 -> 11 -> 2 which sum is 22.

**235.1 Java Solution 1 - Using Queue**

Add all node to a queue and store sum value of each node to another queue. When it
is a leaf node, check the stored sum value.
For the tree above, the queue would be: 5 - 4 - 8 - 11 - 13 - 4 - 7 - 2 - 1. It will check

node 13 , 7 , 2 and 1. This is a typical breadth first search(BFS) problem.

/**

* Definition for binary tree
* public class TreeNode {
* int val;
* TreeNode left;
* TreeNode right;
* TreeNode(int x) { val = x; }
* }
*/
public class Solution {
public boolean hasPathSum(TreeNode root, int sum) {
if(root == null) return false;

```
LinkedList<TreeNode> nodes = new LinkedList<TreeNode>();
LinkedList<Integer> values = new LinkedList<Integer>();
```
```
nodes.add(root);
values.add(root.val);
```
```
while(!nodes.isEmpty()){
```
587 | 677


235 Path Sum

```
TreeNode curr = nodes.poll();
int sumValue = values.poll();
```
```
if(curr.left == null && curr.right == null && sumValue==sum){
return true;
}
```
```
if(curr.left != null){
nodes.add(curr.left);
values.add(sumValue+curr.left.val);
}
```
```
if(curr.right != null){
nodes.add(curr.right);
values.add(sumValue+curr.right.val);
}
}
```
return false;
}
}

**235.2 Java Solution 2 - Recursion**

public boolean hasPathSum(TreeNode root, int sum) {
if (root == null)
return false;
if (root.val == sum && (root.left == null && root.right == null))
return true;

return hasPathSum(root.left, sum - root.val)
|| hasPathSum(root.right, sum - root.val);
}

Thanks to nebulaliang, this solution is wonderful!

588 | 677 Program Creek


## 236 Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path’s sum equals
the given sum.

For example, given the below binary tree and sum = 22 ,

5
/ \
4 8
/ / \
11 13 4
/ \ / \
7 2 5 1

the method returns the following:

[
[5,4,11,2],
[5,8,4,5]
]

**236.1 Analysis**

This problem can be converted to be a typical depth-first search problem. A recursive

depth-first search algorithm usually requires a recursive method call, a reference to
the final result, a temporary result, etc.

**236.2 Java Solution**

public List<ArrayList<Integer>> pathSum(TreeNode root, int sum) {
ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
if(root == null)
return result;

ArrayList<Integer> l = new ArrayList<Integer>();
l.add(root.val);
dfs(root, sum-root.val, result, l);
return result;
}

589 | 677


236 Path Sum II

public void dfs(TreeNode t, int sum, ArrayList<ArrayList<Integer>> result,
ArrayList<Integer> l){
if(t.left==null && t.right==null && sum==0){
ArrayList<Integer> temp = new ArrayList<Integer>();
temp.addAll(l);
result.add(temp);
}

```
//search path of left node
if(t.left != null){
l.add(t.left.val);
dfs(t.left, sum-t.left.val, result, l);
l.remove(l.size()-1);
}
```
//search path of right node
if(t.right!=null){
l.add(t.right.val);
dfs(t.right, sum-t.right.val, result, l);
l.remove(l.size()-1);
}
}

590 | 677 Program Creek


## 237 Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

**237.1 Analysis**

This problem can be illustrated by using a simple example.

in-order: 4 2 5 (1) 6 7 3 8
post-order: 4 5 2 6 7 8 3 (1)

From the post-order array, we know that last element is the root. We can find the
root in in-order array. Then we can identify the left and right sub-trees of the root
from in-order array.

Using the length of left sub-tree, we can identify left and right sub-trees in post-
order array. Recursively, we can build up the tree.

**237.2 Java Solution**

public TreeNode buildTree(int[] inorder, int[] postorder) {
int inStart = 0;
int inEnd = inorder.length - 1;
int postStart = 0;
int postEnd = postorder.length - 1;

return buildTree(inorder, inStart, inEnd, postorder, postStart, postEnd);
}

public TreeNode buildTree(int[] inorder, int inStart, int inEnd,
int[] postorder, int postStart, int postEnd) {

591 | 677


237 Construct Binary Tree from Inorder and Postorder Traversal

```
if (inStart > inEnd || postStart > postEnd)
return null;
```
```
int rootValue = postorder[postEnd];
TreeNode root = new TreeNode(rootValue);
```
```
int k = 0;
for (int i = 0; i < inorder.length; i++) {
if (inorder[i] == rootValue) {
k = i;
break;
}
}
```
```
root.left = buildTree(inorder, inStart, k - 1, postorder, postStart,
postStart + k - (inStart + 1));
// Becuase k is not the length, it it need to -(inStart+1) to get the length
root.right = buildTree(inorder, k + 1, inEnd, postorder, postStart + k-
inStart, postEnd - 1);
// postStart+k-inStart = postStart+k-(inStart+1) +1
```
return root;
}

592 | 677 Program Creek


## 238 Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

**238.1 Analysis**

Consider the following example:

in-order: 4 2 5 (1) 6 7 3 8
pre-order: (1) 2 4 5 3 7 6 8

From the pre-order array, we know that first element is the root. We can find the
root in in-order array. Then we can identify the left and right sub-trees of the root
from in-order array.

Using the length of left sub-tree, we can identify left and right sub-trees in pre-order
array. Recursively, we can build up the tree.

**238.2 Java Solution**

public TreeNode buildTree(int[] preorder, int[] inorder) {
int preStart = 0;
int preEnd = preorder.length-1;
int inStart = 0;
int inEnd = inorder.length-1;

return construct(preorder, preStart, preEnd, inorder, inStart, inEnd);
}

public TreeNode construct(int[] preorder, int preStart, int preEnd, int[]
inorder, int inStart, int inEnd){

593 | 677


238 Construct Binary Tree from Preorder and Inorder Traversal

```
if(preStart>preEnd||inStart>inEnd){
return null;
}
```
```
int val = preorder[preStart];
TreeNode p = new TreeNode(val);
```
```
//find parent element index from inorder
int k=0;
for(int i=0; i<inorder.length; i++){
if(val == inorder[i]){
k=i;
break;
}
}
```
```
p.left = construct(preorder, preStart+1, preStart+(k-inStart), inorder,
inStart, k-1);
p.right= construct(preorder, preStart+(k-inStart)+1, preEnd, inorder, k+1
, inEnd);
```
return p;
}

594 | 677 Program Creek


## 239 Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height
balanced BST.

**239.1 Java Solution**

A typical DFS problem using recursion.

// Definition for binary tree
class TreeNode {
int val;
TreeNode left;
TreeNode right;

TreeNode(int x) {
val = x;
}
}

public class Solution {
public TreeNode sortedArrayToBST(int[] num) {
if (num.length == 0)
return null;

```
return sortedArrayToBST(num, 0, num.length - 1);
}
```
```
public TreeNode sortedArrayToBST(int[] num, int start, int end) {
if (start > end)
return null;
```
```
int mid = (start + end) / 2;
TreeNode root = new TreeNode(num[mid]);
root.left = sortedArrayToBST(num, start, mid - 1);
root.right = sortedArrayToBST(num, mid + 1, end);
```
return root;
}
}

595 | 677



## 240 Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a
height balanced BST.

**240.1 Thoughts**

If you are given an array, the problem is quite straightforward. But things get a little

more complicated when you have a singly linked list instead of an array. Now you no
longer have random access to an element in O( 1 ) time. Therefore, you need to create
nodes bottom-up, and assign them to its parents. The bottom-up approach enables us
to access the list in its order at the same time as creating nodes.

**240.2 Java Solution**

// Definition for singly-linked list.
class ListNode {
int val;
ListNode next;

ListNode(int x) {
val = x;
next = null;
}
}

// Definition for binary tree
class TreeNode {
int val;
TreeNode left;
TreeNode right;

TreeNode(int x) {
val = x;
}
}

public class Solution {
static ListNode h;

597 | 677


240 Convert Sorted List to Binary Search Tree

```
public TreeNode sortedListToBST(ListNode head) {
if (head == null)
return null;
```
```
h = head;
int len = getLength(head);
return sortedListToBST(0, len - 1);
}
```
```
// get list length
public int getLength(ListNode head) {
int len = 0;
ListNode p = head;
```
```
while (p != null) {
len++;
p = p.next;
}
return len;
}
```
```
// build tree bottom-up
public TreeNode sortedListToBST(int start, int end) {
if (start > end)
return null;
```
```
// mid
int mid = (start + end) / 2;
```
```
TreeNode left = sortedListToBST(start, mid - 1);
TreeNode root = new TreeNode(h.val);
h = h.next;
TreeNode right = sortedListToBST(mid + 1, end);
```
```
root.left = left;
root.right = right;
```
return root;
}
}

598 | 677 Program Creek


## 241 Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.

**241.1 Thoughts**

LinkedList is a queue in Java. The add() and remove() methods are used to manipulate

the queue.

**241.2 Java Solution**

### /**

* Definition for binary tree
* public class TreeNode {
* int val;
* TreeNode left;
* TreeNode right;
* TreeNode(int x) { val = x; }
* }
*/
public class Solution {
public int minDepth(TreeNode root) {
if(root == null){
return 0;
}

```
LinkedList<TreeNode> nodes = new LinkedList<TreeNode>();
LinkedList<Integer> counts = new LinkedList<Integer>();
```
```
nodes.add(root);
counts.add(1);
```
```
while(!nodes.isEmpty()){
TreeNode curr = nodes.remove();
int count = counts.remove();
```
```
if(curr.left == null && curr.right == null){
return count;
}
```
599 | 677


241 Minimum Depth of Binary Tree

```
if(curr.left != null){
nodes.add(curr.left);
counts.add(count+1);
}
```
```
if(curr.right != null){
nodes.add(curr.right);
counts.add(count+1);
}
}
```
return 0;
}
}

600 | 677 Program Creek


## 242 Binary Tree Maximum Path Sum

Given a binary tree, find the maximum path sum. The path may start and end at any
node in the tree. For example, given the below binary tree

1
/ \
2 3

the result is 6.

**242.1 Analysis**

1 ) Recursively solve this problem 2 ) Get largest left sum and right sum 2 ) Compare to
the stored maximum

**242.2 Java Solution**

We can also use an array to store value for recursive methods.

public int maxPathSum(TreeNode root) {
int max[] = new int[1];
max[0] = Integer.MIN_VALUE;
calculateSum(root, max);
return max[0];
}

public int calculateSum(TreeNode root, int[] max) {
if (root == null)
return 0;

```
int left = calculateSum(root.left, max);
int right = calculateSum(root.right, max);
```
```
int current = Math.max(root.val, Math.max(root.val + left, root.val +
right));
```
```
max[0] = Math.max(max[0], Math.max(current, left + root.val + right));
```
return current;
}

601 | 677



## 243 Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.

**243.1 Analysis**

This is a typical tree problem that can be solve by using recursion.

**243.2 Java Solution**

// Definition for binary tree
class TreeNode {
int val;
TreeNode left;
TreeNode right;

TreeNode(int x) {
val = x;
}
}

public class Solution {
public boolean isBalanced(TreeNode root) {
if (root == null)
return true;

```
if (getHeight(root) == -1)
return false;
```
```
return true;
}
```
```
public int getHeight(TreeNode root) {
if (root == null)
return 0;
```
```
int left = getHeight(root.left);
int right = getHeight(root.right);
```
```
if (left == -1 || right == -1)
```
603 | 677


243 Balanced Binary Tree

```
return -1;
```
```
if (Math.abs(left - right) > 1) {
return -1;
}
```
```
return Math.max(left, right) + 1;
```
}
}

604 | 677 Program Creek


## 244 Symmetric Tree

**244.1 Problem**

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its

center).
For example, this binary tree is symmetric:

1
/ \
2 2
/ \ / \
3 4 4 3

But the following is not:

1
/ \
2 2
\ \
3 3

**244.2 Java Solution - Recursion**

This problem can be solve by using a simple recursion. The key is finding the con-
ditions that return false, such as value is not equal, only one node(left or right) has
value.

public boolean isSymmetric(TreeNode root) {
if (root == null)
return true;
return isSymmetric(root.left, root.right);
}

public boolean isSymmetric(TreeNode l, TreeNode r) {
if (l == null && r == null) {
return true;
} else if (r == null || l == null) {
return false;
}

```
if (l.val != r.val)
```
605 | 677


244 Symmetric Tree

```
return false;
```
```
if (!isSymmetric(l.left, r.right))
return false;
if (!isSymmetric(l.right, r.left))
return false;
```
return true;
}

606 | 677 Program Creek


## 245 Binary Search Tree Iterator

**245.1 Problem**

Implement an iterator over a binary search tree (BST). Your iterator will be initialized
with the root node of a BST. Calling next() will return the next smallest number in
the BST. Note: next() and hasNext() should run in average O( 1 ) time and uses O(h)

memory, where h is the height of the tree.

**245.2 Java Solution**

The key to solve this problem is understanding the features of BST. Here is an example
BST.

### /**

```
* Definition for binary tree
* public class TreeNode {
* int val;
* TreeNode left;
* TreeNode right;
* TreeNode(int x) { val = x; }
* }
*/
```
public class BSTIterator {
Stack<TreeNode> stack;

607 | 677


245 Binary Search Tree Iterator

```
public BSTIterator(TreeNode root) {
stack = new Stack<TreeNode>();
while (root != null) {
stack.push(root);
root = root.left;
}
}
```
```
public boolean hasNext() {
return !stack.isEmpty();
}
```
public int next() {
TreeNode node = stack.pop();
int result = node.val;
if (node.right != null) {
node = node.right;
while (node != null) {
stack.push(node);
node = node.left;
}
}
return result;
}
}

608 | 677 Program Creek


## 246 Binary Tree Right Side View Contents

Given a binary tree, imagine yourself standing on the right side of it, return the values
of the nodes you can see ordered from top to bottom. For example, given the following
binary tree,

1 <---
/ \
2 3 <---
\
5 <---

You can see [ 1 , 3 , 5 ].

**246.1 Analysis**

This problem can be solve by using a queue. On each level of the tree, we add the
right-most element to the results.

**246.2 Java Solution**

public List<Integer> rightSideView(TreeNode root) {
ArrayList<Integer> result = new ArrayList<Integer>();

```
if(root == null) return result;
```
```
LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
queue.add(root);
```
```
while(queue.size() > 0){
//get size here
int size = queue.size();
```
```
for(int i=0; i<size; i++){
TreeNode top = queue.remove();
```
```
//the first element in the queue (right-most of the tree)
if(i==0){
result.add(top.val);
}
//add right first
if(top.right != null){
```
609 | 677


246 Binary Tree Right Side View

```
queue.add(top.right);
}
//add left
if(top.left != null){
queue.add(top.left);
}
}
}
```
return result;
}

610 | 677 Program Creek


## 247 Lowest Common Ancestor of a Binary Search Tree

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given
nodes in the BST.

**247.1 Analysis**

This problem can be solved by using BST property, i.e., left <parent <right for each
node. There are 3 cases to handle.

**247.2 Java Solution**

public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
TreeNode m = root;

```
if(m.val > p.val && m.val < q.val){
return m;
}else if(m.val>p.val && m.val > q.val){
return lowestCommonAncestor(root.left, p, q);
}else if(m.val<p.val && m.val < q.val){
return lowestCommonAncestor(root.right, p, q);
}
```
return root;
}

611 | 677



## 248 Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the
tree.

**248.1 Java Solution 1**

public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
if(root==null)
return null;

```
if(root==p || root==q)
return root;
```
```
TreeNode l = lowestCommonAncestor(root.left, p, q);
TreeNode r = lowestCommonAncestor(root.right, p, q);
```
if(l!=null&&r!=null){
return root;
}else if(l==null&&r==null){
return null;
}else{
return l==null?r:l;
}
}

To calculate time complexity, we know that f(n)= 2 *f(n- 1 )= 2 * 2 *f(n- 2 )= 2 ˆ(logn), so time=O(n).

**248.2 Java Solution 2 - deprecated**

Please use the following diagram to walk through the solution.

613 | 677


248 Lowest Common Ancestor of a Binary Tree

Since each node is visited in the worst case, time complexity is O(n).

class Entity{
public int count;
public TreeNode node;

public Entity(int count, TreeNode node){
this.count = count;
this.node = node;
}
}

public class Solution {
public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode
q) {
return lcaHelper(root, p, q).node;
}

```
public Entity lcaHelper(TreeNode root, TreeNode p, TreeNode q){
if(root == null) return new Entity(0, null);
```
```
Entity left = lcaHelper(root.left, p, q);
if(left.count==2)
return left;
```
```
Entity right = lcaHelper(root.right,p,q);
if(right.count==2)
return right;
```
614 | 677 Program Creek


```
248 Lowest Common Ancestor of a Binary Tree
```
```
int numTotal = left.count + right.count;
if(root== p || root == q){
numTotal++;
}
```
return new Entity(numTotal, root);
}
}

Program Creek 615 | 677



## 249 Verify Preorder Serialization of a Binary Tree

One way to serialize a binary tree is to use pre-order traversal. When we encounter
a non-null node, we record the node’s value. If it is a null node, we record using a
sentinel value such as #.

9
/ \
3 2
/ \ / \
4 1 # 6
/ \ / \ / \
# # # # # #

For example, the above binary tree can be serialized to the string " 9 , 3 , 4 ,#,#, 1 ,#,#, 2 ,#, 6 ,#,#",
where # represents a null node.
Given a string of comma separated values, verify whether it is a correct preorder
traversal serialization of a binary tree. Find an algorithm without reconstructing the

tree.

**249.1 Java Solution - Stack**

We can keep removing the leaf node until there is no one to remove. If a sequence
is like " 4 # #", change it to "#" and continue. We need a stack so that we can record
previous removed nodes.

617 | 677


249 Verify Preorder Serialization of a Binary Tree

public boolean isValidSerialization(String preorder) {
LinkedList<String> stack = new LinkedList<String>();
String[] arr = preorder.split(",");

```
for(int i=0; i<arr.length; i++){
stack.add(arr[i]);
```
```
while(stack.size()>=3
&& stack.get(stack.size()-1).equals("#")
&& stack.get(stack.size()-2).equals("#")
&& !stack.get(stack.size()-3).equals("#")){
```
```
stack.remove(stack.size()-1);
stack.remove(stack.size()-1);
stack.remove(stack.size()-1);
```
```
stack.add("#");
}
```
```
}
```
if(stack.size()==1 && stack.get(0).equals("#"))
return true;
else
return false;
}

618 | 677 Program Creek


## 250 Populating Next Right Pointers in Each Node

Given the following perfect binary tree,

1
/ \
2 3
/ \ / \
4 5 6 7

After calling your function, the tree should look like:

1 -> NULL
/ \
2 -> 3 -> NULL
/ \ / \
4->5->6->7 -> NULL

**250.1 Java Solution 1 - Simple**

public void connect(TreeLinkNode root) {
if(root==null)
return;

```
LinkedList<TreeLinkNode> nodeQueue = new LinkedList<TreeLinkNode>();
LinkedList<Integer> depthQueue = new LinkedList<Integer>();
```
```
if(root!=null){
nodeQueue.offer(root);
depthQueue.offer(1);
}
```
```
while(!nodeQueue.isEmpty()){
TreeLinkNode topNode = nodeQueue.poll();
int depth = depthQueue.poll();
```
```
if(depthQueue.isEmpty()){
topNode.next = null;
}else if(depthQueue.peek()>depth){
topNode.next = null;
```
619 | 677


250 Populating Next Right Pointers in Each Node

```
}else{
topNode.next = nodeQueue.peek();
}
```
```
if(topNode.left!=null){
nodeQueue.offer(topNode.left);
depthQueue.offer(depth+1);
}
```
if(topNode.right!=null){
nodeQueue.offer(topNode.right);
depthQueue.offer(depth+1);
}
}
}

**250.2 Java Solution 2**

This solution is easier to understand. You can use the example tree above to walk

through the algorithm. The basic idea is have 4 pointers to move towards right on two
levels (see comments in the code).

public void connect(TreeLinkNode root) {
if(root == null)
return;

```
TreeLinkNode lastHead = root;//prevous level’s head
TreeLinkNode lastCurrent = null;//previous level’s pointer
TreeLinkNode currentHead = null;//currnet level’s head
TreeLinkNode current = null;//current level’s pointer
```
```
while(lastHead!=null){
lastCurrent = lastHead;
```
620 | 677 Program Creek


```
250 Populating Next Right Pointers in Each Node
```
```
while(lastCurrent!=null){
if(currentHead == null){
currentHead = lastCurrent.left;
current = lastCurrent.left;
}else{
current.next = lastCurrent.left;
current = current.next;
}
```
```
if(currentHead != null){
current.next = lastCurrent.right;
current = current.next;
}
```
```
lastCurrent = lastCurrent.next;
}
```
```
//update last head
lastHead = currentHead;
currentHead = null;
}
```
}

Program Creek 621 | 677



## 251 Populating Next Right Pointers in Each Node II

Follow up for problem "Populating Next Right Pointers in Each Node".
What if the given tree could be any binary tree? Would your previous solution still
work?

**251.1 Analysis**

Similar to Populating Next Right Pointers in Each Node, we have 4 pointers at 2 levels
of the tree.

**251.2 Java Solution**

public void connect(TreeLinkNode root) {
if(root == null)
return;

```
TreeLinkNode lastHead = root;//prevous level’s head
TreeLinkNode lastCurrent = null;//previous level’s pointer
TreeLinkNode currentHead = null;//currnet level’s head
TreeLinkNode current = null;//current level’s pointer
```
```
while(lastHead!=null){
lastCurrent = lastHead;
```
```
while(lastCurrent!=null){
//left child is not null
if(lastCurrent.left!=null) {
```
623 | 677


251 Populating Next Right Pointers in Each Node II

```
if(currentHead == null){
currentHead = lastCurrent.left;
current = lastCurrent.left;
}else{
current.next = lastCurrent.left;
current = current.next;
}
}
```
```
//right child is not null
if(lastCurrent.right!=null){
if(currentHead == null){
currentHead = lastCurrent.right;
current = lastCurrent.right;
}else{
current.next = lastCurrent.right;
current = current.next;
}
}
```
```
lastCurrent = lastCurrent.next;
}
```
//update last head
lastHead = currentHead;
currentHead = null;
}
}

624 | 677 Program Creek


## 252 Unique Binary Search Trees

Given n, how many structurally unique BST’s (binary search trees) that store values

1 ...n?
For example, Given n = 3 , there are a total of 5 unique BST’s.

1 3 3 2 1
\ / / / \ \
3 2 1 1 3 2
/ / \ \
2 1 2 3

**252.1 Analysis**

Let count[i] be the number of unique binary search trees for i. The number of trees are
determined by the number of subtrees which have different root node. For example,

i=0, count[0]=1 //empty tree

i=1, count[1]=1 //one tree

i=2, count[2]=count[0]*count[1] // 0 is root
+ count[1]*count[0] // 1 is root

i=3, count[3]=count[0]*count[2] // 1 is root
+ count[1]*count[1] // 2 is root
+ count[2]*count[0] // 3 is root

i=4, count[4]=count[0]*count[3] // 1 is root
+ count[1]*count[2] // 2 is root
+ count[2]*count[1] // 3 is root
+ count[3]*count[0] // 4 is root
..
..
..

i=n, count[n] = sum(count[0..k]*count[k+1...n]) 0 <= k < n-1

Use dynamic programming to solve the problem.

**252.2 Java Solution**

625 | 677


252 Unique Binary Search Trees

public int numTrees(int n) {
int[] count = new int[n + 1];

```
count[0] = 1;
count[1] = 1;
```
```
for (int i = 2; i <= n; i++) {
for (int j = 0; j <= i - 1; j++) {
count[i] = count[i] + count[j]* count[i - j - 1];
}
}
```
return count[n];
}

Check out how to get all unique binary search trees.

626 | 677 Program Creek


## 253 Unique Binary Search Trees II

Given n, generate all structurally unique BST’s (binary search trees) that store values
1 ...n.

For example, Given n = 3 , your program should return all 5 unique BST’s shown
below.

1 3 3 2 1
\ / / / \ \
3 2 1 1 3 2
/ / \ \
2 1 2 3

**253.1 Analysis**

Check out Unique Binary Search Trees I.
This problem can be solved by recursively forming left and right subtrees. The

different combinations of left and right subtrees form the set of all unique binary
search trees.

**253.2 Java Solution**

public List<TreeNode> generateTrees(int n) {
if(n==0){
return new ArrayList<TreeNode>();
}

return helper(1, n);
}

public List<TreeNode> helper(int m, int n){
List<TreeNode> result = new ArrayList<TreeNode>();
if(m>n){
result.add(null);
return result;
}

```
for(int i=m; i<=n; i++){
List<TreeNode> ls = helper(m, i-1);
List<TreeNode> rs = helper(i+1, n);
```
627 | 677


253 Unique Binary Search Trees II

```
for(TreeNode l: ls){
for(TreeNode r: rs){
TreeNode curr = new TreeNode(i);
curr.left=l;
curr.right=r;
result.add(curr);
}
}
}
```
return result;
}

628 | 677 Program Creek


## 254 Sum Root to Leaf Numbers

Given a binary tree containing digits from 0 - 9 only, each root-to-leaf path could repre-
sent a number. Find the total sum of all root-to-leaf numbers.

For example,

1
/ \
2 3

The root-to-leaf path 1 -> 2 represents the number 12. The root-to-leaf path 1 -> 3
represents the number 13. Return the sum = 12 + 13 = 25.

**254.1 Java Solution - Recursive**

This problem can be solved by a typical DFS approach.

public int sumNumbers(TreeNode root) {
int result = 0;
if(root==null)
return result;

```
ArrayList<ArrayList<TreeNode>> all = new ArrayList<ArrayList<TreeNode>>();
ArrayList<TreeNode> l = new ArrayList<TreeNode>();
l.add(root);
dfs(root, l, all);
```
```
for(ArrayList<TreeNode> a: all){
StringBuilder sb = new StringBuilder();
for(TreeNode n: a){
sb.append(String.valueOf(n.val));
}
int currValue = Integer.valueOf(sb.toString());
result = result + currValue;
}
```
return result;
}

public void dfs(TreeNode n, ArrayList<TreeNode> l,
ArrayList<ArrayList<TreeNode>> all){
if(n.left==null && n.right==null){
ArrayList<TreeNode> t = new ArrayList<TreeNode>();

629 | 677


254 Sum Root to Leaf Numbers

```
t.addAll(l);
all.add(t);
}
```
```
if(n.left!=null){
l.add(n.left);
dfs(n.left, l, all);
l.remove(l.size()-1);
}
```
```
if(n.right!=null){
l.add(n.right);
dfs(n.right, l, all);
l.remove(l.size()-1);
}
```
}

Same approach, but simpler coding style.

public int sumNumbers(TreeNode root) {
if(root == null)
return 0;

return dfs(root, 0, 0);
}

public int dfs(TreeNode node, int num, int sum){
if(node == null) return sum;

```
num = num*10 + node.val;
```
```
// leaf
if(node.left == null && node.right == null) {
sum += num;
return sum;
}
```
// left subtree + right subtree
sum = dfs(node.left, num, sum) + dfs(node.right, num, sum);
return sum;
}


## 255 Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

**255.1 Analysis**

Steps to solve this problem: 1 ) get the height of left-most part 2 ) get the height of

right-most part 3 ) when they are equal, the # of nodes = 2 h -ˆ 1 4) when they are not
equal, recursively get # of nodes from left&right sub-trees

Time complexity is O(h 2 ˆ).

**255.2 Java Solution**

public int countNodes(TreeNode root) {
if(root==null)
return 0;

```
int left = getLeftHeight(root)+1;
int right = getRightHeight(root)+1;
```
631 | 677


255 Count Complete Tree Nodes

if(left==right){
return (2<<(left-1))-1;
}else{
return countNodes(root.left)+countNodes(root.right)+1;
}
}

public int getLeftHeight(TreeNode n){
if(n==null) return 0;

int height=0;
while(n.left!=null){
height++;
n = n.left;
}
return height;
}

public int getRightHeight(TreeNode n){
if(n==null) return 0;

int height=0;
while(n.right!=null){
height++;
n = n.right;
}
return height;
}

632 | 677 Program Creek


## 256 Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST
that is closest to the target.

**256.1 Java Solution 1 - Recursion**

Recursively traverse down the root. When target is less than root, go left; when target
is greater than root, go right.

public class Solution {
int goal;
double min = Double.MAX_VALUE;

```
public int closestValue(TreeNode root, double target) {
helper(root, target);
return goal;
}
```
```
public void helper(TreeNode root, double target){
if(root==null)
return;
```
```
if(Math.abs(root.val - target) < min){
min = Math.abs(root.val-target);
goal = root.val;
}
```
if(target < root.val){
helper(root.left, target);
}else{
helper(root.right, target);
}
}
}

**256.2 Java Solution 2 - Iteration**

public int closestValue(TreeNode root, double target) {
double min=Double.MAX_VALUE;
int result = root.val;

633 | 677


256 Closest Binary Search Tree Value

```
while(root!=null){
if(target>root.val){
```
```
double diff = Math.abs(root.val-target);
if(diff<min){
min = Math.min(min, diff);
result = root.val;
}
root = root.right;
}else if(target<root.val){
```
```
double diff = Math.abs(root.val-target);
if(diff<min){
min = Math.min(min, diff);
result = root.val;
}
root = root.left;
}else{
return root.val;
}
}
```
return result;
}

634 | 677 Program Creek


## 257 Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.

**257.1 Java Solution**

A typical depth-first search problem.

public List<String> binaryTreePaths(TreeNode root) {
ArrayList<String> finalResult = new ArrayList<String>();

```
if(root==null)
return finalResult;
```
```
ArrayList<String> curr = new ArrayList<String>();
ArrayList<ArrayList<String>> results = new ArrayList<ArrayList<String>>();
```
```
dfs(root, results, curr);
```
```
for(ArrayList<String> al : results){
StringBuilder sb = new StringBuilder();
sb.append(al.get(0));
for(int i=1; i<al.size();i++){
sb.append("->"+al.get(i));
}
```
```
finalResult.add(sb.toString());
}
```
return finalResult;
}

public void dfs(TreeNode root, ArrayList<ArrayList<String>> list,
ArrayList<String> curr){
curr.add(String.valueOf(root.val));

```
if(root.left==null && root.right==null){
list.add(curr);
return;
}
```
```
if(root.left!=null){
ArrayList<String> temp = new ArrayList<String>(curr);
dfs(root.left, list, temp);
```
635 | 677


257 Binary Tree Paths

### }

if(root.right!=null){
ArrayList<String> temp = new ArrayList<String>(curr);
dfs(root.right, list, temp);
}
}

636 | 677 Program Creek


## 258 Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

**258.1 Java Solution**

public int maxDepth(TreeNode root) {
if(root==null)
return 0;

```
int leftDepth = maxDepth(root.left);
int rightDepth = maxDepth(root.right);
```
```
int bigger = Math.max(leftDepth, rightDepth);
```
return bigger+1;
}

637 | 677



## 259 Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake. Recover the tree

without changing its structure.

**259.1 Java Solution**

Inorder traveral will return values in an increasing order. So if an element is less than

its previous element,the previous element is a swapped node.

public class Solution {
TreeNode first;
TreeNode second;
TreeNode pre;

```
public void inorder(TreeNode root){
if(root==null)
return;
```
```
inorder(root.left);
```
```
if(pre==null){
pre=root;
}else{
if(root.val<pre.val){
if(first==null){
first=pre;
}
```
```
second=root;
}
pre=root;
}
```
```
inorder(root.right);
}
```
```
public void recoverTree(TreeNode root) {
if(root==null)
return;
```
```
inorder(root);
if(second!=null && first !=null){
```
639 | 677


259 Recover Binary Search Tree

```
int val = second.val;
second.val = first.val;
first.val = val;
}
```
}
}

640 | 677 Program Creek


## 260 Same Tree

Two binary trees are considered the same if they have identical structure and nodes
have the same value.
This problem can be solved by using a simple recursive function.

public boolean isSameTree(TreeNode p, TreeNode q) {
if(p==null && q==null){
return true;
}else if(p==null || q==null){
return false;
}

if(p.val==q.val){
return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}else{
return false;
}
}

641 | 677



## 261 Serialize and Deserialize Binary Tree

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on
how your serialization/deserialization algorithm should work. You just need to ensure
that a binary tree can be serialized to a string and this string can be deserialized to the
original tree structure.

**261.1 Java Solution 1 - Level Order Traveral**

// Encodes a tree to a single string.
public String serialize(TreeNode root) {
if(root==null){
return "";
}

```
StringBuilder sb = new StringBuilder();
```
```
LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
```
```
queue.add(root);
while(!queue.isEmpty()){
TreeNode t = queue.poll();
if(t!=null){
sb.append(String.valueOf(t.val) + ",");
queue.add(t.left);
queue.add(t.right);
}else{
sb.append("#,");
}
}
```
sb.deleteCharAt(sb.length()-1);
System.out.println(sb.toString());
return sb.toString();
}

// Decodes your encoded data to tree.
public TreeNode deserialize(String data) {
if(data==null || data.length()==0)
return null;

```
String[] arr = data.split(",");
```
643 | 677


261 Serialize and Deserialize Binary Tree

```
TreeNode root = new TreeNode(Integer.parseInt(arr[0]));
```
```
LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
queue.add(root);
```
```
int i=1;
while(!queue.isEmpty()){
TreeNode t = queue.poll();
```
```
if(t==null)
continue;
```
```
if(!arr[i].equals("#")){
t.left = new TreeNode(Integer.parseInt(arr[i]));
queue.offer(t.left);
```
```
}else{
t.left = null;
queue.offer(null);
}
i++;
```
```
if(!arr[i].equals("#")){
t.right = new TreeNode(Integer.parseInt(arr[i]));
queue.offer(t.right);
```
```
}else{
t.right = null;
queue.offer(null);
}
i++;
}
```
return root;
}

**261.2 Java Solution 2 - Preorder Traversal**

// Encodes a tree to a single string.
public String serialize(TreeNode root) {
if(root==null)
return null;

```
Stack<TreeNode> stack = new Stack<TreeNode>();
stack.push(root);
StringBuilder sb = new StringBuilder();
```
644 | 677 Program Creek


```
261 Serialize and Deserialize Binary Tree
```
```
while(!stack.isEmpty()){
TreeNode h = stack.pop();
if(h!=null){
sb.append(h.val+",");
stack.push(h.right);
stack.push(h.left);
}else{
sb.append("#,");
}
}
```
return sb.toString().substring(0, sb.length()-1);
}

// Decodes your encoded data to tree.
public TreeNode deserialize(String data) {
if(data == null)
return null;

```
int[] t = {0};
String[] arr = data.split(",");
```
return helper(arr, t);
}

public TreeNode helper(String[] arr, int[] t){
if(arr[t[0]].equals("#")){
return null;
}

```
TreeNode root = new TreeNode(Integer.parseInt(arr[t[0]]));
```
```
t[0]=t[0]+1;
root.left = helper(arr, t);
t[0]=t[0]+1;
root.right = helper(arr, t);
```
return root;
}

Program Creek 645 | 677



## 262 Inorder Successor in BST

Given a binary search tree and a node in it, find the in-order successor of that node in

the BST.

**262.1 Java Solution 1**

public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
Stack<TreeNode> stack = new Stack<TreeNode>();
if(root==null || p==null)
return null;

```
stack.push(root);
boolean isNext = false;
while(!stack.isEmpty()){
TreeNode top = stack.pop();
```
```
if(top.right==null&&top.left==null){
if(isNext){
return top;
}
```
```
if(p.val==top.val){
isNext = true;
}
continue;
}
```
```
if(top.right!=null){
stack.push(top.right);
top.right=null;
}
```
```
stack.push(top);
```
```
if(top.left!=null){
stack.push(top.left);
top.left=null;
}
}
```
return null;
}

647 | 677


262 Inorder Successor in BST

Time is O(n), Space is O(n).

**262.2 Java Solution 2**

public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
if(root==null)
return null;

```
TreeNode next = null;
TreeNode c = root;
while(c!=null && c.val!=p.val){
if(c.val > p.val){
next = c;
c = c.left;
}else{
c= c.right;
}
}
```
```
if(c==null)
return null;
```
```
if(c.right==null)
return next;
```
```
c = c.right;
while(c.left!=null)
c = c.left;
```
return c;
}

Time is O(log(n)) and space is O( 1 ).

648 | 677 Program Creek


## 263 Find Leaves of Binary Tree

Given a binary tree, collect a tree’s nodes as if you were doing this: Collect and remove
all leaves, repeat until the tree is empty.

Example: Given binary tree

1
/ \
2 3
/ \
4 5

Returns [ 4 , 5 , 3 ], [ 2 ], [ 1 ].

**263.1 Java Solution**

The key to solve this problem is converting the problem to be finding the index of the
element in the result list. Then this is a typical DFS problem on trees.

public List<List<Integer>> findLeaves(TreeNode root) {
List<List<Integer>> result = new ArrayList<List<Integer>>();
helper(result, root);
return result;
}

// traverse the tree bottom-up recursively
private int helper(List<List<Integer>> list, TreeNode root){
if(root==null)
return -1;

```
int left = helper(list, root.left);
int right = helper(list, root.right);
int curr = Math.max(left, right)+1;
```
```
// the first time this code is reached is when curr==0,
//since the tree is bottom-up processed.
if(list.size()<=curr){
list.add(new ArrayList<Integer>());
}
```
```
list.get(curr).add(root.val);
```
```
return curr;
```
649 | 677


263 Find Leaves of Binary Tree

### }

650 | 677 Program Creek


## 264 Largest BST Subtree

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where

largest means subtree with largest number of nodes in it.

**264.1 Java Solution**

class Wrapper{
int size;
int lower, upper;
boolean isBST;

public Wrapper(){
lower = Integer.MAX_VALUE;
upper = Integer.MIN_VALUE;
isBST = false;
size = 0;
}
}
public class Solution {
public int largestBSTSubtree(TreeNode root) {
return helper(root).size;
}

```
public Wrapper helper(TreeNode node){
Wrapper curr = new Wrapper();
```
```
if(node == null){
curr.isBST= true;
return curr;
}
```
```
Wrapper l = helper(node.left);
Wrapper r = helper(node.right);
```
```
//current subtree’s boundaries
curr.lower = Math.min(node.val, l.lower);
curr.upper = Math.max(node.val, r.upper);
```
```
//check left and right subtrees are BST or not
//check left’s upper again current’s value and right’s lower against
current’s value
if(l.isBST && r.isBST && l.upper<=node.val && r.lower>=node.val){
```
651 | 677


264 Largest BST Subtree

```
curr.size = l.size+r.size+1;
curr.isBST = true;
}else{
curr.size = Math.max(l.size, r.size);
curr.isBST = false;
}
```
return curr;
}
}

652 | 677 Program Creek


## 265 Single Number

The problem:
Given an array of integers, every element appears twice except for one. Find that single
one.

**265.1 Java Solution 1**

The key to solve this problem is bit manipulation. XOR will return 1 only on two
different bits. So if two numbers are the same, XOR will return 0. Finally only one
number left.

public int singleNumber(int[] A) {
int x = 0;
for (int a : A) {
x = x ^ a;
}
return x;
}

**265.2 Java Solution 2**

public int singleNumber(int[] A) {
HashSet<Integer> set = new HashSet<Integer>();
for (int n : A) {
if (!set.add(n))
set.remove(n);
}
Iterator<Integer> it = set.iterator();
return it.next();
}

The question now is do you know any other ways to do this?

653 | 677



## 266 Single Number II

**266.1 Problem**

Given an array of integers, every element appears three times except for one. Find that

single one.

**266.2 Java Solution**

This problem is similar to Single Number.

public int singleNumber(int[] A) {
int ones = 0, twos = 0, threes = 0;
for (int i = 0; i < A.length; i++) {
twos |= ones & A[i];
ones ^= A[i];
threes = ones & twos;
ones &= ~threes;
twos &= ~threes;
}
return ones;
}

655 | 677



## 267 Twitter Codility Problem Max Binary Gap

Problem: Get maximum binary Gap.
For example, 9 ’s binary form is 1001 , the gap is 2.

**267.1 Java Solution 1**

An integer x & 1 will get the last digit of the integer.

public static int getGap(int N) {
int max = 0;
int count = -1;
int r = 0;

```
while (N > 0) {
// get right most bit & shift right
r = N & 1;
N = N >> 1;
```
```
if (0 == r && count >= 0) {
count++;
}
```
```
if (1 == r) {
max = count > max? count : max;
count = 0;
}
}
```
return max;
}

Time is O(n).

**267.2 Java Solution 2**

public static int getGap(int N) {
int pre = -1;
int len = 0;

657 | 677


267 Twitter Codility Problem Max Binary Gap

```
while (N > 0) {
int k = N & -N;
```
```
int curr = (int) Math.log(k);
```
```
N = N & (N - 1);
```
```
if (pre != -1 && Math.abs(curr - pre) > len) {
len = Math.abs(curr - pre) + 1;
}
pre = curr;
}
```
return len;
}

Time is O(log(n)).

658 | 677 Program Creek


## 268 Number of 1 Bits

**268.1 Problem**

Write a function that takes an unsigned integer and returns the number of ’ 1 ’ bits it

has (also known as the Hamming weight).
For example, the 32 -bit integer ’ 11 ’ has binary representation 00000000000000000000000000001011 ,
so the function should return 3.

**268.2 Java Solution**

public int hammingWeight(int n) {
int count = 0;
for(int i=1; i<33; i++){
if(getBit(n, i) == true){
count++;
}
}
return count;
}

public boolean getBit(int n, int i){
return (n & (1 << i)) != 0;
}

659 | 677



## 269 Reverse Bits

**269.1 Problem**

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100 ),
return 964176192 (represented in binary as 00111001011110000010100101000000 ).
Follow up: If this function is called many times, how would you optimize it?
Related problem: Reverse Integer

**269.2 Java Solution**

public int reverseBits(int n) {
for (int i = 0; i < 16; i++) {
n = swapBits(n, i, 32 - i - 1);
}

return n;
}

public int swapBits(int n, int i, int j) {
int a = (n >> i) & 1;
int b = (n >> j) & 1;

```
if ((a ^ b) != 0) {
return n ^= (1 << i) | (1 << j);
}
```
return n;
}

661 | 677



## 270 Repeated DNA Sequences

**270.1 Problem**

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for
example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify
repeated sequences within the DNA.

Write a function to find all the 10 -letter-long sequences (substrings) that occur more
than once in a DNA molecule.
For example, given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT", re-

turn: ["AAAAACCCCC", "CCCCCAAAAA"].

**270.2 Java Solution**

The key to solve this problem is that each of the 4 nucleotides can be stored in 2 bits.

So the 10 -letter-long sequence can be converted to 20 -bits-long integer. The following
is a Java solution. You may use an example to manually execute the program and see
how it works.

public List<String> findRepeatedDnaSequences(String s) {
List<String> result = new ArrayList<String>();

```
int len = s.length();
if (len < 10) {
return result;
}
```
```
Map<Character, Integer> map = new HashMap<Character, Integer>();
map.put(’A’, 0);
map.put(’C’, 1);
map.put(’G’, 2);
map.put(’T’, 3);
```
```
Set<Integer> temp = new HashSet<Integer>();
Set<Integer> added = new HashSet<Integer>();
```
```
int hash = 0;
for (int i = 0; i < len; i++) {
if (i < 9) {
//each ACGT fit 2 bits, so left shift 2
hash = (hash << 2) + map.get(s.charAt(i));
} else {
```
663 | 677


270 Repeated DNA Sequences

```
hash = (hash << 2) + map.get(s.charAt(i));
//make length of hash to be 20
hash = hash & (1 << 20) - 1;
```
```
if (temp.contains(hash) && !added.contains(hash)) {
result.add(s.substring(i - 9, i + 1));
added.add(hash); //track added
} else {
temp.add(hash);
}
}
```
```
}
```
return result;
}

664 | 677 Program Creek


## 271 Bitwise AND of Numbers Range Contents

**271.1 Given a range [m, n] where 0 <= m <= n <=**

```
2147483647, return the bitwise AND of all numbers
in this range, inclusive. For example, given the
range [5, 7], you should return 4. Java Solution
```
The key to solve this problem is bitwise AND consecutive numbers. You can use the
following example to walk through the code.

8 4 2 1
---------------
5 | 0 1 0 1
6 | 0 1 1 0
7 | 0 1 1 1

public int rangeBitwiseAnd(int m, int n) {
while (n > m) {
n = n & n - 1;
}
return m & n;
}

665 | 677



## 272 Sum of Two Integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator
+ and -.
Example: Given a = 1 and b = 2 , return 3.

**272.1 Java Solution**

Given two numbers a and b, a&b returns the number formed by ’ 1 ’ bits on a and b.
When it is left shifted by 1 bit, it is the carry.
For example, given a= 101 and b= 111 (in binary), the a&b= 101. a&b « 1 = 1010.
ab is the number formed by different bits of a and b. a&b=ˆ 10.

public int getSum(int a, int b) {

```
while(b!=0){
int c = a&b;
a=a^b;
b=c<<1;
}
```
return a;
}

667 | 677



## 273 Counting Bits

Given a non negative integer number num. For every numbers i in the range 0 ≤i≤
num calculate the number of 1 ’s in their binary representation and return them as an

array.

```
Example:
For num = 5 you should return [ 0 , 1 , 1 , 2 , 1 , 2 ].
```
**273.1 Naive Solution**

We can simply count bits for each number like the following:

public int[] countBits(int num) {
int[] result = new int[num+1];

```
for(int i=0; i<=num; i++){
result[i] = countEach(i);
}
```
return result;
}

public int countEach(int num){
int result = 0;

```
while(num!=0){
if(num%2==1){
result++;
}
num = num/2;
}
```
return result;
}

**273.2 Improved Solution**

For number 2 ( 10 ), 4 ( 100 ), 8 ( 1000 ), 16 ( 10000 ), ..., the number of 1 ’s is 1. Any other

number can be converted to be 2 m + x. For example,ˆ 9 = 8 + 1 , 10 = 8 + 2. The number of
1 ’s for any other number is 1 + # of 1 ’s in x.

669 | 677


273 Counting Bits

public int[] countBits(int num) {
int[] result = new int[num+1];

```
int p = 1; //p tracks the index for number x
int pow = 1;
for(int i=1; i<=num; i++){
if(i==pow){
result[i] = 1;
pow <<= 1;
p = 1;
}else{
result[i] = result[p]+1;
p++;
}
```
```
}
```
return result;
}

670 | 677 Program Creek


## 274 Maximum Product of Word Lengths

Given a string array words, find the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. You may assume that each word
will contain only lower case letters. If no such two words exist, return 0.

**274.1 Java Solution**

public int maxProduct(String[] words) {
if(words==null || words.length==0)
return 0;

```
int[] arr = new int[words.length];
for(int i=0; i<words.length; i++){
for(int j=0; j<words[i].length(); j++){
char c = words[i].charAt(j);
arr[i] |= (1<< (c-’a’));
}
}
```
```
int result = 0;
```
```
for(int i=0; i<words.length; i++){
for(int j=i+1; j<words.length; j++){
if((arr[i] & arr[j]) == 0){
result = Math.max(result, words[i].length()*words[j].length());
}
}
}
```
return result;
}

671 | 677



## 275 Gray Code

The gray code is a binary numeral system where two successive values differ in only
one bit.
Given a non-negative integer n representing the total number of bits in the code,
print the sequence of gray code. A gray code sequence must begin with 0.

```
For example, given n = 2 , return [ 0 , 1 , 3 , 2 ]. Its gray code sequence is:
00 - 0 01-1 11-3 10- 2
```
**275.1 Java Solution**

public List<Integer> grayCode(int n) {
if(n==0){
List<Integer> result = new ArrayList<Integer>();
result.add(0);
return result;
}

```
List<Integer> result = grayCode(n-1);
int numToAdd = 1<<(n-1);
```
```
for(int i=result.size()-1; i>=0; i--){
result.add(numToAdd+result.get(i));
}
```
return result;
}

673 | 677



## 276 Pow(x, n)

Problem:
Implement pow(x, n).
This is a great example to illustrate how to solve a problem during a technical
interview. The first and second solution exceeds time limit; the third and fourth are
accepted.

**276.1 Recursive Method**

Naturally, we next may think how to do it in O(logn). We have a relation that xn =ˆ
xˆ(n/ 2 ) * xˆ(n/ 2 ) * xˆ(n

public static double pow(double x, int n) {
if(n == 0)
return 1;

```
if(n == 1)
return x;
```
```
int half = n/2;
int remainder = n%2;
```
if(n % 2 ==1 && x < 0 && n < 0)
return - 1/(pow(-x, half)* pow(-x, half)*pow(-x, remainder));
else if (n < 0)
return 1/(pow(x, -half) *pow(x, -half)* pow(x, -remainder));
else
return (pow(x, half)*pow(x, half) * pow(x, remainder));
}

**276.2 Accepted Solution**

The accepted solution is also recursive, but does division first. Time complexity is

O(nlog(n)). The key part of solving this problem is the while loop.

public double pow(double x, int n) {
if (n == 0)
return 1;
if (n == 1)

675 | 677


276 Pow(x, n)

```
return x;
```
```
int pn = n > 0? n : -n;// positive n
int pn2 = pn;
```
```
double px = x > 0? x : -x;// positive x
double result = px;
```
```
int k = 1;
//the key part of solving this problem
while (pn / 2 > 0) {
result = result* result;
pn = pn / 2;
k = k* 2;
}
```
```
result = result* pow(px, pn2 - k);
```
```
// handle negative result
if (x < 0 && n % 2 == 1)
result = -result;
```
```
// handle negative power
if (n < 0)
result = 1 / result;
```
return result;
}

**276.3 Best Solution**

The most understandable solution I have found so far.

public double power(double x, int n) {
if (n == 0)
return 1;

```
double v = power(x, n / 2);
```
if (n % 2 == 0) {
return v* v;
} else {
return v* v* x;
}
}

public double pow(double x, int n) {
if (n < 0) {

676 | 677 Program Creek


```
276 Pow(x, n)
```
return 1 / power(x, -n);
} else {
return power(x, n);
}
}

