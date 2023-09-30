import json

data = {
	"name": "Satyam kumar",
	"place": "patna",
	"skills": [
		"Raspberry pi",
		"Machine Learning",
		"Web Development"
	],
	"email": "xyz@gmail.com",
	"projects": [
		"Python Data Mining",
		"Python Data Science"
	]
}

with open( "data_file.json" , "w" ) as write:
	json.dump( data , write )

# json.load()
with open("data_file.json", "r") as read_content:
	print(json.load(read_content))
 
	
# JSON string:
# Multi-line string
data = """{
	"Name": "Jennifer Smith",
	"Contact Number": 7867567898,
	"Email": "jen123@gmail.com",
	"Hobbies":["Reading", "Sketching", "Horse Riding"]
	}"""
	
# parse data:
res = json.loads( data )
	
# the result is a Python dictionary:
print( res )


