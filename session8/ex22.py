job_list = [
  {
    "name" : "Huy",
    "Role" : "Waiter",
    "Hours" : 12,
    "Salary per hour($)": 0.8,
  },

  {
    "name" : "Tung",
    "Role" : "Cook",
    "Hours" : 24,
    "Salary per hour($)": 1.5,
  },

  {
    "name" : "M.Duc",
    "Role" : "manager",
    "Hours" : 20,
    "Salary per hour($)": 2,
  } 
]
person4 = {
    "name" : "Don",
    "Role" : "Waiter",
    "Hours" : 12,
    "Salary per hour($)": 0.9,
}

person5 = {
    "name" : "H.Duc",
    "Role" : "Waiter",
    "Hours" : 14,
    "Salary per hour($)": 0.7,
}

job_list.append(person4)
job_list.append(person5)

job_list[0] = {
    "name" : "Huyen",
    "Role" : "Waitress",
    "Hours" : 14,
    "Salary per hour($)": 1,
}

for person in job_list:
    print(person)
