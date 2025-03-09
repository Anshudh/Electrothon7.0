import hashlib
import requests
import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from PIL import Image

# Etherscan API key
etherscan_api_key = "R9NIAM8NVC9K1G4Y4DP2GGGX6AJ64NU2JA"

# Contract address
contract_address = "0x4263415ce070A8d31870F353d35EE5CC90487889"

# Etherscan API URL
url = f"https://api-sepolia.etherscan.io/api?module=account&action=txlist&address={contract_address}&startblock=0&endblock=99999999&sort=desc&apikey={etherscan_api_key}"

# Make the API request
response = requests.get(url)
data = response.json()

# Check if the request was successful
if data["status"] == "1":
    transactions = data["result"]
    if transactions:
        # Print the hash of the most recent transaction
        print(f"Recent Transaction Hash: {transactions[0]['hash']}")
    else:
        print("No transactions found for this address.")
else:
    print("Error retrieving transactions:", data["message"])


Transhash = transactions[0]['hash']


def generate_qr_code(data, qr_code_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(qr_code_path)

def create_affidavit_pdf(data, file_path, qr_code_path):
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    c.drawString(150, height - 80, "Affidavit")
    c.drawString(80, height - 120, f"Name: {data['name']}")
    # c.drawString(80, height - 140, f"Document ID: {data['document_id']}")
    c.drawString(80, height - 160, data['statement1'])
    c.drawString(80, height - 180, data['statement2'])
    c.drawString(80, height - 200, data['statement3'])
    c.drawString(80, height - 220, data['statement4'])
    c.drawString(80, height - 240, data['statement5'])
    c.drawString(80, height - 260, data['statement6'])
    c.drawString(80, height - 280, data['statement7'])
    c.drawString(80, height - 300, data['statement8'])
    c.drawString(80, height - 320, data['statement9'])
    c.drawString(80, height - 340, data['statement10'])

    # Add QR code to the PDF
    qr_code_image = Image.open(qr_code_path)
    qr_code_image.save("qr_code_temp.png")
    c.drawImage("qr_code_temp.png", width - 100, height - 100, width=50, height=50)

    c.save()


def main():
    

        # Generate QR code for the hash
    
        qr_code_path = "qrcode.png"
        generate_qr_code(Transhash, qr_code_path)
        print(f"QR code generated and saved as {qr_code_path}")

        # Create PDF with QR code
 
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        address = input("Enter your address: ")
        exam_year = input("Enter your 12th exam year: ")
        exam_month = input("Enter your 12th exam month: ")
        institute = input("Enter your examination institute: ")
        gap_year = input("Enter your gap year: ")
        issuedate = input("Enter the date of issue: ")


        affidavit_data = {
            'name': name,
            #'document_id': hash_data,
            'statement1': f'I, {name}, aged {age} years, residing at {address}, do hereby solemnly affirm and declare as under:',
            'statement2': '',
            'statement3': f'1. That I have passed my 12th examination in the month of {exam_month}, {exam_year} from {institute}.',
            'statement4': f'2. That I did not pursue any academic or professional course during the year {gap_year}.',
            'statement5': f'3. That the gap year was due to personal reasons and I was not involved in any employment',
            'statement6': ' or business activities during this period.',
            'statement7': '',
            'statement8': 'I declare that the above information is true and correct to the best of my knowledge and belief.',
            'statement9': '',
            'statement10': f'Date of issue: {issuedate}'
        }

        create_affidavit_pdf(affidavit_data, 'affidavit.pdf', qr_code_path)

        print(f"Affidavit document created at affidavit.pdf")

if __name__ == "__main__":
    main()
