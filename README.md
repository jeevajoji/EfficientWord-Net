# EfficientWord-Net: Hotword Detection Using One-Shot Learning
EfficientWord-Net is an open-source hotword detection engine built on a lightweight architecture that leverages one-shot learning for real-time performance. This engine achieves high accuracy with minimal training samples, eliminating the need for large datasets or retraining for each new hotword. It is optimized for edge devices and is based on EfficientNet-B0 and Siamese neural network architecture, utilizing Log Mel spectrograms for feature extraction.

## Features
- One-shot learning: Detect hotwords with only one or a few training samples.
- EfficientNet Backbone: Leverages EfficientNetB0 for reduced computation and faster inference.
- Siamese Network: Compares audio samples and learns similarity between hotwords.
Edge Device Ready: Works efficiently on devices like Raspberry Pi with real-time performance.
- Noise Robust: Trained with noisy data to ensure reliable detection in real-world environments.
- Open-source: Free for modification and use, with no need for commercial licensing.

## Model Architecture

The network utilizes a Siamese architecture, where pairs of audio segments are processed using shared EfficientNet layers. The audio is first converted to a Log Mel spectrogram, allowing the model to focus on frequency distribution. Euclidean distance between the embeddings determines whether the hotwords match.


Figure 1: Overview of the Siamese architecture used for hotword detection

## Dataset
The dataset consists of artificially synthesized audio, combined with various noise environments. The hotwords were chosen to have distinct phoneme sequences, ensuring uniqueness in pronunciation.

## Performance
Accuracy: 94.51% with noise and 96.8% without noise.
Inference Time: ~0.08 seconds on a Raspberry Pi 4.
False Acceptance Rate (FAR): Low FAR across various tested hotwords.
## Installation
Clone the repository:
```
git clone https://github.com/your-username/efficientword-net.git
```
Install the required dependencies:
```
pip install -r requirements.txt
```
## Usage
Train the model:
```
python train.py --data_path path_to_dataset
```
Perform real-time inference:
```
python infer.py --audio_input path_to_audio
```
## Results
The network was trained for 42 epochs with noise augmentation, achieving a validation accuracy of 94.51%. The system is able to detect hotwords in real-time on low-resource devices with minimal latency.

## License
This project is licensed under the MIT License - see the LICENSE file for details.