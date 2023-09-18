# openai_commands.py

def generate_intro_command(title, country, case_study_info):
    command = f"Write a brief Introduction about {title} in {country} and specifically in {case_study_info} with enough in-text citations. Make about three paragraphs for this Introduction and conclude the fourth paragraph outlining the outline of chapter one ... NOTE THAT THE CURRENT YEAR WE ARE IN IS 2023 and citations need to be between June of 2020 to June of 2023 and in APA style."
    return command

def generate_global_background_command(title):
    command = f"Write historical Background of the study about {title} looking at it on a global perspective with enough in text citations ... NOTE THAT THE CURRENT YEAR WE ARE IN IS 2023 and citations need to be between June of 2020 to June of 2023 and in APA style."
    return command

def generate_african_background_command(title):
    command = f"Write historical Background of the study about {title} looking at it on an African perspective with in text citations ... NOTE THAT THE CURRENT YEAR WE ARE IN IS 2023."
    return command

def generate_east_african_background_command(title):
    command = f"Write historical Background of the study about {title} looking at it on a East African perspective with in text citations ... NOTE THAT THE CURRENT YEAR WE ARE IN IS 2023 and citations need to be between June of 2020 to June of 2023 and in APA style."
    return command

def generate_country_specific_background_command(title, country, case_study_info):
    command = f"Write historical Background of the study about {title} looking at it on {country} perspective with in text citations. Then Write A very detailed past then current situation of {title} in {case_study_info}. Conclude saying it is upon the above background that this study aims to ... {title} in {case_study_info}, {country}. NOTE THAT THE CURRENT YEAR WE ARE IN IS 2023 and citations need to be between June of 2020 to June of 2023 and in APA style."
    return command
