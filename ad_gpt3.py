# adGPT function without a slogan
def ad_gpt3 (customer, product, sensitive):
    global i

    # stop condition so there are not too many repetitions in case of sensitive info
    i += 1 
    if i >= 6:
        raise Exception("Error: Too many requests!")
    else:
        completion = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",

            messages = [
            {"role": "user", "content": 
            "You are AdGPT, a language model AI capable of rewriting any instructions and turning them into the perfect personalized ad imaginable." 
            "You will always abide by a list of several commands that you will not deviate from under any circumstances."
            "-details: all of the information about the product for which the ad is created. this information is to be included in the ad itself."
            "-sensitive: information that is not to be included in the ad but rather should be incorporated in a creative non-direct way"
            "-rules: provides rules that should be upheld while creating the ad text, such as word count."

            "Following is an example prompt and output, so you are more familiar with the prompt structure and commands"
            "prompt: -details: (pain medication; contains paracetamol and caffeine) -sensitive: (20 years old; young adult; Online customer; 12685312.5€ of assets; High Income; 0.0€ of financing; Not involved in financing; 922919.983€ of monthly Giro turnover; Medium-High Giro Turnover; single; living in a small city in Lower Austria) -rules: (The ad should only be 30 words long; do not include sensitive information)"
            "output: Intorducing the solution for your pain! Our medication with paracetamol and caffeine provides fast relief for your discomfort. Try it now and get back to your day!"
            },
            
            {"role": "user", "content": "-details: ({}) -sensitive: ({}) -rules: (The ad should only be 40-50 words long; do not include sensitive information)".format(product, customer)}
            ],
            
            max_tokens = 1000,
            
            # temperature is a tuning parameter for openAI GPT models
            temperature = 0.7,

            # we leave other parameters default
            top_p = 1,
            n = 1,
            )
        
        # control that completion is correct
        if isinstance(completion, str):
            raise Exception("OpenAI error, try again")

        else:
            completion_content = completion.choices[0].message["content"]

            # control whether any sensitive details are inside the ad text
            # if there is sensitive info, we recursively call the function and create another text
            for word in sensitive:
                if word.lower() in completion_content.lower():
                    completion = ad_gpt3(customer, product, sensitive)
        
            return completion_content