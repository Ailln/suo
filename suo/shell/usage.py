from time import ctime

from suo.version import VERSION


def run():
    cur_time = ctime()
    text = f"""
    # suo 
    
    Version {VERSION} ({cur_time} +0800)
    """
    print(text)
