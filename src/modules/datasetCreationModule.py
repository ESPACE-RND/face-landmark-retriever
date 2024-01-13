import os
from moviepy.video.io.VideoFileClip import VideoFileClip


def split_video_and_extract_audio(video_path, video_output_folder, audio_output_folder):
    # Create output folders if they don't exist
    if not os.path.exists(video_output_folder):
        os.makedirs(video_output_folder)
    if not os.path.exists(audio_output_folder):
        os.makedirs(audio_output_folder)

    # Extract video file name without extension as a unique identifier
    video_filename = os.path.splitext(os.path.basename(video_path))[0]

    # Load video clip
    video_clip = VideoFileClip(video_path)

    # Get video duration in seconds
    video_duration = int(video_clip.duration)

    # Define the length of each segment (10 seconds)
    segment_length = 10

    # Iterate through each 10-second segment
    for start_time in range(0, video_duration, segment_length):
        end_time = min(start_time + segment_length, video_duration)

        # Extract video segment
        video_segment = video_clip.subclip(start_time, end_time)

        # Extract audio from video segment
        audio_segment = video_segment.audio

        # Construct unique identifiers for video and audio segments
        video_identifier = f"{video_filename}_video_{start_time}-{end_time}.mp4"
        audio_identifier = f"{video_filename}_audio_{start_time}-{end_time}.wav"

        # Save video segment
        video_output_path = os.path.join(video_output_folder, video_identifier)
        video_segment.write_videofile(video_output_path, codec="libx264")

        # Save audio segment
        audio_output_path = os.path.join(audio_output_folder, audio_identifier)
        audio_segment.write_audiofile(audio_output_path, codec="mp3")
