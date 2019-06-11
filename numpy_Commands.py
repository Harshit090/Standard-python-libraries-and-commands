# working on NUMPY library

import numpy as np
a = np.array([1,2,3]) # create a rank 1 array
print(type(a))

# output { <class 'numpy.ndarray'> }

print(a.shape)
print(a)

# output { (3,) (here the (row,cloumn) for two d array for 1 d array (cloumn,))
#          [1 2 3] }

print(a.ndim)

# output { 1 }

print(a[0],a[1],a[2]) #prints "1 2 3"

# output { 1 2 3 }

a[0] = 5    # changing an element of the array
print(a)

# output  { [5 2 3] }

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)

# output { (2, 3) }

print(b[0,0],b[0,1],b[1,0])

# otput { 1 2 4 }

c = np.zeros((2,2))
print(c)
'''
    output [[0. 0.]
            [0. 0.]]

'''

d = np.ones((1,2))
print(d)
#  output { [[1. 1.]] }

e = np.full((2,2),7) #create a constant array
print(e)

# output  { [[7 7]
#            [7 7]]}
'''
        a2 = input()
        a1 = np.full((2,2),a2) #create a constant array with user input
        print(a1)

        # output  here user input is 13
        #       [['13' '13']
        #        ['13' '13']]
'''
f = np.eye(2) # creates a 2x2 identity matrix
print(f)
# output {[[1. 0.]
#          [0. 1.]]}

g = np.random.random((2,2))  # create an array with random values
print(g)

# output { [[0.31397114 0.89523947]
#           [0.68368857 0.04386615]]}

print(np.arange(10)) # arange() will create an array eith regularly increasing values
# output { [0 1 2 3 4 5 6 7 8 9] }

print(np.arange(2,10, dtype=float))
# output { [2. 3. 4. 5. 6. 7. 8. 9.] }

print(np.arange(2,3,0.1))
# output { [2.  2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9] }

print(np.linspace(1.,4.,6)) # linspace() will create a set of array (stacked as a one-higher dimmensional array) one per dimension with each representing variation it that dimension
# her form 1 to 4 ^ equally distributed elements are added to array
# output { [1.  1.6 2.2 2.8 3.4 4. ] }

print(np.indices((4,5))) # indices() wil create a set of array (stacked as a one higher-dimmension array ), one per dimension with each representing variation in that dimension
# output [[[0 0 0 0 0]
#          [1 1 1 1 1]
#          [2 2 2 2 2]
#          [3 3 3 3 3]]
#
#         [[0 1 2 3 4]
#          [0 1 2 3 4]
#          [0 1 2 3 4]
#          [0 1 2 3 4]]]

h = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(h)
print(h.shape)
h1 = h[1:,2:] # assigning rows 1 onward and columns 2 onwards
print(h1)

# output {[[ 1  2  3  4]
#          [ 5  6  7  8]
#          [ 9 10 11 12]]
#         (3, 4)
#         [[ 7  8]
#          [11 12]]}

# to print a particular row
row_1 = h[1,:]
print(row_1)
# output { [5 6 7 8] }

# to print a particular columns
col_1 = h[:,0]
col_2 = h[:,0:1]
print(col_1,col_1.shape)
print(col_2,col_2.shape)
# output { [1 5 9] (3,)
#          [[1]
#           [5]
#           [9]] (3, 1) }
i = np.array([[1,2],[3,4],[5,6]])
print(i[[0,1,2],[0,1,0]]) # prints array with refernce i[x][y] position so i[0][1] is 1 similarly i[1][1] is 4
# output [1 4 5]


# the above array indexing can also be written as this
print(i[0,0],i[1,1],i[2,0])
# output  { 1 4 5 }
h2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
h3 = np.arange(4)
h4 = np.array([0,2,0,1])
print(h2[h3,h4])
# output { [ 1  7  9 14] }

h2[h3,h4] += 10
print(h2)
# output [[11  2  3  4]
#         [ 5  6 17  8]
#         [19 10 11 12]
#         [13 24 15 16]]

# boolean array indexing lets you pick out arbitary elements on an array, frequently this type of
j = np.array([[1,2],[3,4],[5,6]])
'''
    finda the elements of j that are greater than 2
    this return a numoy array of the bollean of the same
'''
bool_idx = ( j > 2 )
print(bool_idx)
print(j[bool_idx])

# output { [[ True  True]
#           [ True  True]]
#          [3 4 5 6]}
