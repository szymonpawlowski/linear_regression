import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from gui.gui import LinearRegressionApp


def main():
    app = LinearRegressionApp()

if __name__ == "__main__":
    main()
