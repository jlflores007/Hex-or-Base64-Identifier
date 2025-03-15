import argparse
import base64
import binascii
import re

def is_base64(s):
    """Check if a string is valid Base64 and has valid padding."""
    try:
        decoded = base64.b64decode(s, validate=True)
        return base64.b64encode(decoded).decode() == s.strip()  # Ensure it round-trips
    except binascii.Error:
        return False


def is_hex(s):
    """Check if a string is Hex-encoded."""
    return bool(re.fullmatch(r'[0-9a-fA-F]+', s)) and len(s) % 2 == 0

def check_encoding(s):
    """Ensure Hex check runs first to avoid false Base64 detection."""
    if is_hex(s):
        return "Hex"
    elif is_base64(s):
        return "Base64"
    return "Unknown"


def main():
    """Parse arguments and check string encoding."""
    parser = argparse.ArgumentParser(
        description="Check if a string is Hex or Base64.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("-s", "--string", help="String to analyze", required=True)

    args = parser.parse_args()
    
    result = check_encoding(args.string)
    print(f"Identified Encoding: {result}")

if __name__ == "__main__":
    main()

    