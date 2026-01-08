from Authenticate import authenticate
import sys

############################################################################################################################################
#Spreadsheet functions:
#       Still needs handling if new order is added in a middle of spreadsheet, without any orders in between.
#       Update test_check_status() func to check if order # row True when Status row empty.

def test_check_status():                                                #Returns first empty cell from Status column by checking its content
    _, sheets_service, _ = authenticate()
    spreadsheet_id = "spreadsheet_id"
    cell_range = "Sheet1!G2:G"
    response = sheets_service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=cell_range,
        majorDimension="COLUMNS").execute()

    status_dict = {}
    for value_range in response.get("valueRanges", []):
        list_of_ranges = value_range.get("values", [""])[0]
    for index, i in enumerate(list_of_ranges):
        status_dict[index+2] = i

    if status_dict:
        for row, status in status_dict.items():
            if status == '':
                return row
            elif status == 'Complete':
                pass
        return row + 1
    else:
        return 2


def test_update_order_status():                                         #Updates the status cell after an order has been completed
    _, sheets_service, _ = authenticate()
    column_no = test_check_status()
    updated_value = {"values": [["Complete"]]}
    spreadsheet_id = "spreadsheet_id"
    status_cell = f"Sheet1!G{column_no}:G{column_no}"
    update_status = sheets_service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=status_cell,
        valueInputOption="RAW",
        body=updated_value).execute()


def test_order_values():                                                #Returns a list of 'order #', 'year', 'make', 'model' and 'trim' from spreadsheet
    _, sheets_service, _ = authenticate()
    row_no = test_check_status()
    if row_no == None:
        row_no = 2
    spreadsheet_id = "spreadsheet_id"
    ranges = f"Sheet1!A{row_no}:E{row_no}"
    response = sheets_service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=ranges,
        majorDimension="ROWS").execute()

    order_details = []
    for value_range in response.get("valueRanges", []):
        for row in value_range.get("values", [[""]])[0]:
            order_details.append(row)
        return order_details


def test_number_of_runs():                                              #Returns number of runs by subtracting the number of True Status rows from Order rows
    _, sheets_service, _ = authenticate()
    spreadsheet_id = "spreadsheet_id"
    cell_range_order = "Sheet1!A2:A"
    order_response = sheets_service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=cell_range_order,
        majorDimension="COLUMNS").execute()
    order_response.get("valueRanges", )

    cell_range_status = "Sheet1!G2:G"
    status_response = sheets_service.spreadsheets().values().batchGet(
        spreadsheetId=spreadsheet_id,
        ranges=cell_range_status,
        majorDimension="COLUMNS").execute()
    status_response.get("valueRanges", )

    order_list = []
    for value_range in order_response.get("valueRanges", []):
        range = value_range.get("values", [""])[0]
        for item in range:
            if item != '':
                order_list.append(item)

    status_list = []
    for value_range in status_response.get("valueRanges", []):
        range = value_range.get("values", [""])[0]
        for item in range:
            if item != '':
                status_list.append(item)

    return len(order_list) - len(status_list)

############################################################################################################################################
#Main function

def main():                                                             #Main function to run the script and handle errors
    complete_number_of_orders = test_number_of_runs()
    if complete_number_of_orders < 0:
        raise sys.exit(f"Could not run the script.\nCheck if 'Order #' is properly filled in.")
    number_of_runs = 0
    while complete_number_of_orders > number_of_runs:
        try:
            order_details_list = test_order_values()
            order_labels_list = ['order', 'year', 'make', 'model', 'trim']
            order_dict = {}
            for key, value in zip(order_labels_list, order_details_list):
                order_dict[key] = value
            print(order_dict)
            test_update_order_status()
            number_of_runs += 1
        except:
            break
    print(f"Completed {number_of_runs} orders in this run. No more pending orders at the moment.")

############################################################################################################################################
#Entry point check

if __name__ == '__main__':
    main()

############################################################################################################################################
