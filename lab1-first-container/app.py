import sys
import datetime

def main():
    print("Hello from inside Docker!")
    print(f"Running Python {sys.version.split()[0]}")
    print(f"Today is: {datetime.date.today()}")

if __name__ == "__main__":
    main()
