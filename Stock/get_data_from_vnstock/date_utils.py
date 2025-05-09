from datetime import datetime, timedelta
    
def get_start_date(end_date = datetime.now(), period = '1d'):
    if period == 'max':
        return '2012-03-20'
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    days = 1
    tokens = ['d', 'mo', 'y']
    for token in tokens:
        if period.endswith(token):
            temp = int(period.removesuffix(token))
            if token == 'd':
                days = temp
            elif token == 'mo':
                days = temp * 30
            else:
                days = temp * 365
    start_date = end_date - timedelta(days=days)
    return start_date.strftime("%Y-%m-%d")
