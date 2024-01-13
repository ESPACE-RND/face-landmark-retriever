import librosa
from librosa import feature


# Function to load and preprocess audio data
def load_and_preprocess_audio(file_path):
    audio, _ = librosa.load(file_path, sr=44100)
    mfccs = feature.mfcc(y=audio, sr=44100, n_mfcc=128)
    return mfccs.transpose()  # Transpose the matrix to have time steps as rows
