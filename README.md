# 〰️ Linear Regression Model App
Implementation of linear regression in Python.

## 📄 Description
This project implements linear regression from the ground up. The model is learning on randomly generated data, user input data or data from file. Everything is set in a friendly GUI easy to use.
PS. Currently as of July 2025 the project isn't finished.

## 📦 Requirements
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
To launch current version of this project, use this command in your terminal:
```bash
python src/gui/gui.py
```

## 📁 File structure
```bash
linear_regression/
│
├── src/
│   │
│   ├── data/
│   │   ├── input_handler.py
│   │   └── validators.py
│   │
│   ├── gui/
│   │   ├── buttons.py
│   │   ├── callbacks
│   │   └── gui.py
│   │
│   ├── model/
│   │   ├── regression.py
│   │   └── utils.py
│   │
│   └── test/
│       ├── test_input_handler.py
│       └── test_regression.py
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
