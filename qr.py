# qr.py


import argparse
import qrcode
import validators
import sys
from colour import Color


versions = [1, 5, 10, 20, 40]
error_correction_levels = ['L','M','Q','H']


def read_user_cli_args():
    """
    Handles the CLI user interactions.

    Returns:
        argparse.Namespace: Populated namespace object
    """
    parser = argparse.ArgumentParser(
        description="Gets URL from user and generates custom color QR code",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "url", 
        type=str, 
        help="Enter the URL you would like to convert to a QR code."
    )

    parser.add_argument(
        "-v",
        "--version", 
        choices=versions, 
        default=1,
        type=int, 
        nargs='?',
        help="""
            Enter the version of QR code you desire.
            The 'version' indicates the size, or number of modules, of a QR code. 
            A larger version contains greater data, along with increasing the size of the QR code.

            There exist five versions to choose from:

            1, or 21 x 21 modules

            5, or 37 x 37 modules

            10, or 57 x 57 modules

            20, or 97 x 97 modules

            40, or 177 x 177 modules

            The default is set to the standard version 1, or 21 x 21 modules.
            """,
        metavar='\b'
    )

    parser.add_argument(
        "-error",
        "--error", 
        choices=error_correction_levels, 
        default='M',
        type=str, 
        nargs='?',
        help="""
            Enter the level of error correction for the QR code you desire.
            Error correction allows for the capability to restore data should the QR code become damaged or dirty. 
            
            There exist four error correction levels to choose from: 
            
            Note: Raising the level increases the error correction capability but also increases the amount of data.


            ERROR CORRECTION LEVEL L:
                Error Correction: About 7%% or less errors can be corrected.
                Usage: General marketing purposes.

            ERROR CORRECTION LEVEL M:
                Error Correction: About 15%% or less errors can be corrected.
                Usage: General marketing purposes.
            
            ERROR CORRECTION LEVEL Q:
                Error Correction: About 25%% or less errors can be corrected.
                Usage: Industrial.

            ERROR CORRECTION LEVEL H:
                Error Correction: About 30%% or less errors can be corrected.
                Usage: Industrial.


            The default is set to the standard error correction level, M.
            """,
        metavar=''
    )

    return parser.parse_args()


def validate_url():
    """
    """
    
    if not validators.url(user_args.url):
        sys.exit("\nPlease enter only a URL. If you require help, use the '-h' flag.\n")


def convert_error_correction():
    """
    """

    if user_args.error == "L":
        user_args.error = qrcode.constants.ERROR_CORRECT_L
        return
    elif user_args.error == "M":
        user_args.error = qrcode.constants.ERROR_CORRECT_M
        return
    elif user_args.error == "Q":
        user_args.error = qrcode.constants.ERROR_CORRECT_Q
        return
    else:
        user_args.error = qrcode.constants.ERROR_CORRECT_H
        return


def check_color(color):
    """
    """
    
    try:
        color = color.replace(" ", "")
        Color(color)
        return True
    except ValueError:
        return False


def build_qr_code(url, version, error):
    """
    """

    qr = qrcode.QRCode(
        version=version,
        error_correction=error,
    )

    qr.add_data(url)
    qr.make(fit=True)


    while True:
        fill_color = input("Please enter your fill color: ")
        back_color = input("Please enter your background color: ")
        
        if check_color(fill_color) and check_color(back_color):
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            break
        else:
            print(f"\nOops! It appears either {fill_color} or {back_color} isn't a valid color! If you would like help in deciding, you can search here: https://www.w3.org/TR/css-color-3/#svg-color. Please try again.\n")


    while True:
        filename = input("Save file as: ")
        
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img.save(filename)
            break
        else:
            print("Please enter .jpg or .png file type.")
    
    return 




if __name__ == "__main__":
    user_args = read_user_cli_args()
    validate_url()
    convert_error_correction()
    build_qr_code(user_args.url, user_args.version, user_args.error)