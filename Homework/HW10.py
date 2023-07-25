byte_string = b'r\xc3\xa9sum\xc3\xa9'
#  UTF-8)
decoded_string = byte_string.decode()
print("Декодировано в строковый вид (кодировка по умолчанию):", decoded_string)
#  'Latin1'
latin1_bytes = decoded_string.encode('latin1')
print("Преобразовано обратно в байтовый вид (кодировка Latin1):", latin1_bytes)
# (по умолчанию)
final_string = latin1_bytes.decode()
print("Декодировано в строковый вид (кодировка по умолчанию):", final_string)
