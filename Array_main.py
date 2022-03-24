def company_names_of_employes():
  for employee in kebab:
    print(employee["Firstname"],employee["Surname"])

employee1={}
employee1["Firstname"]="Alexander"
employee1["Surname"]="Ostrozovic"
employee1["Age"]="40"
employee1["Jobposiotion"]="Manazer"

employee2={}
employee2["Firstname"]="Bartolomej"
employee2["Surname"]="Feferovic"
employee2["Age"]="25"
employee2["Jobposiotion"]="Programator"

employee3={}
employee3["Firstname"]="Zoltan"
employee3["Surname"]="Puskas"
employee3["Age"]="40"
employee3["Jobposiotion"]="Dizajner"

kebab=[employee1,employee2,employee3]

company={}
company["Name"]= "Sumec s.r.o"
company["Segment"]= "Herna spolocnost"
company["Employees"]=kebab

company_names_of_employes()

  














































