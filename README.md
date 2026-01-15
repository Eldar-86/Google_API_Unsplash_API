# GoogleAPI; spreadsheet/drive

## Creating a project on Google

- Log into Google cloud console with the account where the project is to be, and creat the project.
- Select the project (keep in mind every project is in the test mode at first, until user requests approval from google, and then google approves it) and click on the hamburger in the upper left corner; hover over APIs & Services and select credentials.

- This is where OAuth 2.0 Client ID needs to be generated. Select external (internal is only for google accounts in your workspace -- limited access); also App name must be added, User support email and Developer contact email (the same email address and details where the project is created).

- Once created, since this is test project (not approved by google), you need to add audience (list of emails with allowed access). Select OAuth consent screen and select audience. In the audience section, scroll to the bottom and + Add users. With publish app button at the top of the screen, you can submit the app for google's approval and make it public once approved.

- You now need to add the scope available; go to data access. Select Add or remove scopes. After selecting scopes, they will be automatically categorized to non-sensitive, sensitive  and restricted scopes. You can select, for example, ../auth/drive for google drive access and|or ../auth/spreadsheets for spreadsheets access, etc.

- Created directory and sheet in that account's drive.

## Writing the script

- Authenticate.py to authenticate and create a token for specific email address with allowed access.

- Spreadsheet.py is accessing and updating the order spreadsheet, and it contains 5 functions: **1.** to check the status of order and return row number of the first incomplete order **2.** to update the status of the order after completion **3.** to collect and return values of incomplete orders (order#, year, make, model, trim as a list) for further process. **4.** to return number of runs by comparing the number of existing orders with number of completed orders. 

- Drive.py is to manage folders and files on the drive. There are two functions: **1** creates folder named after the pending order number and returns the folder id **2** uploads photos from UnsplashAPI to the order# folder via BytesIO so to not take unnecessary memory or space

- Main.py is the main function to run the script and handle errors. It shows which order is in process and how many orders has been processed when there is no more orders in the spreadsheet

- Unsplash_image_get.py has one fucntion using the requests lib. It takes the order info, filters it and returns a list of URLs with regular size photos. It also returns query -- values picked up from the order.



#### Required updates

- The script still needs handling if new order is added somewhere in the middle of a spreadsheet, without any orders in between; perhaps update ***test_check_status()*** func to check if order # row True when Status row False. Also, this perhaps can be done by updating test_number_of_runs()...

- The script needs to be updated in case folder 'Photos' does not exist. It needs to check if folder exists, and then create it if not.

- The script needs handling external (API / HTTP) errors
