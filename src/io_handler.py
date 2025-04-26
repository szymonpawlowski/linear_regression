from utils import generate_random_data, load_data_file


def choose_data_source():
    print("\nChoose the source of data:")
    print("1 - Manual data input")
    print("2 - Random data input")
    print("3 - Data from file input")
    choice = input("Enter your choice (1/2/3): ") or "2"
    return choice


def get_data():
    choice = choose_data_source()
    if choice == "1":
        return get_manual_data()
    elif choice == "2":
        return get_random_data()
    elif choice == "3":
        return get_file_data()
    else:
        print("⚠️ Error: Invalid input, generating random data...")
        return get_random_data()


def get_manual_data():
    try:
        X = list(map(float, input("Set X values seperated with space: ").split()))
        y_true = list(map(float, input("Set y values seperated with space: ").split()))
    except ValueError("⚠️ Error: Invalid data!"):
        return None, None
    if len(X) != len(y_true):
        raise ValueError("⚠️ Error: X and Y number of values must be the same!")
        return None, None
    return X, y_true


def get_random_data():
    try:
        n_samples = int(input("Set number of data points (default = 100): ") or "100")
        dim = int(input("Set number of dimensions (default = 1): ") or "1")
        x_min = float(input("Set minimum X value (default = 0): ") or "0")
        x_max = float(input("Set maximum X value (default = 10): ") or "10")
        w_min = float(input("Set minimum weight value (default = 1): ") or "1")
        w_max = float(input("Set maximum weight value (default = 5): ") or "5")
        b_min = float(input("Set minimum bias value (default = -2): ") or "-2")
        b_max = float(input("Set maximum bias value (default = 2): ") or "2")
        noise = float(input("Set noise level (default = 1.0): ") or "1.0")
    except ValueError:
        print("⚠️ Error: Invalid data!")
        print("Setting default values...")
        n_samples, dim = 100, 1
        x_min, x_max = 0, 10
        w_min, w_max = 1, 5
        b_min, b_max = -2, 2
        noise = 1.0

    return generate_random_data(
        n_samples = n_samples,
        dim = dim,
        x_range = (x_min, x_max),
        w_range = (w_min, w_max),
        b_range = (b_min, b_max),
        noise = noise
    )


def get_file_data():
    filepath = input("Enter file path: ").strip()
    return load_data_file(filepath)
