print("=== Numbers Summary Calculator ===")
print("Hello! This program will calculate the Sum, Average, Maximum, and Minimum of the numbers you provide.")
def calculate_sum(numbers):
    result=(sum(numbers))
    return result 
def calculate_average(numbers):
    result= calculate_sum(numbers)/len(numbers)
    return result     
def find_max(numbers):
    result=(max(numbers))
    return result 
def find_min(numbers):
    result=(min(numbers))
    return result 
try:    
    str_numbers=input("Enter numbers separated by commas \n Example: 10, 20, 5, 8 \n")    
    numbers=[int(number.strip()) for number in str_numbers.split(",")]
    print("\n--- Summary ---")
    print("Numbers: ",str_numbers)
    print("Sum:" ,calculate_sum(numbers))
    print("Average:", round(calculate_average(numbers), 2))
    print("Max: ",find_max(numbers))
    print("Min: ", find_min(numbers))
except(ValueError):
    print("Please Enter  Valid Numbers  separated by commas !")
except(ZeroDivisionError):
    print("Please Enter  Valid Numbers  separated by commas ! ")
except:
    print("An Unknown occured! ")
