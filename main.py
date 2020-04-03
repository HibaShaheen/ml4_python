"""
Created on Fri Feb 14 21:13:03 2020

@author: Hiba Shaheen Nawaid Dokadia
"""
import bank_account_test as bat

DATA_FRAME = bat.read_and_display_excel_file()
COUNTRY_CODE = input("Please enter the Country Code: ")
bat.display_info_by_country_code(DATA_FRAME, COUNTRY_CODE)
print("\nsorted Bank Account details by first name are:  ")
bat.sort_and_display_bank_accounts_by_first_name(DATA_FRAME)
print("\nBank Account details having maximum details are:  ")
bat.display_bank_account_having_max_balance(DATA_FRAME)
print("\nUnique card type with there counts are: ")
bat.display_number_of_bank_account_for_unique_card_type(DATA_FRAME)
bat.display_the_histogram_for_balance(DATA_FRAME)
CARD_TYPE = input("\nEnter Card Type: ")
print("\nBank Account details with new column added are:  ")
bat.update_balance_for_card_type_and_add_new_column_for_It(DATA_FRAME, CARD_TYPE)
Pattern = input("\nPlease enter the pattern you want to search: ")
print("\nBank Account details with matched pattern are:  ")
bat.display_account_info_having_following_pattern_for_credit_card(DATA_FRAME, Pattern)
