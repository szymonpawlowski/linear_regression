# 📈 Linear Regression Model App
Implementation of linear regression in Python. Current version: 1.0.0

## 📄 Description
This project implements linear regression from the ground up. The model is learning on randomly generated data, user input data or data from file. Everything is set in a friendly GUI easy to use.


## 📌 Requirements
In order for this project to work you'll need:
- Python 3.x
- Tkinter
- Numpy
- Matplotlib

## 📥 Installation
To install required libraries, use this command in your terminal:
```bash
pip install -r requirements.txt
```

## ▶️ Launch
To launch this project, use this command in your terminal:
```bash
python src/main.py
```

## 📁 File structure
```bash
linear_regression/
│
├── src/
│   │
│   ├── gui/
│   │   ├── data_ui.py
│   │   ├── gui.py
│   │   ├── options_ui.py
│   │   └── training_ui.py
│   │
│   ├── regression/
│   │   ├── model.py
│   │   ├── trainer.py
│   │   └── utils.py
│   │
│   ├── test/
│   │   ├── test_input_handler.py
│   │   └── test_regression.py
│   │
│   └── config.py
│
├── .gitignore
├── LICENSE.txt
├── main.py 
├── README.md
└── requirements.txt
```

## 👤 Author
- Szymon Pawłowski (szymonpawlowski)

## 📃 License
This project is released with GNU GPLv3 license.
