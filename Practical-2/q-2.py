# Write a program to read a date in format DD/MM/YYYY and print same in MM/DD/YYYY.
print("Enter the date in format DD/MM/YYYY")
date = input("Enter the date : ")
date = date.split("/")
print("Date in format MM/DD/YYYY : %s/%s/%s" % (date[1], date[0], date[2]))