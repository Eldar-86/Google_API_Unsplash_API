import sys
from Spreadsheet import test_number_of_runs, test_order_values, test_update_order_status
from Unsplash_image_get import test_get_images
from Drive import test_uploading_photos


############################################################################################################################################
#Main function

def main():                                                             #Main function to run the script and handle errors
    complete_number_of_orders = test_number_of_runs()
    if complete_number_of_orders < 0:
        raise sys.exit(f"Could not run the script.\nCheck if 'Order #' are properly filled in.")
    number_of_runs = 0
    while complete_number_of_orders > number_of_runs:
        try:
            order_details_list = test_order_values()
            print(f"Running order {order_details_list[0]}. Please wait.")
            test_uploading_photos()
            test_update_order_status()
            number_of_runs += 1
        except:
            break
    print(f"Completed {number_of_runs} order(s) in this run. No more pending orders at the moment.")

############################################################################################################################################
#Entry point check

if __name__ == '__main__':
    main()

############################################################################################################################################
