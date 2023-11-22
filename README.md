<h1>Implementation of Data Encryption Standard in python</h1>

<h3>File Breakdown</h3>

<ul>

<li><b>KeyGen.py:</b> contains the methods related to creating keys and sub keys</li>

<li><b>Conversions.py:</b> contains utility methods for converting between ascii, binary, and hex encoding</li>

<li><b>tables.py:</b> contains the permutation, substitution, and shifting tables used in the encryption process</li>

<li><b>BitOperations.py:</b> contains utility methods for performing bitwise operations</li>

<li><b>DES.py:</b> main file contining the methods related to encrypting and decrypting text</li>

</ul>

<h3>How to Use</h3>

<h4>Standalone:</h4>
    Run DES.py and input text to terminal prompt. Encrypted and decrypted text is returned to standard output

<h4>As Package:</h4>
<ul>
<li><b>To Encrypt:</b> Call Encryt() function in DES.py, parameters are text(required, encoded as ascii string) and key (optional, 64bit hexadecimal string). Function returns encrypted text (hexadecimal encoded string) and ke  (64bit hexadecimal string).</li>

<li><b>To Decrypt:</b> Call Decrypt() function in DES, parameters are encrypted string (required, hexadecimal encoded string), and decryption key (required, hexadecimal encoded string). Function returns decrypted text (ascii encoded string).</li>
</ul>