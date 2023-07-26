byte_string = b'r\xc3\xa9sum\xc3\xa9'
decoded_string = byte_string.decode('latin1')
print("(кодировка по умолчанию):", decoded_string)
latin1_bytes = decoded_string.encode('latin1')
print("(кодировка Latin1):", latin1_bytes)
final_string = latin1_bytes.decode()
print("(кодировка по умолчанию):", final_string)