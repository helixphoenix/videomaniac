import cv2
from data import CapturedVideo

def process_video(video_path):
   video= cv2.VideoCapture(video_path)
   video_details = CapturedVideo()
   if video.isOpened():
       video_details.width = video.get(3)
       video_details.height = video.get(4)
       video_details.frame_rate = video.get(5)
       video_details.number_of_frames = video.get(7)
       video_details.temperature =video.get(23)
   return video_details   
       
print(process_video("/Users/fitifiti/Documents/videos/lovis.mp4"))