
import studentclass as sc

studentid = 1001
name = 'John'
dob = '1/1/2000'
classification = 'junior'

# once you create the John instance, you just use John from then on
john = sc.Student(studentid,name,dob,classification)

john.calc_age()

john.register()

print("Student age is:",john.get_age())
print("Student can register between:",john.get_registration())