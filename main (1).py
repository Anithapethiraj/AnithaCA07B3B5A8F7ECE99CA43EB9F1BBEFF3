def print_leap_year(year):
    """
    Print whether the given year is a leap year or not.
    """
    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

print_leap_year(2000)  
print_leap_year(2016)  
print_leap_year(2100)