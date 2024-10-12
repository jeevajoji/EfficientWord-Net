import os
import glob

def delete_folders_with_few_audio(parent_folder, min_audio_files=2):
    audio_extensions = ('.wav')
    subfolders = [f for f in os.listdir(parent_folder) 
                if os.path.isdir(os.path.join(parent_folder, f))]
    deleted_folders = []
    for subfolder in subfolders:
        subfolder_path = os.path.join(parent_folder, subfolder)
        
        audio_files = []
        for ext in audio_extensions:
            audio_files.extend(glob.glob(os.path.join(subfolder_path, f'*{ext}')))
        
        # If less than minimum required audio files, delete the folder
        if len(audio_files) < min_audio_files:
            try:
                for file in os.listdir(subfolder_path):
                    file_path = os.path.join(subfolder_path, file)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                    except Exception as e:
                        print(f"Error deleting file {file_path}: {e}")
                
                # Delete the folder
                os.rmdir(subfolder_path)
                deleted_folders.append(subfolder)
            except Exception as e:
                print(f"Error deleting folder {subfolder_path}: {e}")
    
    return deleted_folders

main_folder = r"C:\Users\jeeva\Videos\Efficient_word_net\test - Copy"

deleted = delete_folders_with_few_audio(main_folder)

if deleted:
    print("Deleted the following folders:")
    for folder in deleted:
        print(f"- {folder}")
    print(f"Total folders deleted: {len(deleted)}")
else:
    print("No folders were deleted.")