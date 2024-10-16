import os
import pandas as pd
import shutil

csv_path = r"C:\Users\jeeva\Videos\Efficient_word_net\test.csv"
dataset_folder = r"C:\Users\jeeva\Videos\Efficient_word_net\test - Copy"
destination_folder = r"C:\Users\jeeva\Videos\Efficient_word_net\GG"

data = pd.read_csv(csv_path)

data['WORD'] = data['WORD'].astype(str)
data = data[data['WORD'] != 'nan']  # Remove NaN values

if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

for _, row in data.iterrows():
    audio_file_path = row['LINK']
    word = row['WORD']

    # Replace '/' with '_' and change extension from .opus to .wav
    audio_file_name = audio_file_path.replace('/', '_').replace('.opus', '.wav')

    full_audio_file_path = os.path.join(dataset_folder, audio_file_name)

    word_dir = os.path.join(destination_folder, word)
    if not os.path.exists(word_dir):
        os.makedirs(word_dir)

    if os.path.exists(full_audio_file_path):
        shutil.move(full_audio_file_path, os.path.join(word_dir, os.path.basename(full_audio_file_path)))
        print(f"Moved: {full_audio_file_path}")
    else:
        print(f"Audio file not found: {full_audio_file_path}")
