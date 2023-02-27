# video_utils
Contains utilities used for processing videos. 
- Extracts fps and audio from original video.
- Combines the extracted audio with provided frames using the original fps.


Directory Hierarchy:
- main directory
-- video1.mp4
-- video1
--- video1.mp3 [will be extracted automatically]
--- video1.pkl [will be extracted automatically]
--- [frames to combine]
--- out.mp4 [result after running code]
-- video2.mp4
-- video2
--- video2.mp3 [will be extracted automatically]
--- video2.pkl [will be extracted automatically]
--- [frames to combine]
--- out.mp4 [result after running code]


Steps to follow:
1) Copy the code to a main directory.
2) Copy the source video in the main directory. 
3) Create a folder with same name as the video without extension. (if video is video1.mp4, the folder will be 'video1')
5) Copy the frames to the video folder. 
4) run merge_video.bat
5) When prompted give the complete path of video (path/to/test.mp4)
6) Your results will be saved in video folder as out.mp4  (video1/out.mp4) 
