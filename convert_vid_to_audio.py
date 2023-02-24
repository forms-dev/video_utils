import pickle
import subprocess
import os
import sys
import cv2
import time

def convert_video_to_audio_ffmpeg(video_file, output_ext, filename):
    """Converts video to audio directly using `ffmpeg` command
    with the help of subprocess module"""
    print("Extracting audio")
    out = os.path.join(filename,filename+output_ext)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, out],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.STDOUT)


def convert_img_video(filename):

    with open(os.path.join(filename, f'{filename}.pickle'), 'rb') as handle:
        prop = pickle.load(handle)
    fps = prop['fps']
    path = filename + "/%05d.jpg"
    audio = os.path.join(filename,filename + ".mp3")
    # cmd = f'ffmpeg -y -framerate {fps} -pattern_type glob -i {path} -i {audio}  out.mp4'
    cmd = f'ffmpeg -y -i {path} -i {audio} -framerate {fps} -async 10000 -c:v libx264 -pix_fmt yuv420p test_out1.mp4'

    os.system(cmd)

def get_fps(video_file, filename):
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(video_file)
    #find and save fps
    fps = cap.get(cv2.CAP_PROP_FPS)
    prop = dict()
    prop['fps'] = fps
    out = os.path.join(filename, filename + ".pickle")
    with open(out, 'wb') as handle:
        pickle.dump(prop, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
    print("Number of frames: ", video_length)
    count = 0
    print("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        if not ret:
            continue
        # Write the results back to output location.
        cv2.imwrite(filename + "/%#05d.jpg" % (count + 1), frame)
        count = count + 1
        # If there are no more frames left
        if (count > (video_length - 1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print("Done extracting frames.\n%d frames extracted" % count)
            print("It took %d seconds forconversion." % (time_end - time_start))
            break

if __name__ == "__main__":
    vf = sys.argv[1]
    filename, _ = os.path.splitext(vf)
    if not os.path.isdir(filename):
        os.mkdir(filename)
    convert_video_to_audio_ffmpeg(vf, '.mp3', filename)
    get_fps(vf,filename)
    convert_img_video(filename)
