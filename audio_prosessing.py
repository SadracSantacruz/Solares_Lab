from pydub import AudioSegment

# Read data from a text file
file_path = "time_recordings.txt"

with open(file_path, "r") as file:
    data_lines = file.readlines()

# Parse the data into a dictionary
parsed_data = {}
for line in data_lines:
    values = line.split(',')
    key = values[0].strip()
    data = [value.strip() for value in values[1:]]
    
    # Handle repeated keys by appending data to a list
    if key in parsed_data:
        parsed_data[key].append(data)
    else:
        parsed_data[key] = [data]

# for key, values in parsed_data.items():
    # print(f"{key}: {values}")


# Path to the folder containing audio files
audio_folder = 'audios/'

# Iterate through the dictionary and extract segments
for file_name, segment_info_list in parsed_data.items():
    # Load the audio file
    audio_path = audio_folder + file_name
    audio = AudioSegment.from_file(audio_path)

    # Iterate through each segment information in the list
    for segment_info in segment_info_list:
        label, start_time, end_time = segment_info

        # Convert start and end times to milliseconds
        start_ms = float(start_time) * 1000
        end_ms = float(end_time) * 1000

        # Extract the specified segment
        segmented_audio = audio[int(start_ms):int(end_ms)]

        # Save the segmented audio to a new file
        output_path = f'output_audios/{file_name}'
        segmented_audio.export(output_path, format='mp3')
