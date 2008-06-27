def strIsInt(str):
    """Test given string is an integer
    """
    if str == None:
        return False
    
    try:
        num = int(str)
    except ValueError:
        return False
    return True
    