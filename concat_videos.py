from moviepy.editor import VideoFileClip, concatenate_videoclips

clip1 = VideoFileClip("C:\coding files\wiki-videos\images\output_1.mp4")

clip3 = VideoFileClip("C:\coding files\wiki-videos\introduction.mp4")
final_clip = concatenate_videoclips([clip3 , clip1])
final_clip.write_videofile("my_concatenation.mp4")
