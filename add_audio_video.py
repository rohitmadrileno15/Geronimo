import moviepy.editor as mpe
import os
from mutagen.mp3 import MP3


def add_audio_and_video(video_ip , audio_ip , video_op):
    clip = mpe.VideoFileClip(video_ip)
    audio_bg = mpe.AudioFileClip(audio_ip)
    
    audio = MP3(audio_ip)
    audio_info = audio.info        
    length_in_secs = int(audio_info.length)

    final_clip = clip.set_audio(audio_bg)
    print("set Audio")
    
    final_clip.write_videofile(video_op)

    
    clip1 = mpe.VideoFileClip(video_op)
    print("duration  ", clip1.duration)

    final_clip1 = clip1.cutout(length_in_secs , int(clip1.duration))

    final_clip1.write_videofile(video_op)

    #removing the original input file

    os.remove(video_ip)
    os.remove(audio_ip)

    return f"Video Available on {video_op}"

