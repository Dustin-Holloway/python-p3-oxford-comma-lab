def oxford_comma(items):
    if len(items) == 1:
        string = " ".join(items)
        return string
    elif len(items) == 2:
        string = " and ".join(items)
        return string
    elif len(items) >= 3:
        updated_list = items[:-1] + [f"and {items[-1]}"]
        update = ", ".join(updated_list)
        return update



        

    

