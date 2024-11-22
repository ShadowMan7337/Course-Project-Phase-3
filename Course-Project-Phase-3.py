#Joshua Martin CIS261 Course Project Phase 3
from datetime import datetime

# Function to open and store data to text file

def write_employee_data_to_file(employee_data):

    with open("employee_data.txt", "a") as file:  # Open file in append mode

        file.write(employee_data + "\n")


# Function to input the from date and to date for hours worked

def get_date_range():

    while True:

        try:

            from_date = input("Enter From Date (mm/dd/yyyy): ")

            to_date = input("Enter To Date (mm/dd/yyyy): ")

# Check if dates are in the correct format

            from_date = datetime.strptime(from_date, "%m/%d/%Y")

            to_date = datetime.strptime(to_date, "%m/%d/%Y")

            break

        except ValueError:

            print("Invalid date format. Please enter date in mm/dd/yyyy format.")

    return from_date.strftime("%m/%d/%Y"), to_date.strftime("%m/%d/%Y")

 
# Function to input employee data and write to text file

def collect_employee_data():

    while True:

        employee_name = input("Enter employee's name (or type 'end' to finish): ")

        if employee_name.lower() == 'end':

            break

 
# Call the date input function to get from and to dates

        from_date, to_date = get_date_range()

 

        try:

            hours_worked = float(input(f"Enter total hours worked for {employee_name}: "))

            hourly_rate = float(input(f"Enter hourly rate for {employee_name}: "))

            tax_rate = float(input(f"Enter income tax rate for {employee_name} (as a percentage, e.g., 20 for 20%): ")) / 100

        except ValueError:

            print("Invalid input, please try again.")

            continue

 
# Pipe-delimited format to store employee data in the text file

        employee_data = f"{from_date}|{to_date}|{employee_name}|{hours_worked}|{hourly_rate}|{tax_rate}"

        write_employee_data_to_file(employee_data)

 

# Function to validate date

def validate_date(date_str):

    try:

        datetime.strptime(date_str, "%m/%d/%Y")

        return True

    except ValueError:

        return False

 

# Function to generate the report

def generate_report():

    from_date_input = input("Enter the From Date for the report (or 'All' to display all records): ")

 
    if from_date_input.lower() != "all" and not validate_date(from_date_input):

        print("Invalid date format. Please enter date in mm/dd/yyyy format.")

        return

 
    totals = {

        'total_employees': 0,

        'total_hours': 0,

        'total_gross_pay': 0,

        'total_income_tax': 0,

        'total_net_pay': 0

    }

 
# Read data from file

    try:

        with open("employee_data.txt", "r") as file:

            print("\nEmployee Payroll Information:")

            for line in file:

                record = line.strip().split('|')

                rec_from_date, rec_to_date, name, hours_worked, hourly_rate, tax_rate = record

 
# Convert string data to correct types

                hours_worked = float(hours_worked)

                hourly_rate = float(hourly_rate)

                tax_rate = float(tax_rate)

 
# Calculate payroll details

                gross_pay = hours_worked * hourly_rate

                income_tax = gross_pay * tax_rate

                net_pay = gross_pay - income_tax

 
# Check if the record should be included in the report

                if from_date_input.lower() == "all" or from_date_input == rec_from_date:


# Display individual employee payroll details

                    print(f"\nFrom Date: {rec_from_date}")

                    print(f"To Date: {rec_to_date}")

                    print(f"Employee Name: {name}")

                    print(f"Total Hours Worked: {hours_worked}")

                    print(f"Hourly Rate: ${hourly_rate:.2f}")

                    print(f"Gross Pay: ${gross_pay:.2f}")

                    print(f"Income Tax Rate: {tax_rate * 100:.2f}%")

                    print(f"Income Tax: ${income_tax:.2f}")

                    print(f"Net Pay: ${net_pay:.2f}")

 
# Update totals

                    totals['total_employees'] += 1

                    totals['total_hours'] += hours_worked

                    totals['total_gross_pay'] += gross_pay

                    totals['total_income_tax'] += income_tax

                    totals['total_net_pay'] += net_pay

    except FileNotFoundError:

        print("No data available. Please enter employee data first.")

        return

 
# Display totals summary

    print("\n--- Totals Summary ---")

    print(f"Total Number of Employees: {totals['total_employees']}")

    print(f"Total Hours Worked: {totals['total_hours']:.2f}")

    print(f"Total Gross Pay: ${totals['total_gross_pay']:.2f}")

    print(f"Total Income Tax: ${totals['total_income_tax']:.2f}")

    print(f"Total Net Pay: ${totals['total_net_pay']:.2f}")

 
# Main function to run the program

def main():

    while True:

        print("\n1. Enter Employee Data")

        print("2. Generate Payroll Report")

        print("3. Exit")

        choice = input("Choose an option: ")

 
        if choice == "1":

            collect_employee_data()

        elif choice == "2":

            generate_report()

        elif choice == "3":

            print("Exiting the program.")

            break

        else:

            print("Invalid option. Please try again.")

 
# Run the payroll program

if __name__ == "__main__":

    main()