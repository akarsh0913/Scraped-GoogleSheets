# Scraped-GoogleSheets
This repository hands out a short but easy to grasp example for scraping data from google sheets.

(<i><ins>Note:</ins>  Edit the code according to the structure of your excel or google sheets file.</i>)

Link to the file - `https://docs.google.com/spreadsheets/d/1zOnmh-CZXa5h978y9MnH06YjAU1m6F5q0IMfRyn7D6U/`

### Requirements:
- Python Libraries - `json`, `gspread` and `oauth2client`
- Google Service Account
- Save `xlsx` file as `google sheets` file in drive.

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
   - Give your service account a descriptive name (e.g., "testuser") and an optional description.
     ![image](https://github.com/akarsh0913/Scraped-GoogleSheets/assets/134067749/e1d0397d-a93c-417b-8ee8-5312003e92e9)
   - Click on "Create and Continue".
   - Click on "Done".

5. Adding Keys:
   - Soon after creating your service account, you will be taken to this page.
     ![image](https://github.com/akarsh0913/Scraped-GoogleSheets/assets/134067749/fe1aadd7-8f03-4187-a2e6-1709f9ecaa48)
   - Click on the email that's displayed in the "Email" section. (<i>this would be different for you</i>)
   - Head over to the "Keys" tab and click on "Add Key".
   - This will open a drop-down list. Click on "Create New Key".
     ![image](https://github.com/akarsh0913/Scraped-GoogleSheets/assets/134067749/6316638f-cbb9-462f-8a88-db15f2c96432)
   - Select "JSON" and click on "Create".
     ![image](https://github.com/akarsh0913/Scraped-GoogleSheets/assets/134067749/2ca94761-5fe0-4f2f-9892-27454dcf85eb)
   - After clicking on "Create", a JSON file would be downloaded that contains your credentials.

### Importing Credentials in the Python Script

- Rename the downloaded JSON file to `cred.json`.
- Copy `cred.json` in the directory of the python script.
  
   

