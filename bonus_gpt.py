def bonus_gpt (customer, product):

    # importing the module containing all the product bonuses and then putting the bonuses of our product into a variable
    import product_bonuses as bonuses
    try:
        bonus = getattr(bonuses, "".join(product.split()))

        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            
            messages = [
            {"role": "system", "content": 
            "You are BonusGPT, a language model AI which takes as input a list of product details and reorders them based on how suitable they are for the target customer. Always respond with just the reordered details separated by \";\" and nothing else." 
            "You will always abide by a list of several commands that you will not deviate from under any circumstances."
            "-details: list of details about the product. Go through the whole list and reorder it from most to least suitable detail."
            "-product: the product for which the ad will be created."
            "-customer: information about the target customer. Use this information to base your decision of the most suitable product details."
            "-rules: provides rules that should be upheld while reordering."
            },
            
            {"role": "user", "content": "-product: ({}) -details: ({}) -customer: ({}) -rules: (only provide two reordered details; do not provide anything except the details)".format(product, bonus, customer)}
            ],

            max_tokens = 1000,

            # temperature is a tuning parameter for openAI GPT models
            temperature = 0.7,

            # we leave other parameters default
            top_p = 1,
            n = 1,
            )
        
        bonuses_selected = completion.choices[0].message["content"]

    # if the product is not one of the products we have details about, it gets assigned general details
    except:
        bonuses_selected = "great benefits; support from Raiffeisen"

    text_about_bonuses = "Product selected: {}. Bonuses selected: {}".format(product, bonuses_selected)

    return bonuses_selected, text_about_bonuses