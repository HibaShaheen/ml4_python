"""
Created on friday Feb 14  21:05:06 2020

@author: Hiba Shaheen Nawaid Dokadia
"""

import re

import matplotlib.pyplot as plt
import pandas as pd


def read_and_display_excel_file():
    """ reading the data from excel file"""
    excel_file_name = 'bankAccountData.xlsx'
    df = pd.read_excel(excel_file_name)
    print(df)
    return df  # return dataframe so that we can use it in other functions


# display only those account having same country code as input
def display_info_by_country_code(df, country_code):
    """Check the column of country code with the given input"""
    df_for_country_code = df[df["Country Code"] == country_code]
    print(df_for_country_code)



def sort_and_display_bank_accounts_by_first_name(df):
    """ sort the dataframe by first_name."""
    sorted_df = df.sort_values("first_name")
    print(sorted_df)



def display_bank_account_having_max_balance(df):
    """Function should find the account which have maximum balance"""
    balance_column = df["Balance"]
    maximum_balance = max(balance_column)  # balance_column is the list of balances of respective
    # bank account. max is inbuilt function which finds the maximum in the list
    max_balance_info = df[maximum_balance == df["Balance"]]  # Checks the balance of each row
    print(max_balance_info)



def display_number_of_bank_account_for_unique_card_type(df):
    """Print different number of card types present in data and number of account having that card type"""
    sorted_df = df.sort_values("Card Type")  # dataFrame is sorted on card type field
    sorted_card_type_list = sorted_df["Card Type"]  # card type column as list. list is sorted
    card_type = sorted_card_type_list.iloc[0]  # access first element of sorted list,iloc was used.
    count = 0
    for i in range(len(sorted_card_type_list)):
        if card_type != sorted_card_type_list.iloc[i]:  # check that if card type is not equal
            print(card_type, count)  # for which we were counting with the count of it.
            count = 0
            card_type = sorted_card_type_list.iloc[i]
        count += 1
    print(card_type, count)



def update_balance_for_card_type_and_add_new_column_for_It(df, card_type):
    """ increment the balance of account by 10% for input card type and then add it to new column"""
    updated_balance = []
    for i in range(len(df)):
        if df.loc[i, "Card Type"] == card_type:  # card type of ith row equal to i/p card type
            updated_balance.append(df.loc[i, "Balance"] + df.loc[i, "Balance"] / 10)
        else:
            updated_balance.append(df.loc[i, "Balance"])
    df["updated_balance"] = updated_balance  # the updated balance list
    print(df)



def display_the_histogram_for_balance(df):
    """ Display the histogram view of balance for knowing the distribution of balance"""
    df["Balance"].plot(kind="hist")  # Used matplotlib.pyplot library for plotting
    plt.show()


def display_account_info_having_following_pattern_for_credit_card(df, pattern):
    """input pattern is search in credit card column and display the bank account info"""
    match_row = []
    for i in range(len(df)):
        match = re.search(pattern, str(df.loc[i, "Credit Card"]))  # re.search search the pattern
        if match:  # match is NONE if pattern is not found in string
            match_row.append(i)  # the row number of the matched row is appended in list
    print(df.loc[match_row, :])  # prints the row of dataframe using the row number

