def apply(m, r1, r2, k):
    """
    Use row r1 to nullify element k on row r2.
    This is a transformation that doesn't change the solution of the system.
    """

    row1 = m[r1]
    row2 = m[r2]

    sign = -1 if row1[k]*row2[k] >= 0 else 1
    alpha = sign * row2[k]/row1[k]

    to_b_added_row = [alpha*e for e in row1]

    new_row2 = [e1 + e2 for e1, e2 in zip(row2, to_b_added_row)]

    m2 = m[:] # copy matrix
    m2[r2] = new_row2
    return m2


def pretty_print(m):
    for row in m:
        for col in row:
            print(col, '\t', end='')
        print()

    print()


def pivot(m, k):
    """
    To avoid having a r1[k] == 0 and doing: alpha = r2[k]/0.
    """

    # list of tuples, each tuple has row-index and row
    rows = list(enumerate(m))

    # get index i of row with max k-th element
    # TODO: limit the number of rows to the ones that still have to be eliminated plus the one above them, depends on k
    i = max(rows,  key=lambda r:  (-1 if r[0] > k else 1) * abs(r[1][k]))[0]

    m2 = m[:]  # copy matrix

    # swap rows such that row i goes at the top
    m2[0], m2[i] = m2[i], m2[0]
    return m2


def test_pivot():

    m = [[3, 6, 3, 0],
         [1, 4, 3, 6],
         [2, 6, 7, 0]]

    return (
        pivot(m, 3) == [[1, 4, 3, 6], [3, 6, 3, 0], [2, 6, 7, 0]] and
        pivot(m, 2) == [[2, 6, 7, 0], [1, 4, 3, 6], [3, 6, 3, 0]] and
        pivot(m, 1) == [[3, 6, 3, 0], [1, 4, 3, 6], [2, 6, 7, 0]])


def gem(m):

    n = len(m)

    for k in range(n):  # for each possible column k

        m = pivot(m, k)  # pivoting step
        r1 = k  # row one, used for simplifying

        for r2 in range(r1+1, n):  # for each possible row two, below row one

            print("for rows:", r1, r2, "on col:", k, "\n")
            m = apply(m, r1, r2, k)
            pretty_print(m)

    return m


if __name__ == '__main__':

    # m = [
    #     [3, 6, 3, 0],
    #     [1, 4, 3, 6],
    #     [2, 6, 7, 0],
    # ]

    m = [
        [2, 7, 5],
        [14, 50, 36],
        [2, 8, 8],
    ]

    assert test_pivot()
    print("initial:")
    pretty_print(m)
    m = gem(m)
    print("final:")
    pretty_print(m)
