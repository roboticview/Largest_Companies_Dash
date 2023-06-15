import pandas as pd 

PATH = r"/Users/n/largestcompanies/LargestCompanies.csv"

def get_data(PATH):
    df = pd.read_csv(PATH) 
    print(df)
    return df 

def get_contries_marketcap(PATH):
    df = get_data(PATH)
    companies = df.groupby(['country'])['marketcap'].sum()
    companies.sort_values(ascending=False, inplace=True)
    companies = companies.iloc[:10].to_frame()
    companies['trillions'] = round(companies['marketcap']/1000000000000,2)
    companies.reset_index(inplace=True)
    return companies   
    
# print(get_contries_marketcap())