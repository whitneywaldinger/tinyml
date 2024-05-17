import os
import json
import shutil

def preprocess_emoset(data_root, output_dir, phase='train'):
    # Create output directories
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the phase-specific JSON file
    with open(os.path.join(data_root, f'{phase}.json'), 'r') as f:
        data = json.load(f)

    # Create directories for each emotion class in the output directory
    emotions = ['amusement', 'anger', 'awe', 'contentment', 'excitement', 'disgust', 'fear', 'sadness']
    for emotion in emotions:
        emotion_dir = os.path.join(output_dir, emotion)
        if not os.path.exists(emotion_dir):
            os.makedirs(emotion_dir)

    # Process each entry in the JSON file
    for entry in data:
        emotion, image_id, image_path, annotation_path = entry
        full_image_path = os.path.join(data_root, image_path)

        if os.path.exists(full_image_path):
            # Copy image to the corresponding emotion directory
            dest_path = os.path.join(output_dir, emotion, f'{image_id}.jpg')
            shutil.copyfile(full_image_path, dest_path)
        else:
            print(f"Image not found: {full_image_path}")

# Define paths
data_root = 'path/to/data_root'
output_dir_train = 'path/to/output/train'
output_dir_val = 'path/to/output/val'
output_dir_test = 'path/to/output/test'

# Preprocess datasets
preprocess_emoset(data_root, output_dir_train, phase='train')
preprocess_emoset(data_root, output_dir_val, phase='val')
preprocess_emoset(data_root, output_dir_test, phase='test')
