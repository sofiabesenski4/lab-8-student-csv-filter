"""
Lab8.py
this program will take a csv formatted file as input, and stdout an altered csv file

Each line in the file needs to contain: 
				"first_name,last_name,age,course1,…courseN" of university students
The goal is to return a csv table of students who are over the age of 25 in the form:
				"LASTNAME,firstname,int(number of courses)"
The implementation required, is to create a dictionary for every student in the file, then add to a list of student dictionaries.
After that, use lambda, map and filter functions to retrieve only students over age 25, and format the output according to the specifications noted


"""
def main():
	filename= input("enter the filename")
	students = []
	with open(filename, "r") as fp:
		for line in fp.readlines():
			students.append({"first": line.split(",")[0], "last":line.split(',')[1], "age":line.split(",")[2], "courses": [course for course in line.split(',')[3:]]})
		return(list(map(lambda student:  str(student["last"].upper() + "," + student["first"] + "," + str(len(student["courses"])))  ,   list(filter(lambda student: int(student["age"])>25,students))      )))

	
	
	
if __name__=="__main__":
	for entry in main():
		print(entry)
	
