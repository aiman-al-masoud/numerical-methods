def gem(m):

    n = len(m)

    for k in range(n):  # for each possible column k

        m = pivot(m, k)  # pivoting step

        print('after pivoting')
        pretty_print(m)
        
        r1 = k  # row one, used for simplifying

        for r2 in range(r1+1, n):  # for each possible row two, below row one

            print('eliminating row:', r2, 'using row:', r1, 'on col:', k)
            m, alpha = apply(m, r1, r2, k)
            print('alpha=', alpha)
            pretty_print(m)

    return m


def pivot(m, k): # k is the column to be checked
    """
    To avoid having a r1[k] == 0 and doing: alpha = r2[k]/0.
    This returns a new matrix with (if needed) a hoisted up row.
    """

    # NB: to "nullify" the first column you use the first row,
    # etc ...
    # To "nullify" the kth column you use the kth row.
    #
    # (AFTER PIVOTING)

    # During each pivoting step:
    # You must sort* rows on the their k-th element, but only rows 
    # from the kth row to the last row. The rows before the kth stay the same.
    #
    # * actually just hoist up "max row" to the kth position 
    #

    no_change_rows = m[:k]  # k-th not included
    to_be_sorted_rows = m[k:] # k-th included
    to_be_sorted_rows.sort(key= lambda r : abs(r[k]), reverse=True)

    return no_change_rows + to_be_sorted_rows

def apply(m, r1, r2, k):
    """
    Use row r1 to set element k on row r2 to zero.
    This is a transformation that doesn't change the solution of the system.
    """

    row1 = m[r1]
    row2 = m[r2]

    alpha = row2[k]/row1[k]
    
    to_b_added_row = [alpha*e for e in row1]
    new_row2 = [e1 - e2 for e1, e2 in zip(row2, to_b_added_row)]

    m2 = m[:]  # copy matrix
    m2[r2] = new_row2

    # print('alpha is: ', '+' if sign>0 else '-'  , abs(row2[k]), '/' , abs(row1[k]))
    # print('alpha is:', 'positive' if alpha>0 else 'negative',  end='\n\n')
    return m2, alpha

def test_pivot():

    m = [[3, 6, 3, 0],
         [1, 4, 3, 6],
         [2, 6, 7, 0]]

    return (
        pivot(m, 3) == [[1, 4, 3, 6], [3, 6, 3, 0], [2, 6, 7, 0]] and
        pivot(m, 2) == [[2, 6, 7, 0], [1, 4, 3, 6], [3, 6, 3, 0]] and
        pivot(m, 1) == [[3, 6, 3, 0], [1, 4, 3, 6], [2, 6, 7, 0]])

def pretty_print(m):
    for row in m:
        for col in row:
            print(col, '\t', end='')
        print()

    print()

if __name__ == '__main__':

    m = [
        [3, 6, 3, 0],
        [1, 4, 3, 6],
        [2, 6, 7, 0],
    ]

    m = [
        [2, 7, 5],
        [14, 50, 36],
        [2, 8, 8],
    ]

    # m = [ # TODO: WROOOOOOOOONG
    #     [-1, 1, 3, 1],
    #     [2, 5, 5, 2],
    #     [0, 7, 2, 3]
    # ]

    # m = [
    #     [2,2,0],
    #     [1,1,-1],
    #     [3,-2,4]
    # ]

    # m = [[3, -2, 1, 1],
    #     [1, -3, 2, 2],
    #     [-1, 2, 4, 0]]


    # assert test_pivot()
    print("initial:")
    pretty_print(m)
    m = gem(m)
    print("final:")
    pretty_print(m)
