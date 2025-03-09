# Question 4

# Create the following using a simple 2D list using the standard Python
# indexing:

#  | 0  | 1  | 2  | 
#0 | 2  | 5  | 8  |
#1 | 3  | 7  | 4  |
#2 | 1  | 6  | 9  |
#3 | 4  | 2  | 0  |

# • Using the 2D list from program, ask the user to select a row and a column
# and display that value.

# • Using the 2D list, ask the user which row they would like displayed and
# display just that row. Ask them to enter a new value and add it to the end
# of the row and display the row again.


# Create the 2D list as per the given table
matrix = [
    [2, 5, 8],
    [3, 7, 4],
    [1, 6, 9],
    [4, 2, 0]
]

# Display the matrix
print("The matrix is:")
for row in matrix:
    print(row)

# Ask the user to select a row and column and display that value
row_index = int(input("\nEnter the row number (0-3): "))
col_index = int(input("Enter the column number (0-2): "))

if 0 <= row_index < len(matrix) and 0 <= col_index < len(matrix[0]):
    print(f"The value at row {row_index} and column {col_index} is: {matrix[row_index][col_index]}")
else:
    print("Invalid row or column number.")

# Ask the user which row they would like displayed and display that row
row_choice = int(input("\nWhich row would you like to display (0-3)? "))

if 0 <= row_choice < len(matrix):
    print(f"The selected row is: {matrix[row_choice]}")
    
    # Ask the user to enter a new value to add to the end of the row
    new_value = int(input("Enter a new value to add to the end of the row: "))
    
    # Add the new value to the row and display it again
    matrix[row_choice].append(new_value)
    print(f"The updated row is: {matrix[row_choice]}")
else:
    print("Invalid row number.")
