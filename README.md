# Electrothon7.0
Automated Affidavit Generator
This is a platform which automates the process of affidavit generation which would be a faster, transparent and tamper proof process. This would not only reduce human efforts but would also generate higher revenue for government.
1. We take required information from the user then verify it with the help of government API's (if access granted)
2. After verification, affidavit will be generated with a specified format.
3. Alongside we deploy a contract account on remix Ethereum and then transact with the help of metamask account.
4. The transaction hash generated during that transaction will be used to generate a unique QR code with the help of qrcode module.
5. That qr code will be pasted on the generated format of affidavit.
6. This qr code will be used for proving the authenticity of that affidavit by comparing the qr code with the etherscan transaction data.
