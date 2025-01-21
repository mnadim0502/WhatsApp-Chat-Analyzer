import re
import pandas as pd

def preprocess(data):
    pattern = r'(\d{2}/\d{2}/\d{2}), (\d{1,2}:\d{2})\s?[ap]m - (.*?): (.*)'

    # Initialize lists to store usernames, messages, and dates
    usernames = []
    messages = []
    dates = []

    # Extract data from each line of the text
    for line in data.split('\n'):
        match = re.search(pattern, line)
        if match:
            date = match.group(1) + ", " + match.group(2)
            username = match.group(3)
            message = match.group(4)
            
            dates.append(date)
            usernames.append(username)
            messages.append(message)

    df = pd.DataFrame({'date': dates})
    df['date'] = pd.to_datetime(df['date'])
    # df['date'] = pd.to_datetime(df['date'], errors='coerce', format='%Y-%m-%d %H:%M:%S')

    df['user'] = usernames
    df['message'] = messages
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute


    # period = []
    # for hour in df[['day_name', 'hour']]['hour']:
    #     if hour == 23:
    #         period.append(str(hour) + "-" + str('00'))
    #     elif hour == 0:
    #         period.append(str('00') + "-" + str(hour + 1))
    #     else:
    #         period.append(str(hour) + "-" + str(hour + 1))

    # df['period'] = period

    return df


