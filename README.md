# Scraped-GoogleSheets
This repository hands out a short but easy to grasp example for scraping data from google sheets.

(<i><ins>Note:</ins>  Edit the code according to the structure of your excel or google sheets file.</i>)

Link to the file - `https://docs.google.com/spreadsheets/d/1zOnmh-CZXa5h978y9MnH06YjAU1m6F5q0IMfRyn7D6U/`

### Requirements:
- Python Libraries - `json`, `gspread` and `oauth2client`
- Google Service Account

### Install Python Libraries
```
pip install gspread oauth2client
```

### Google Service Account

1. Go to the Google Cloud Console:
   - Open the Google Cloud Console in your web browser: `https://console.cloud.google.com/`

2. Select or Create a Project:
   - If you already have a project for your application, select it from the dropdown menu in the top navigation bar.
   - If you don't have a project, click on "Create project" and follow the instructions to create a new one.
     
3. Enable the Google Sheets API:
   - In the navigation menu, go to APIs & Services > Library.
   - Search for "Google Sheets API" and click on it.
   - Click on "Enable" to enable the API for your project.
     
4. Create a Service Account:
   - Go to IAM & Admin > Service Accounts.
   - Click on "Create service account".
   - Give your service account a descriptive name (e.g., "Sheets API Access") and an optional description.
     ![image](https://github.com/akarsh0913/Scraped-GoogleSheets/assets/134067749/abc3b7fa-2f77-43d1-aa55-9de8e956452a)
   - Click on "Create and Continue".
   - Click on "Done".
  
   

