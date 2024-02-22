import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('cred.json', scope)

client = gspread.authorize(credentials)

sheet_url = 'https://docs.google.com/spreadsheets/d/1zOnmh-CZXa5h978y9MnH06YjAU1m6F5q0IMfRyn7D6U/'

sheet = client.open_by_url(sheet_url)

worksheet = sheet.get_worksheet(0)

data = worksheet.get_all_values()

# print(data)

organized_data = {}
headers = data[0]
current_day = None
current_semester = None

for row in data[1:]:
    day = row[0]
    semester = row[1]
    section = row[2]
    timings = row[3:]

    # If the day is not blank, update current_day
    if day:
        current_day = day

    # If the semester is not blank, update current_semester
    if semester:
        current_semester = semester

    # If the current_day is not in the dictionary, add it
    if current_day not in organized_data:
        organized_data[current_day] = {}

    # If the current_semester is not in the current_day's dictionary, add it
    if current_semester not in organized_data[current_day]:
        organized_data[current_day][current_semester] = {}

    # If the section is not in the current_day's semester's dictionary, add it
    if section not in organized_data[current_day][current_semester]:
        organized_data[current_day][current_semester][section] = {}

    # Add timings to the section
    for i in range(len(timings)):
        if timings[i]:  # Check if timing is not empty
            organized_data[current_day][current_semester][section][headers[i + 3]] = timings[i]

# print(organized_data)

json_data = json.dumps(organized_data, indent=2)

with open("org_sheets.json", 'w') as json_file:
    json_file.write(json_data)
