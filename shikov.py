import random
from moviepy import VideoFileClip
from moviepy import concatenate_videoclips

#しかのこのこのここしたんたん__
#し: shi
#か: ka
#の: no
#こ: ko
#た: ta
#ん: n
#eighth rest: _
states = ["shi", "ka", "no", "ko", "ta", "n", "_"]
transition_matrix = {
    "shi":{"ka":0.5, "ta":0.5},
    "ka":{"no":1},
    "no":{"ko":1},
    "ko":{"no":0.5, "ko":0.25, "shi":0.25},
    "ta":{"n":1},
    "n":{"ta":0.5, "_":0.5},
    "_":{"shi":0.5, "_":0.5},
}

#link the video segment to each syllable
video_files = {
    "shi": VideoFileClip("clips/shi_.mp4"),
    "ka": VideoFileClip("clips/ka_.mp4"),
    "no": VideoFileClip("clips/no_.mp4"),
    "ko": VideoFileClip("clips/ko_.mp4"),
    "ta": VideoFileClip("clips/ta_.mp4"),
    "n": VideoFileClip("clips/n_.mp4"),
    "_": VideoFileClip("clips/__.mp4"),
}

def shikov_simulation(start_state, steps):
    current_state = start_state
    sequence = [current_state]
    clips = [video_files[current_state]]
    for i in range(steps):
        next_state = random.choices(
            list(transition_matrix[current_state].keys()),
            list(transition_matrix[current_state].values()),
        )[0]
        sequence.append(next_state)
        clips.append(video_files[next_state])
        current_state = next_state
    return sequence, clips

target_sentence = ["shi", "ka", "no", "ko", "no", "ko", "no", "ko", "ko", "shi", "ta", "n", "ta", "n", "_", "_"]
start_state = "shi"

while True:
    flag = 0
    sequence, clips = shikov_simulation(start_state, 200) # you can change the length of the video by changing the value of "steps"
    for i in range(len(sequence) - len(target_sentence) + 1):
        if sequence[i:i + len(target_sentence)] == target_sentence:
            print(sequence)
            flag = 1
            break
    if flag == 1:
        clips = [VideoFileClip("clips/non.mp4")] + clips
        final_clip = concatenate_videoclips(clips, method="compose")
        final_clip.write_videofile("output/sample.mov", codec="libx264")
        break