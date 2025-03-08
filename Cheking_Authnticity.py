import requests
import cv2
from pyzbar.pyzbar import decode

# Etherscan API key
etherscan_api_key = "R9NIAM8NVC9K1G4Y4DP2GGGX6AJ64NU2JA"

# Contract address
contract_address = "0xa94342867054F2F44eBcCc920fbDE8e177745260"

def get_transaction_history(contract_address):
    # Etherscan API URL
    url = f"https://api-sepolia.etherscan.io/api?module=account&action=txlist&address={contract_address}&startblock=0&endblock=99999999&sort=desc&apikey={etherscan_api_key}" 
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching transaction history: {response.status_code}")
        return None

def scan_qr_code(image_path):
    # Read the image
    img = cv2.imread(image_path)
    # Decode the QR code
    decoded_objects = decode(img)
    for obj in decoded_objects:
        # Return the decoded data
        return obj.data.decode('utf-8')
    return None

def compare_hash_with_transactions(contract_address, hash_to_check):
    transactions = get_transaction_history(contract_address)
    if transactions and transactions['status'] == '1':
        for tx in transactions['result']:
            if tx['hash'] == hash_to_check:
                return True
    else:
        print("No transactions found or error in fetching transactions.")
    return False

if __name__ == "__main__":
    # Replace with the path to your QR code image
    qr_image_path = "qrcode.png"
    hash_to_check = scan_qr_code(qr_image_path)

    if hash_to_check:
        
        result = compare_hash_with_transactions(contract_address, hash_to_check)
        if result:
            print("Document is Authentic")
        else:
            print("Document is not Authentic")
    else:
        print("No QR code found in the image.")
