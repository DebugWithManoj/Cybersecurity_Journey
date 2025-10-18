
# Number Summary Tool

This is a simple Python script that takes a list of numbers from the user and gives a quick summary, including the total, maximum, minimum, and average. It’s perfect for quickly checking your numbers without doing the math manually.

## Features

- Calculate the **total** of all numbers.
- Find the **maximum** number.
- Find the **minimum** number.
- Calculate the **average** of the numbers.
- Works directly from the command line.

## How to Use

1. Open your terminal or command prompt.
2. Run the script with a list of numbers separated by spaces. For example:

```bash
python your_script.py "10 20 30 40"
````

3. The script will print out:

```
Total: 100
Maximum: 40
Minimum: 10
Average: 25.0
```

## Notes

* Make sure to enter **only numbers** separated by spaces.
* If no numbers are provided, the script will let you know.
* The script uses Python’s built-in `argparse` module to handle input.

## Example

```bash
python your_script.py "5 8 12 20"
```

Output:

```
Total: 45
Maximum: 20
Minimum: 5
Average: 11.25
```

## Requirements

* Python 3.x
* No additional packages are required.

## Author

Made with ❤️ by Manoj

