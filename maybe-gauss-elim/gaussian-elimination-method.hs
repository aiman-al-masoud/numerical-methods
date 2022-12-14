import Data.List

type Row = [Double]
type Matrix = [Row]

apply :: Matrix -> Int -> Int -> Int ->  Matrix
apply m r1 r2 k = 
    replaceRow m r2 row2New
    where row1 =  m !! r1
          row2 =  m !! r2
          alpha  = (row2 !! k) / (row1 !! k)
          row2New = [ e2 - alpha*e1 | (e1, e2) <- zip row1 row2 ]
          replaceRow m index newRow = (take index m) ++ [newRow] ++ (drop (index+1) m)

gem :: Matrix -> Int -> Int -> Matrix
gem m k r2 
    | k == last-1 && r2 == last = m2
    | r2 == last                = gem m2 (k+1) (k+2) 
    | r2 /= last                = gem m2  k    (r2+1)         

    where m2 = apply m k r2 k
          last = length m - 1


pivot :: Matrix -> Int -> Matrix
pivot m k =
    noChangeRows ++ resortedRows
    -- resortedRows
    where noChangeRows = take k m
          toBeChangedRows = drop k m
          resortedRows = sortByKth toBeChangedRows k
          sortByKth m k = sortBy (\row1 row2 -> compare  (row2!!k) (row1!!k) ) m -- descending order sort 

-- m = [[1.0,2.0,3.0],
--     [1.0,2.0,3.0]]

m = [[3.0, 6.0, 3.0, 0.0],
    [1.0, 4.0, 3.0, 6.0],
    [2.0, 6.0, 7.0, 0.0]]

m' = gem m 0 1
