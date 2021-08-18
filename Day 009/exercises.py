student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.


#TODO-2: Write your code below to add the grades to student_grades.👇

student_grades = {}

for key in student_scores:
  value = student_scores[key]
  grade = 'Fail'
  if value > 90:
    grade = 'Outstanding'
  elif value > 80:
    grade = 'Exceeds expectations'
  elif value > 70:
    grade = 'Acceptable'
  student_grades[key] = grade

# 🚨 Don't change the code below 👇
print(student_grades)



#####################


travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, cities):
  travel_log.append({
    "country": country,
    "visits": visits,
    "cities": cities
  })





#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)


###############