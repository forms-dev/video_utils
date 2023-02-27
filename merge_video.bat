echo off

ECHO Input video path needed.
set /p video=Please enter input video path:

python convert_vid_to_audio.py %video% 

pause
