import argparse
import requests
import json

def output(data, prefix="> "):
    for key, value in data.items():
        print(f"{prefix}{key.capitalize()}: ", end="")
        if isinstance(value, dict):
            print()
            output(value, "  ")
        else:
            print(value)

def upload_file(file_path, expires):
    with open(file_path, 'rb') as file:
        response = requests.post(
            'https://file.io/',
            files   = {
                'file': file,
                'expires': (None, str(expires)),
            }
        )
        output(response.json())

def main():
    parser = argparse.ArgumentParser(description='[ PYTHON FILE UPLOADER ]')
    parser.add_argument('file', help='Example: /path/to/file.txt')
    parser.add_argument('--exp', metavar='', default='10h', help='Set expiration time (e.g., 1h, 2d) (default: 10h)')
    args = parser.parse_args()
    upload_file(args.file, args.exp)

if __name__ == "__main__":
    main()
