## 🛠️ Technologies Used
- Python
- Scikit-learn (PCA, SVM)
- NumPy
- LabelEncoder (for opcode encoding)
- Django (for optional frontend/UI)

## 📂 Dataset
- ASM files of applications (malware + benign)
- OpCode sequences are extracted and analyzed
- Labels used to classify malware vs benign
- Robustness tested with junk-code inserted variants

## 📁 Project Structure

iot-malware-detection/  
├── src/  
│   ├── opcode_preprocessing.py         # Extracts opcodes from .asm files  
│   ├── eigenspace_classifier.py        # Applies PCA + SVM for malware classification  
├── report/  
│   └── malware_detection_report.pdf    # Complete project report  
├── README.md                           # Project overview and documentation  

## 👨‍💻 Author

**Khoushik Raj Rasumalla**  
Bachelor's in Computer Science  
📫 Email: k.rasumalla@wsu.edu  
💼 LinkedIn: [linkedin.com/in/khoushikraj](https://www.linkedin.com/in/khoushikraj)  
💻 GitHub: [github.com/khoushikraj](https://github.com/khoushikraj)
