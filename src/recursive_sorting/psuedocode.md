## Merge_Sort Function

SPLIT

- If there's an array greater than 1 (need more than one otherwise there's no point in doing this sort, and should just return the array)

- Split the left side of the array from index 0 to the midddle

- Split the right side of the array from the middle to the end of the array

- Continue to split the left and right sides recursively

MERGE

- Now use the MERGE FUNCTION to merge the array in the correct order (Passing in left and right sides to be arrays a and b).

- Code already has a way to create an array with zeros based on the length of the arrays passed in.

- Start at the index of 0 for the left and right sides.

- Loop through the length of the elements

- Goal is to look for smallest element between the two arrays, and assign it in the merged_arr

- Need to set up what to do in certain situations

- If left is already merged, then move on to right (When left index is greater than the length of the left array)

- Add in the number on the right's index into the merged_arr[i]

- Increase the counter for the right_index

- If the right is already merged, then do the same as above but to the left.

- If the number at the left's index is smaller than the number on the right's index

- Then add the left number at merged_arr[i]

- Increase left counter

- If the number in the right is smaller than the number in the left

- Then add the right number at merged_arr[i], and increase right counter.

- Return the newly sorted array
