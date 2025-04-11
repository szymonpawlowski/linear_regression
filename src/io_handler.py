import random

def custom_data_list(prompt):
    # list of comma seperated values
    while True:
        try:
            raw = input(prompt)
            return [float(x.strip()) for x in raw.split(",")]
        except ValueError:
            print("⚠️ Error: Input comma seperated data!")

def get_user_input():
    print("===== Linear Regression Data Input =====")
    mode = input("Custom data (C) or Random data (R)? [C/R]: ").upper().strip()
    
    if mode == "C":
        print("===== Custom Data Input =====")
        X = custom_data_list("Set X values: ")
        y = custom_data_list("Set y values: ")
        
        if len(X) != len(y):
            raise ValueError("⚠️ Error: X and y number of values must be the same!")
        
    elif mode == "R":
        print("===== Random Data Input =====")
        count = int(input("How many data points to generate? ") or "30")
        X_min = float(input("Minimum X value: ") or "0")
        X_max = float(input("Maximum X value: ") or "10")
        a = float(input("Slope a: ") or "2")
        b = float(input("Bias b: ") or "4")
        noise = float(input("Noise: ") or "1.0")
        
        X = [random.uniform(X_min, X_max) for _ in range(count)]
        y = [a * x + b + random.uniform(-noise, noise) for x in X]
        
    try:
        epochs = int(input("Epochs: "))
    except ValueError:
        raise ValueError("⚠️ Error: Incorrect number of epochs! Setting default: 1000")
        epochs = 1000
        
    try:
        learning_rate = float(input("Learning rate: "))
    except ValueError:
        raise ValueError("⚠️ Error: Incorrect learning rate! Setting default: 0.01")
        learning_rate = 0.01
    
    return X, y, epochs, learning_rate