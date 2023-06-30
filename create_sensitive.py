def create_sensitive(dem, index):
    
    Age = dem.loc[index, "Age"]
    if Age == 110:
        Age = 'unknown age'
        Age_group = 'unknown age group'
    else: 
        Age = "{} years old".format(Age)
        Age_group = dem.loc[index, 'Age_group']

    Segment = dem.loc[index, "Segment"]

    Asset = "{}€ of assets".format(dem.loc[index, "Assets"])
    Financing = "{}€ of financing".format(dem.loc[index, "Financing"])
    Giro = "{}€ of monthly Giro turnover".format(dem.loc[index, "Giro"])

    Income_Category = dem.loc[index, "Income_Category"]
    Financing_Category = dem.loc[index, "Financing_Category"]
    Giro_Category = dem.loc[index, "Giro_Category"]
    
    Family_status = dem.loc[index, 'Family_status']
    Place_category = dem.loc[index, 'Place_category']

    sensitive = [
        Age, 
        Age_group, 
        Segment, 
        Asset, 
        Income_Category, 
        Financing, 
        Financing_Category, 
        Giro, 
        Giro_Category, 
        Family_status, 
        Place_category
    ]
    
    return sensitive

# for example, let's see the characteristics of the customer in the second row
create_sensitive(dem, 2)