from keras.models import load_model
from src.modules.audioModule import load_and_preprocess_audio
from keras.preprocessing.sequence import pad_sequences


# Load the model
model = load_model("")

# Assuming you have a list of audio file paths
audio_paths = [""]

# Extract MFCCs for each audio sample
mfccs_list = [load_and_preprocess_audio(audio_path) for audio_path in audio_paths]

padded_mfccs = pad_sequences(mfccs_list, maxlen=1000,dtype='float32', padding='post')

predictions = model.predict(padded_mfccs)

# Reshape predictions
y_pred_reshaped = predictions.reshape(-1, 447, 468, 3)

# Display the predicted landmark coordinates
print("Predicted Landmark Coordinates:")
print(y_pred_reshaped[0])