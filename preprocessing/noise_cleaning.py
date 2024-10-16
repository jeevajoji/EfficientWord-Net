import pandas as pd
import shutil
import os

csv_file = r"C:\Users\jeeva\Videos\Efficient_word_net\urbansound8k\UrbanSound8K.csv"  
data = pd.read_csv(csv_file)
data['duration'] = data['end'] - data['start']
data = data[data['duration'] >= 1]

output_base_dir = 'noise_subset'
selected_sounds = data.groupby('class').apply(lambda x: x.nlargest(50, 'salience')).reset_index(drop=True)

for index, row in selected_sounds.iterrows():
    fold = 'fold' + str(row['fold'])
    sound_file = f'{row["slice_file_name"]}'
    source_file = os.path.join(r"C:\Users\jeeva\Videos\Efficient_word_net\urbansound8k", fold, sound_file)  
    class_folder = row['class']
    class_output_dir = os.path.join(output_base_dir, class_folder)
    if not os.path.exists(class_output_dir):
        os.makedirs(class_output_dir)
    dest_file = os.path.join(class_output_dir, sound_file)
    try:
        shutil.copy(source_file, dest_file)
        print(f'Copied: {sound_file} to {class_folder}')
    except FileNotFoundError:
        print(f'File not found: {sound_file}')

print('Selection and copying complete!')
