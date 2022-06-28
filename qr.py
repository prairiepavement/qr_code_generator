# qr.py

import argparse
from PIL import Image
from pyqrcode import QRCode


def read_user_cli_args():
    """
    Handles the CLI user interactions.

    Returns:
        argparse.Namespace: Populated namespace object
    """
    parser = argparse.ArgumentParser(
        description="gets URL to generate QR code"
    )
    
    parser.add_argument(
        "url", 
        type=str, 
        help="enter url"
    )

    parser.add_argument(
        "version", 
        choices=range(1, 41), 
        default=1,
        type=int, 
        nargs='?',
        help="enter version"
    )

    parser.add_argument(
        "error_correction", 
        choices=['-L','-M','-Q','-H'], 
        default='-M',
        type=str, 
        nargs='?',
        help="enter error correction"
    )

    return parser.parse_args()



if __name__ == "__main__":
    user_args = read_user_cli_args()
    print(user_args.url, user_args.version, user_args.error_correction)
