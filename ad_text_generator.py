def ad_text_generator (sensitive, product, slogan = 0):
    global i
    i = 0

    # creating the customer variable by joining together the sensitive list
    customer = "; ".join(sensitive)

    # adding two best fitting bonuses to the product 
    bonuses, text_about_bonuses = bonus_gpt(customer, product)

    # joining the product with details (bonuses)
    product = product + "; " + bonuses

    # creating the ad text
    if slogan == 1:
        result = ad_gpt3_slogan(customer, product, sensitive)
    else:
        result = ad_gpt3(customer, product, sensitive)


    return result, text_about_bonuses