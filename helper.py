from urlextract import URLExtract
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
from emoji import is_emoji
extractor = URLExtract()

def fetch_stats(selected_user ,sample):
    count = 0
    if selected_user == 'Overall':
        num_messages = sample.shape[0]
        words = []
        links = []
        for i in sample['message']:
            if i == '<Media omitted>':
                count = count + 1
            else:
                links.extend(extractor.find_urls(i))
                words.extend(i.split())
        num_words = len(words)
        num_links = len(links)

    else:
        num_messages =  sample[sample['user']== selected_user].shape[0]
        words = []
        links = []
        indexes = sample[sample['user']==selected_user].index
        for i in indexes:
            if sample['message'][i] == '<Media omitted>':
                count = count + 1
            else:
                links.extend(extractor.find_urls(sample['message'][i]))
                words.extend(sample['message'][i].split())
        num_words = len(words)
        num_links = len(links)

    return num_messages, num_words , count, num_links

def busy_person(df):
    x = df['user'].value_counts()
    df = round(df['user'].value_counts()/df.shape[0]*100, 2).reset_index().rename(columns={'index':'count','user':'percentage'})
    return x , df

def create_wordcloud(selected_user ,df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    df = df[df['message'] != '<Media omitted>']
    df = df[df['user']!='group notifications']
    wc = WordCloud(width=500 , height=500 , min_font_size =10,background_color='white')
    new_df = wc.generate(df['message'].str.cat(sep=" "))
    return new_df

def common_words(selected_user ,df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    temp = df[df['user'] != 'group_notifications']
    temp = temp[temp['message'] != '<Media omitted>']
    w = []
    f = open('stop_hinglish_comma_separated.txt', 'r')
    stop_words = f.read()
    stop_words = stop_words.split('\n')
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                w.append(word)
    r = pd.DataFrame(Counter(w).most_common(20) , columns=['word','count'])
    #r.rename(columns={'0': 'Word' , '1':'Frequency'}, inplace=True)
    return r

def emoji_count(selected_user ,df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if is_emoji(c)])
    new_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))), columns =('emoji','count'))
    return new_df


def monthly_timeline(selected_user ,df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    timeline = df.groupby(['month_num', 'year', 'month']).count()['message'].reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + ' - ' + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline

def daily_timeline(selected_user ,df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    daily_time = df.groupby(['date']).count()['message'].reset_index()
    return daily_time

def day_timeline(selected_user ,df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    day_time = df['day_name'].value_counts().reset_index()
    return day_time

def month_timeline(selected_user ,df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    month_time = df['month'].value_counts().reset_index()
    return month_time

def heat_map(selected_user ,df):
    if selected_user != 'Overall':
        df = df[df['user']==selected_user]
    heatmap = df.pivot_table(index = 'day_name' , columns = 'period', values = 'message' ,aggfunc='count').fillna(0)
    return heatmap

