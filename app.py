import streamlit as st
import matplotlib.pyplot as plt
import preprocessor
import pickle
import pandas as pd
import seaborn as sns
from helper import fetch_stats, busy_person, create_wordcloud, common_words, emoji_count, monthly_timeline, daily_timeline , day_timeline , month_timeline, heat_map

st.sidebar.title('Chat Analyser')
uploaded_file = st.sidebar.file_uploader('Upload File')
if uploaded_file is not None:
    bytes_data = uploaded_file.read()
else:
    pass
data = bytes_data.decode('utf-8')
sample = preprocessor.preprocess(data)
st.dataframe(sample)
user_list = sample.user.unique().tolist()
user_list.remove('group_notifications')
user_list.sort()
user_list.insert(0, 'Overall')
selected_user = st.sidebar.selectbox('Select User', user_list)
if st.sidebar.button('Show Analysis'):

    num_messages , num_words , count , links = fetch_stats(selected_user , sample)
    col1, col2, col3, col4 = st.columns(4)
    st.title('Chat Statistics')
    with col1:
        st.header('Messages')
        st.title(num_messages)

    with col2:
        st.header('Words')
        st.title(num_words)

    with col3:
        st.header('Media')
        st.title(count)

    with col4:
        st.header('Links')
        st.title(links)


    if selected_user == 'Overall':
        st.title('Most Busy Users')
        busy , df = busy_person(sample)
        fig , ax  = plt.subplots()
        col1 , col2 = st.columns(2)
        with col1 :
            ax.bar(busy.index , busy.values)
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2 :
            st.dataframe(df)

    df_wc = create_wordcloud(selected_user , sample)
    fig , ax  = plt.subplots()
    st.title('Word Cloud')
    ax.imshow(df_wc)
    st.pyplot(fig)

    common_words = common_words(selected_user , sample)

    fig , ax = plt.subplots()
    st.title('Common Words')
    ax.barh(common_words['word'] , common_words['count'])
#plt.xticks(rotation='vertical')
    st.pyplot(fig)
    st.dataframe(common_words)

    emojis = emoji_count(selected_user , sample)
    st.title('Emoji Count')

    col1, col2 = st.columns(2)
    with col1 :
        st.dataframe(emojis)

    with col2 :
        fig , ax = plt.subplots()
        plt.xticks(rotation='vertical')
        ax.pie(emojis['count'].head(),labels = emojis['emoji'].head())
        st.pyplot(fig)
    st.title('Monthly_Timeline')
    monthly_timeline = monthly_timeline(selected_user , sample)
    fig , ax = plt.subplots()
    ax.plot(monthly_timeline['time'],monthly_timeline['message'])
    plt.xticks(rotation='vertical')
    st.pyplot(fig)

    st.title('Daily_Timeline')
    daily_timeline = daily_timeline(selected_user, sample)
    fig, ax = plt.subplots()
    ax.plot(daily_timeline['date'], daily_timeline['message'])
    plt.xticks(rotation='vertical')
    st.pyplot(fig)

    col1, col2 = st.columns(2)

    with col1:
        st.title('Weekly_Timeline')
        day_timeline = day_timeline(selected_user, sample)
        fig, ax = plt.subplots()
        ax.bar(day_timeline['day_name'], day_timeline['count'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

    with col2:
        st.title('Monthly_Timeline')
        month_timeline = month_timeline(selected_user, sample)
        fig, ax = plt.subplots()
        ax.bar(month_timeline['month'], month_timeline['count'])
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

    heatmaps = heat_map(selected_user, sample)
    st.title('User_Activity_Heatmap')
    fig,ax = plt.subplots()
    ax = sns.heatmap(heatmaps)
    st.pyplot(fig)




