import random
import csv
import pandas as pd

# Adjustable variable for the total number of names to generate
TOTAL_NAMES = 100
NAMES_FILE = "generated_names.csv"
FILE_NAME_LIST = "fake_names_list.csv"

# Lists of first and last name components
first_names = ["John", "Jane", "Alex", "Chris", "Taylor", "Jordan", "Morgan", "Casey", "Drew", "Jamie"]
last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]

# Generate fake names
fake_names = []
for _ in range(TOTAL_NAMES):
    first = random.choice(first_names)
    last = random.choice(last_names)
    full_name = f"{first} {last}"
    if len(full_name) < 20:
        fake_names.append(full_name)

# Remove duplicates and sort the fake names alphabetically
fake_names = sorted(set(fake_names))

# Print the generated names
for name in fake_names:
    print(name)
print(f"{len(fake_names)} names generated.")

# Write the names to a CSV file
with open(NAMES_FILE, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name"])  # Header row
    for name in fake_names:
        writer.writerow([name])

# List of job titles in a research organization
job_titles = [
    "Research Scientist",
    "Data Analyst",
    "Lab Technician",
    "Principal Investigator",
    "Postdoctoral Fellow",
    "Research Assistant",
    "Project Manager",
    "Technical Writer",
    "Software Engineer",
    "Bioinformatician",
    "Statistician",
    "Clinical Researcher",
    "Grant Coordinator",
    "Regulatory Specialist",
    "Quality Assurance",
    "Field Researcher",
    "Environmental Scientist",
    "Research Coordinator",
    "Innovation Manager",
    "Science Communicator",
    "Research Fellow",
    "Machine Learning Engineer",
    "AI Specialist",
    "Chemist",
    "Physicist",
    "Biologist",
    "Ecologist",
    "Geologist",
    "Materials Scientist",
    "Medical Writer",
    "Pharmacologist",
    "Research Strategist",
    "Data Scientist",
    "Epidemiologist",
    "Geneticist",
    "Nanotechnologist",
    "Oceanographer",
    "Policy Analyst",
    "Research Consultant",
    "Technical Specialist"
]

# List of locations in North America
locations = [
    "New York, USA",
    "Los Angeles, USA",
    "Chicago, USA",
    "Houston, USA",
    "Phoenix, USA",
    "Philadelphia, USA",
    "San Antonio, USA",
    "San Diego, USA",
    "Dallas, USA",
    "San Jose, USA",
    "Toronto, Canada",
    "Vancouver, Canada",
    "Montreal, Canada",
    "Calgary, Canada",
    "Edmonton, Canada",
    "Ottawa, Canada",
    "Winnipeg, Canada",
    "Quebec City, Canada",
    "Halifax, Canada",
    "Victoria, Canada",
    "Mexico City, Mexico",
    "Guadalajara, Mexico",
    "Monterrey, Mexico",
    "Tijuana, Mexico",
    "Cancun, Mexico",
    "Puebla, Mexico",
    "Merida, Mexico",
    "Chihuahua, Mexico",
    "Leon, Mexico",
    "Acapulco, Mexico"
]

# Create a DataFrame with fake names as rows and job titles + locations as columns
columns = job_titles + locations
data = []

for name in fake_names:
    row = {col: False for col in columns}
    job = random.choice(job_titles)
    location = random.choice(locations)
    row[job] = True
    row[location] = True
    row["Name"] = name
    data.append(row)

df = pd.DataFrame(data)

# Reorder columns to have "Name" as the first column
df = df[["Name"] + columns]

# Print the DataFrame
print(df)

# Optionally save the DataFrame to a CSV file
df.to_csv(FILE_NAME_LIST, index=False)