student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


student_grades = {}

for name in student_scores:
    score = student_scores[name]
    if score > 90:
        student_grades[name] = "Outstanding"
    if score > 80:
        student_grades[name] = "Exceeds Expectations"
    if score > 70:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = 'Fail'
    

print(student_grades)


# Adding a new nested dictionary to a nested dictionary

travel_log = [
    {
    'country': 'france', 
    'visits': 12,
    'cities': ['paris', 'madrid', 'dijon']
    },
    
    {
    'country': 'germany', 
    'visits': 2,
    'cities': ['pari', 'madri', 'din']
    },
]
 
def add_county(country_visited, time_visited, cities_visited):
  new_country= {}
  new_country['country'] = country_visited
  new_country['visits'] = time_visited
  new_country['cities_visited'] = cities_visited
  travel_log.append(new_country)
 
 
  
  
 
add_county('naija', 3, ['delta', 'lag', 'benin'])
print(travel_log)