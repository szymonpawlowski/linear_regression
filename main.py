import sys
import os

current_dir = os.path.dirname(__file__)
src_path = os.path.join(current_dir, 'src')
if src_path not in sys.path:
    sys.path.append(src_path)

try:
    from gui.gui import LinearRegressionApp
except ImportError as e:
    print(f"Import error: {e}")
    print(f"Searched paths: {sys.path}")
    sys.exit(1)

def main():
    app = LinearRegressionApp()

if __name__ == "__main__":
    main()
