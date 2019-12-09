# make sure that you already have ffmpeg in your PATH

import subprocess

def converter(input_video, output_video):
    options = ['ffmpeg', '-i', input_video, output_video]
    subprocess.Popen(options)

if __name__ == "__main__":
    a = input('filename:')
    b = input('output filename with file type: ')
    converter(a,b)
    print(a, 'had been converted to', b)