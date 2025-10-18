import argparse
parser = argparse.ArgumentParser(description=" Summerize ")
parser.add_argument("check",help=" Enter Your Numbers Separated by space : ")

args=parser.parse_args()
def total(numbers):
    total = sum(numbers)
    return total

def maximum(numbers):
    return max(numbers)

def minimum(numbers):
    return min(numbers)

def average(numbers):
    length =  len(numbers)
    total = sum(numbers)
    return total/length

def print_details(numbers):
    if not numbers:
        print("No numbers provided")
        return
    print("Total : ",total(numbers))
    print("Maximum : ",maximum(numbers))
    print("Minimum : " ,minimum(numbers))
    print("Average : ",average(numbers))


def input_number_from_user(check):
    numbers=[]
    numbers_list = check.split(" ")
    try:
        for num in numbers_list:
            adding = int(num)  
            numbers.append(adding)
    except(ValueError):
        print("Enter  Valid Numbers : ")

def main():
    numbers = input_number_from_user(args.check)
    print_details(numbers)

if __name__ == "__main__":
    main()
