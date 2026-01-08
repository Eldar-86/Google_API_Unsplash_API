# GoogleAPI; spreadsheet/drive

## Creating a project on Google

- Log into Google cloud console with the account where the project is to be, and creat the project.

- Select the project (keep in mind every project is in the test mode at first, until user requests approval from google, and then google approves it) and click on the hamburger in the upper left corner; hover over APIs & Services and select credentials.

- This is where OAuth 2.0 Client ID needs to be generated. Select external (internal is only for google accounts in your workspace -- limited access); also App name must be added, User support email and Developer contact email (the same email address and details where the project is created).

- Once created, since this is test project (not approved by google), you need to add audience (list of emails with allowed access). Select OAuth consent screen and select audience. In the audience section, scroll to the bottom and + Add users. With publish app button at the top of the screen, you can submit the app for google's approval and make it public once approved.

- You now need to add the scope available; go to data access. Select Add or remove scopes. After selecting scopes, they will be automatically categorized to non-sensitive, sensitive  and restricted scopes. You can select, for example, ../auth/drive for google drive access and|or ../auth/spreadsheets for spreadsheets access, etc.

- Created directory and sheet in that account's drive.

## Writing the script

- Written Authenticate.py to authenticate and create a token for specific email address with allowed access.

- Written Spreadsheet.py which contains 5 functions: **1.** to check the status of order and return row number of the first incomplete order **2.** to update the status of the order after completion **3.** to collect and return values of incomplete orders (order#, year, make, model, trim as a list) for further process. **4.** to return number of runs by comparing the number of existing orders with number of completed orders and **5.** which is the main function to run the script and handle errors

- Writing Drive.py...
