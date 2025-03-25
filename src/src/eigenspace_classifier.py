# eigenspace_classifier.py

import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def flatten_opcode_sequences(data_dict, max_len=1000):
    data = []
    for seq in data_dict.values():
        padded = seq[:max_len] + ['NOP'] * max(0, max_len - len(seq))
        data.append(padded)
    return np.array(data)

def encode_features(opcode_data):
    # Flatten to 1D list for encoding
    flat = [op for seq in opcode_data for op in seq]
    encoder = LabelEncoder()
    encoder.fit(flat)

    # Transform each sequence
    encoded = [encoder.transform(seq) for seq in opcode_data]
    return np.array(encoded)

def eigenspace_learning(X, y):
    pca = PCA(n_components=50)
    X_pca = pca.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)
    model = SVC(kernel='linear')
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Classification Accuracy: {acc * 100:.2f}%")

# Example usage (this part would be used in your main script):
# data_dict = process_folder("dataset/")
# opcode_sequences = flatten_opcode_sequences(data_dict)
# encoded_data = encode_features(opcode_sequences)
# labels = [...]  # Load labels here
# eigenspace_learning(encoded_data, labels)
