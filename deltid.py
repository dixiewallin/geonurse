import pandas as pd

# Läs in data från CSV-filen med rätt separator och specifiera kolumnnamn
data = pd.read_csv("2023.csv", sep=";", names=[
    "Id", "Headline", "Application_deadline", "Amount", "Description", 
    "Type", "Salary", "Duration", "Working_hours", "Region", "Municipality", 
    "Employer_name", "Employer_workplace", "Publication_date"
])

# Konvertera alla värden i kolumnen "Working_hours" till små bokstäver och ta bort NaN-värden
data['Working_hours'] = data['Working_hours'].astype(str).str.lower()

# Filtrera bort "nan" och "working_hours" från listan över unika arbetstider
working_hours_types = data['Working_hours'].dropna().unique()
working_hours_types = [wh for wh in working_hours_types if wh not in ['nan', 'working_hours']]

# Presentera listan på olika typer av arbetstider för användaren
print("Här är alla olika typer av arbetstider som du kan välja mellan:")
for i, working_hours_type in enumerate(working_hours_types):
    print(f"{i}: {working_hours_type.capitalize()}")

# Användarens val av arbetstid
selected_category = int(input("Ange numret för den önskade arbetstiden: "))

# Filtrera data för den valda arbetstiden
selected_working_hours_type = working_hours_types[selected_category]
filtered_data = data[data['Working_hours'] == selected_working_hours_type]

# Visa resultaten för den valda arbetstiden
print("Resultat för arbetstiden:", selected_working_hours_type.capitalize())
print(filtered_data)

