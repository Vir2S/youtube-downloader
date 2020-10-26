import os
import sys
import pafy

# url = "https://youtu.be/JbHI1yI1Ndk"

print('Want to download video or audio from YouTube? Just enter URL below...')
source_url = input('Enter URL here: ')

print('For download video choose: 1\nFor download audio choose: 2 ')
user_choice = input('Enter your choice here: ')


def downloader(user_choice):

    try:

        v = pafy.new(source_url)

        if user_choice == '1':
            streams = v.streams

        elif user_choice == '2':
            streams = v.audiostreams

        else:
            sys.exit()

        print('Choose the quality of video: ') \
            if user_choice == '1' else print('Choose the quality of audio ')

        available_streams = {}
        counter = 1

        for stream in streams:
            available_streams[counter] = stream
            print(f"{counter}: {stream}")
            counter += 1

        stream_counter = int(input('Enter your choice here: '))
        print('Process started. Wait while file downloading...')
        dl = streams[stream_counter - 1].download()

        if user_choice == '2':
            audio_extension = str(available_streams[stream_counter])
            audio_extension = audio_extension.split('@')[0].split(':')[1]

            file_name = v.title
            audio_file = f"{file_name}.{audio_extension}"
            base = os.path.splitext(audio_file)[0]
            os.rename(audio_file, base + '.mp3')

        print('Download complete!')

    except ValueError:

        print('Oops! Something wrong. Check the data')


downloader(user_choice)
