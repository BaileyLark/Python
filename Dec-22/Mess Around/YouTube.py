from googleapiclient.discovery import build 

api_key = 'AIzaSyBSVRfYPg0eVR-xrHhSswXMkjVIMai_SiA'
youtube = build('youtube', 'v3', developerKey=api_key)
request = youtube.channel().list(
    part='statistics', forUsername='AuroraMusic')

responce = request.execute()

print(responce)


