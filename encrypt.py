import base64
import zlib
import os

# Storage ka full path yahan likhein
input_file = "/storage/emulated/0/newtool.py"
output_file = "/storage/emulated/0/nabin.py"

if not os.path.exists(input_file):
    print(f"[-] Error: '{input_file}' file nahi mili!")
    exit()

with open(input_file, "rb") as f:
    data = f.read()

compressed_data = zlib.compress(data)
encoded_data = base64.b64encode(compressed_data).decode('utf-8')

stub = f'''import base64, zlib
exec(zlib.decompress(base64.b64decode({repr(encoded_data)})).decode('utf-8'))
'''

with open(output_file, "w", encoding="utf-8") as f:
    f.write(stub)

print("[+] Successfully Encrypted!")
print(f"[+] Saved to: {output_file}")
