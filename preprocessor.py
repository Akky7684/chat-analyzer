import regex as re
import pandas as pd
def preprocess(sample):
    pattern = '\n\d{2}/\d{2}/\d{4},\s\d{2}:\d{2}\s-\s'
    sample1 = re.split(pattern, sample)
    pattern4 = '\d{2}/\d{2}/\d{4},\s\d{2}:\d{2}\s-\s'
    message_date = re.findall(pattern4, sample)
    df = pd.DataFrame({'messages': sample1, 'date and time': message_date})
    df['date and time'] = pd.to_datetime(df['date and time'], format='%d/%m/%Y, %H:%M - ')
    df.drop(index=0, inplace=True)
    user = []
    message = []
    for i in df['messages']:
        entry = re.split(':\s', i)
        if (entry[1:]):
            user.append(entry[0])
            message.append(entry[1])
        else:
            user.append('group_notifications')
            message.append(entry[0])
    df['user'] = user
    df['message'] = message
    df.drop(columns=['messages'], inplace=True)
    df['year'] = df['date and time'].dt.year
    df['month'] = df['date and time'].dt.month_name()
    df['month_num'] = df['date and time'].dt.month
    df['date'] = df['date and time'].dt.date
    df['day_name'] = df['date and time'].dt.day_name()
    df['day'] = df['date and time'].dt.day
    df['hour'] = df['date and time'].dt.hour
    df['minute'] = df['date and time'].dt.minute

    period = []

    for hour in df[['day_name', 'hour']]['hour']:
        if hour == 23:
            period.append(str(hour) + "-" + str('00'))
        elif hour == 0:
            period.append(str('00') + "-" + str(hour + 1))
        else:
            period.append(str(hour) + "-" + str(hour + 1))
    df['period'] = period


    return df

