# Shikov

## Introduction

**Shikov** is a fun project that uses a **Markov chain** to generate variations of the "Shikairo Day" video.  


I have cut the original video into segments based on each syllable, with an additional rest beat (marked as "_").

The program randomly traverses the Markov chain based on the transition matrix and generate the video (which is usually kinda like a otoMAD lmao).

The standard sentence is:\
**"しかのこのこのここしたんたん__"**

In my code I will force the program retry until it produces a list containing a segment of this standard lyric (although it is probably not easy to identify because it is assembled by syllables I cut instead of a natural & consistent lyric from the original video).
You can modify the code and to remove this constraint and try your own to see what it will generate :).

I have put the standard sample "standard.mov" here as a reference. 

The Markov chain plot is as following:

![Markov Chain](Markov_chain.png)

---

## Requirements

The program is interpreted by python3

The following packages are needed

1. moviepy

    `pip install miviepy`

2. ffmpeg

    `brew install ffmpeg`

---

## Run
To run the program, do the following:

   `python shikov.py`

---

## Credit

This project is inspired by the YouTube video [【マルコフ連鎖】Shikanoko but it's a Markov chain](https://www.youtube.com/watch?v=Xkq13ZthmA0).

Special thanks to Kat, the creator of the original video, for the fascinating and inspiring content and idea.