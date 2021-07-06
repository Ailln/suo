from time import ctime

from suo import __version__

def run():
    cur_time = ctime()
    text = f"""
    # suo 
    
    Version {__version__} ({cur_time} +0800)
    """
    print(text)
