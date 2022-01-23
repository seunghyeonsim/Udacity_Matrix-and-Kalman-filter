import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        if self.h==1:
            return self[0][0]
        else:
            a=self.g[0][0]
            b=self.g[0][1]
            c=self.g[1][0]
            d=self.g[1][1]
            return a*d-b*c
       

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        trace=0
        for i in range(self.h):
            for j in range(self.h):
                if i==j:
                    trace+=self.g[i][j]
        return trace
                           

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        elif len(self.g)==2:
            a=self.g[0][0]
            b=self.g[0][1]
            c=self.g[1][0]
            d=self.g[1][1]
            if a*d-b*c==0:
                raise ValueError('non-invertible')
            else:
                inverse=[[(d/(a*d-b*c)),(-b/(a*d-b*c))],[(-c/(a*d-b*c)),(a/(a*d-b*c))]]
        else:
            inverse=[[1/self.g[0][0]]]
        return Matrix(inverse)

        

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        matrix_transpose = []
        for c in range(len(self.g[0])):
            new_row = []
            for r in range(len(self.g)):
                new_row.append(self.g[r][c])
            matrix_transpose.append(new_row)
    
        return Matrix(matrix_transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same")
        reset = []
        add_matrix = []
        for i in range(self.h):
            for j in range(self.w):
                add = self.g[i][j] + other.g[i][j]
                reset.append(add)
            add_matrix.append(reset)
            reset = []
        return Matrix(add_matrix)
                
        
        

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)
        Example:
        >> my_matrix = Matrix([ [1, 2], [3, 4] ])
        >> negative  = -my_matrix
        >> print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        matrix=[]  
        row=[]
        for i in range(len(self.g)):
            for j in range(len(self.g)):
                row.append((-1)*self.g[i][j])
            matrix.append(row)
            row=[]
           
        return Matrix(matrix)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        matrix=[]  
        row=[]
        for i in range(len(self.g)):
            for j in range(len(self.g)):
                row.append(self.g[i][j]-other.g[i][j])
            matrix.append(row)
            row=[]
        return Matrix(matrix)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        row=[]
        column=[]
        row_result=[]
        mult=[]
        for i in range(self.h):
            row=self.g[i]
            for j in range(other.w):
                column=[]
                for k in range(other.h):
                    column.append(other.g[k][j])
                result=0
                for l in range(self.w):
                    result+=(row[l]*column[l])
                row_result.append(result)
            mult.append(row_result)
            row_result=[]
        return Matrix(mult)
            
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            
            matrix=[]  
            row=[]
            for i in range(len(self.g)):
                for j in range(len(self.g)):
                    row.append((other)*self.g[i][j])
                matrix.append(row)
                row=[]
            return Matrix(matrix)
            