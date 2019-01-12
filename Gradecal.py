import  csv


def main():
    GPA = 0
    Credit = 0
    Semester = 1
    GradeDB = []
    with open('acsv.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        count = 0
        for row in reader:
            GradeDB.append(row)
            Credit += float(row['Credit'])
            GPA = updateGPA(GPA, Credit, float(row['Grade']), float(row['Credit']))

            print(GPA)
            # when had F need to Decrease Credit that Add for Calculation
            if row['GradeChar'] == 'F':
                Credit -= float(row['Credit'])

def insert(Semester,DataRow):


with open('a.csv', 'w') as output_file:
    csvwriter = csv.DictWriter(output_file, fieldnames=keys)
    csvwriter.writeheader()
    for row in GradeDB:
        csvwriter.writerow(row["Subject"], row["Weight"], row["Grade"], row["Value"], row["Semester"]


def updateGPA(GPA, Credit, Grade, newCredit):
    newGPA = ((GPA * (Credit - newCredit)) + (Grade * newCredit)) / (Credit)
    return newGPA


if __name__ == "__main__":
    main()