
def filter_text(text:str):
    command=text.split(" ")[1].split(":",1)
    flow=command[0]
    domain=command[1].replace("<","").replace(">","").split("|")[1]
    return  flow,domain
