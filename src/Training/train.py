import numpy as np
from src.modules.audioModule import load_and_preprocess_audio
from src.modules.excelModule import load_excel
from keras.preprocessing.sequence import pad_sequences
from src.modules.model import model

# Assuming you have a list of audio file paths
audio_paths = ["C:/Users/Admin/PycharmProjects/faceDet/src/Training/extracted_audio/JP_500x500_audio_0-10.wav"]
target_paths = ["C:/Users/Admin/PycharmProjects/faceDet/src/Training/excel_files/JP_500x500_video_0-10.mp4_pandas_to_excel.xlsx"]

# Extract MFCCs for each audio sample
mfccs_list = [load_and_preprocess_audio(audio_path) for audio_path in audio_paths]

# Pad sequences to a fixed length
padded_mfccs = pad_sequences(mfccs_list, maxlen=1000, dtype='float32', padding='post')

# target list
targets_list = [load_excel(target_path) for target_path in target_paths]

# Assuming you have target data in the format specified in your original question
target_data = np.array([targets_list])

# Convert the target data to a NumPy array
target_array = np.array(target_data, dtype='float32')

X_train = padded_mfccs
y_train = target_array

print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

y_train = y_train.reshape(-1, 447 * 468 * 3)  # Adjusted reshape

# Training loop
num_epochs = 200
batch_size = 32

for epoch in range(num_epochs):
    print(f"Epoch {epoch+1}/{num_epochs}")

    # Assuming X_train and y_train are NumPy arrays
    history = model.fit(X_train, y_train, epochs=1, batch_size=batch_size)

    # Optionally, you can print or log additional information such as training loss
    print(f"Epoch {epoch+1}/{num_epochs}, Loss: {history.history['loss'][0]}")

# Save the model
model.save("C:/Users/Admin/PycharmProjects/faceDet/src/Training/models/your_model.h5")
