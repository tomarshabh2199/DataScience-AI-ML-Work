from googleapiclient.discovery import build
import pandas as pd
import seaborn as sns

api_key='AIzaSyB87-GQGQINqf1piM9MlvgEaQ337g-Io7Q'

channel_ids=['@techTFQ',
             'UCu9rp_Erbctwg12qPcX9-fg',
             'loveBabbar']

youtube=build('youtube','v3',developerKey=api_key)
##function to get channel statistics

def get_channel_stats(youtube, channel_ids):
    all_data=[]
    request=youtube.channels().list(
              part='snippet, contentDetails,statistics',
              id=''.join(channel_ids))
    response=request.execute()
    for i in range(len(response['items'])):
        data= dict(response['items'][0]['snippet']['title'],
                   Subscribers=response['items'][0]['statistics']['subscriberCount'],
                   Views=response['items'][0]['statistics']['viewCount'],
                   Total_videos=response['items'][0]['statistics']['videoCount'],
                   playlist_id=response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)

    return all_data

channel_statistics=get_channel_stats(youtube,channel_ids)

channel_data = pd.DataFrame(channel_statistics)

print(channel_data)

print(channel_data.dtypes)


channel_data['Subscribers']=pd.to_numeric[channel_data['Subscribers']]
channel_data['Views']=pd.to_numeric[channel_data['Views']]
channel_data['Total_videos']=pd.to_numeric[channel_data['Total_videos']]
print(channel_data.dtypes())

sns.set(rc={'figure.figsize':(10,8)})
ax=sns.barplot(x='Channel_name', y='Subscribers', data=channel_data)
ax=sns.barplot(x='Channel_name', y='Views', data=channel_data)
ax=sns.barplot(x='Channel_name', y='Total_videos', data=channel_data)

playlist_id=channel_data.loc[channel_data['Channel_name']=='Ken Jee','playlist_id'].iloc[0]
print(playlist_id)
##Function to get videos ids

def get_video_ids(youtube, playlist_id):
    request=youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50)
    
    response=request.execute()

    video_ids=[]
    for i in range(len(response['items'])):
        video_ids.append(response['items']['contentDetails']['videoId'])

    next_page_token=response.get('nextPageToken')
    more_pages=True

    while more_pages:
        if next_page_token is None:
            more_pages=False
        else:
            request=youtube.playlistItems().list(
                    part='contentDetails',
                    playlistId=playlist_id,
                    maxResults=50,pageToken=next_page_token)

     for i in range(len(response['items'])):
        video_ids.append(response['items']['contentDetails']['videoId'])

     next_page_token=response.get('nextPageToken')
     
    return len(video_ids)

    return response
    

video_ids = get_video_ids(youtube,playlist_id)
print(video_ids)


## Function to get video details

def get_video_details(youtube, video_ids):
    all_video_stats=[]
    for i in range(0, len(video_ids),50):
        request=youtube.videos().list(
            part='snippet, statistics',
            id=','.join(video_ids[i:i+50]))

    response=request.execute()

    for video in response['items']:
        video_stats=dict(Title=video['snippet']['title'],
                         Published_date=video['snippet']['publishedAt'],
                         Views=video['statistics']['viewCount'],
                         Likes=video['statistics']['likeCount'],
                         Dislikes=video['statistics']['dislikeCount'],
                         Comments=video['statistics']['commentCount'])
        
        all_video_stats.append(video_stats)
        
    return all_video_stats

video_details=get_video_details(youtube, video_ids)
print(video_details)


video_data=pd.DataFrame(video_details)    

top10_videos=video_data.sort_values(by='Views', ascending=False).head(10)
print(top10_videos)

ax1=sns.barplot(x='Views', y='Title', data=top10_videos)

videos_per_month=video_data.groupby('Month', as_index=False).size()
print(videos_per_month)

ax2=sns.barplot(x='Month', y='size',data=videos_per_month)

video_data.to_csv('Video_Details(ken jee).csv')














    
