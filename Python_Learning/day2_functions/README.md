# Day 2 — Functions & Scope: Numbers Summary Calculator

## Description
This Python script allows the user to enter a list of numbers and calculates:
- Sum
- Average
- Maximum
- Minimum

The script demonstrates:
- Defining functions
- Using local variables
- Returning values
- Handling exceptions (invalid input or empty list)

## How to Use
1. Run `day2_functions.py`.
2. Enter numbers separated by commas (e.g., `10, 20, 5, 8`).
3. The script will print a summary showing:
   - Numbers entered
   - Sum
   - Average (rounded to 2 decimals)
   - Maximum
   - Minimum

## Key Functions
- `calculate_sum(numbers)` → returns the total sum
- `calculate_average(numbers)` → returns the average
- `find_max(numbers)` → returns the maximum number
- `find_min(numbers)` → returns the minimum number

## Example Output
Numbers: 10, 20, 5, 8
Sum: 43
Average: 10.75
Max: 20
Min: 5


## Notes
- Input must be integers separated by commas.
- The script includes error handling for invalid inputs and empty lists.