print "Part 3. Conditionals. Using if statements."


print "\n1. Use isalpha() to test which characters in this string are alphabetical."
print 'aliens = "Area-51"'
aliens = "Area-51"

# 1. Add a for loop and if/else statements here to test which letters are alphabetical.
# Replace pass with your code.

for ch in aliens:
    if ch.isalpha():
        print '%s is alphabetical' %ch
    else:
        print '%s is non-alphabetical' %ch




print "\n\n2. Here is  dictionary showing the ages of some students. "
age = {"Alan": 19, "Brenda": 20, "Charlene" : 21, "David": 19, "Ed": 24}
print "Dictionary with Name and Age:", age
print "Print out which students can attend an open-bar dance. They must be 21."

# 2. Add your code for exercise 2 here. Replace ths pass statement with your code.
for name in age:
    if age[name] >=21:
        print '%s can attend the open-bar dance' %name
    else:
        print '%s cannot attend the open-bar dance' %name


print "\n\n3. Here is a dictionary showing the grades for some students."
grade = {"Alan": 91.5, "Brenda": 88, "Charlene" : 77, "David": 100, "Ed": 66, "Frank": 50}
print "Dictionary of grades:", grade
print "Print out their letter grades A, B, C, D or F."
# 3. Add your code for exercise 3 here.
# Use the for loop header provided below, and replace the pass command with if/elif/else blocks.

for name in grade:
    if grade[name] >= 90:
        print '%s has earned a A.' %name
    elif grade[name] >=80:
        print '%s has earned a B.' %name
    elif grade[name] >= 70:
        print '%s has earned a C.' %name
    elif grade[name] >= 60:
        print '%s has earned a D.' %name
    else:
        print '%s has earned a F.' %name

print "\n\n4. Print the grades again, but show the student names in alphabetical order."
names = grade.keys()
names.sort()
print names

 # 4a. Add code to sort the list of names from A - Z here.

# 4b. Add more code for exercise 4 here.
# Use the for loop header provided below, and replace the pass command with if/elif/else blocks.

for n in names:
    if grade[n] >=90:
        print '%s has earned a A.' %n
    elif grade[n] >=80:
        print '%s has earned a B.' %n
    elif grade[n] >=70:
        print '%s has earned a C.' %n
    elif grade[n] >= 60:
        print '%s has earned a D.' %n
    else:
        print '%s has earned a F.' %n



print "\n\n5. Print out the students by rank, that is from highest to lowest numerical grade."
grade = {"Alan": 91.5, "Brenda": 88, "Charlene" : 77, "David": 100, "Ed": 66, "Frank": 50}

# 5a. Create a list of the numerical values here.
numerical_grades = grade.values()  # Done for you.
numerical_grades.sort()
nums = numerical_grades[::-1]
# 5b. Sort that list of values here.

rank=0
print "%-8s%-10s%-2s" % ("Rank", "Name", "Grade")  # Headers  for the table of grades by rank.

# 5c. Complete the nested for loop using an if statement to find the student
# with each number_grade, (assumed to be unique), increase the rank by 1, and print out
# that students info to match the sample output in the PDF instruction file.

for number_grade in nums:
    rank+=1
    for name in grade:
        if grade[name] == number_grade:
            print '%d, %s, %d' %(rank,name,number_grade)
