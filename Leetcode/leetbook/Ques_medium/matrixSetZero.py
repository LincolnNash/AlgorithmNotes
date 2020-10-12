"""
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:

输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

示例 2:

输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？
我们可以用数组的第一行（列）来记录，该行（列）是否为0。存在的问题是arr[0][0]这个点记录的是行还是列呢？
"""
def setZero(matrix):
    row_0 = 1
    row_nums = len(matrix)
    column_nums = len(matrix[0])
    # 第一次遍历将0元素的所在行所在列的标为无穷小
    for i in range(row_nums):
        for j in range(column_nums):
            if matrix[i][j] == 0:
                if i == 0:
                    row_0 = float("-inf")
                    matrix[0][j] = float("-inf")
                else:
                    matrix[i][0]=float("-inf")
                    matrix[0][j]=float("-inf")
    # 第二次编历将所在行列第一个元素为0的元素标为0（除行列第一个元素外）
    for i in range(1,row_nums):
        for j in range(1,column_nums):
            print(matrix[i][j])
            if matrix[i][0] == float("-inf") or matrix[0][j]==float("-inf"):
                matrix[i][j] = 0

    # 列
    for i in range(1,row_nums):
        if matrix[i][0] == float("-inf") or matrix[0][0] == float("-inf"):
            matrix[i][0] = 0
    # 行
    for j in range(1,column_nums):
        if matrix[0][j] == float("-inf") or row_0 == float("-inf"):
            matrix[0][j] = 0

    if row_0==float("-inf") or matrix[0][0] == float("-inf"):
        matrix[0][0] = 0
    return matrix

m = [[1,2,3,4],
     [5,0,7,8],
     [0,10,11,12],
     [13,14,15,0]]
ans = setZero(m)
print(ans)
m1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

ans = setZero(m1)
print(ans)





