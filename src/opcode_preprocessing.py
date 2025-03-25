# opcode_preprocessing.py

import os

def extract_opcodes_from_asm(file_path):
    opcodes = []
    with open(file_path, 'r', encoding='latin-1') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) > 1:
                opcodes.append(parts[1])  # Skip address part
    return opcodes

def process_folder(folder_path):
    data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.asm'):
            file_path = os.path.join(folder_path, filename)
            opcodes = extract_opcodes_from_asm(file_path)
            data[filename] = opcodes
    return data
