<h1>Implementation of Data Encryption Standard in python</h1>

<h3>File Breakdown</h3>
<hl>

<b>KeyGen.py:</b> contains the methods related to creating keys and sub keys

<b>Conversions.py:</b> contains utility methods for converting between ascii, binary, and hex encoding

<b>tables.py:</b> contains the permutation, substitution, and shifting tables used in the encryption process

<b>BitOperations.py:</b> contains utility methods for performing bitwise operations

<b>DES.py:</b> main file contining the methods related to encrypting and decrypting text.

<h3>How to Use</h3>
<hl>
<h4>Standalone:</h4>
Run DES.py and input text to terminal prompt. Encrypted and decrypted text is returned to standard output

<h4>As Package</h4>
<b>To Encrypt:</b> Call Encryt() function in DES.py, parameters are text(required, encoded as ascii string) and key (optional, 64bit hexadecimal string). Function returns encrypted text (hexadecimal encoded string) and ke  (64bit hexadecimal string).

<b>To Decrypt:</b> Call Decrypt() function in DES, parameters are encrypted string (required, hexadecimal encoded string), and decryption key (required, hexadecimal encoded string). Function returns decrypted text (ascii encoded string).
