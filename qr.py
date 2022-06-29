# qr.py


import argparse
import qrcode


def read_user_cli_args():
    """
    Handles the CLI user interactions.

    Returns:
        argparse.Namespace: Populated namespace object
    """
    parser = argparse.ArgumentParser(
        description="gets URL to generate QR code",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        "url", 
        type=str, 
        help="Enter the URL you would like to convert to a QR code."
    )

    parser.add_argument(
        "-v", 
        choices=[1, 5, 10, 20, 40], 
        default=1,
        type=int, 
        nargs='?',
        help="""
            Enter the version of QR code you desire.
            The 'version' indicates the size, or number of modules, of a QR code. 
            A larger version contains greater data, along with increasing the size of the QR code.

            The default is set to the standard version 1, or 21 x 21 modules.
            """
    )

    parser.add_argument(
        "-e", 
        choices=['L','M','Q','H'], 
        default='M',
        type=str, 
        nargs='?',
        help="""
            Enter the level of error correction for the QR code you desire.
            Error correction allows for the capability to restore data should the QR code become damaged or dirty. 
            There exist four error correction levels to choose from. Raising the level increases the error correction capability but also increases the amount of data.


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
            """
    )

    return parser.parse_args()


def convert_error_correction():
    """
    """

    if user_args.e == "L":
        user_args.e = qrcode.constants.ERROR_CORRECT_L
        return
    elif user_args.e == "M":
        user_args.e = qrcode.constants.ERROR_CORRECT_M
        return
    elif user_args.e == "Q":
        user_args.e = qrcode.constants.ERROR_CORRECT_Q
        return
    else:
        user_args.e = qrcode.constants.ERROR_CORRECT_H
        return


def build_qr_code(url, version, error):
    """
    """

    qr = qrcode.QRCode(
        version=version,
        error_correction=error,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    filename = input("Save file as: ")

    if filename.endswith(".jpg") or filename.endswith(".png"):
        img.save(filename)
    else:
        raise ValueError("Please enter .jpg or .png file type")
    
    return 




if __name__ == "__main__":
    user_args = read_user_cli_args()
    convert_error_correction()
    build_qr_code(user_args.url, user_args.v, user_args.e)