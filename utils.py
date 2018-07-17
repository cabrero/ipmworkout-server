import datetime

def str_to_datetime(date_str):
    dt = datetime.datetime.strptime(date_str, '%Y-%m-%dT%H:%M')
    return dt
    
def datetime_to_str(dt):
    return dt.strftime('%Y-%m-%dT%H:%M')
    
