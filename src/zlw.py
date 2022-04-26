def zlw(text):
    compressed_list = compress_zlw(text)
    compressed_binary = make_zlw_binary(compressed_list)
    return compressed_binary

def un_zlw(compressed_binary):
    print(compressed_binary)
    compressed_list = get_compressed_list_from_binary(compressed_binary)
    print(compressed_list)
    text = un_compress_zlw(compressed_list)
    print(text)
    return text

def compress_zlw(text):
    values = {}
    for i in range(256):
        values[chr(i)] = i
    next_value = 256
    compressed_list = []
    current_character = text[0]
    for i in range(1, len(text)):
        next_character = text[i]
        if current_character + next_character in values:
            current_character += next_character
        else:
            compressed_list.append(values[current_character])
            values[current_character + next_character] = next_value
            next_value += 1
            current_character = next_character
    compressed_list.append(values[current_character])
    return compressed_list

def make_zlw_binary(compressed_list):
    compressed_binary = ""
    for value in compressed_list:
        value_in_binary = format(value, "012b")
        compressed_binary += value_in_binary
    over_from_bytes = len(compressed_binary) % 8
    if over_from_bytes == 0:
        extra_bits = ""
        extra_bits_needed = 0
    else:
        extra_bits_needed = 8 - over_from_bytes
        extra_bits = "0" * extra_bits_needed
    return str(format(extra_bits_needed, "08b")) + extra_bits + compressed_binary

def un_compress_zlw(compressed_list):
    values = {}
    for i in range(256):
        values[i] = chr(i)
    text = ""
    value = 256
    current_value = compressed_list[0]
    text += values[current_value]
    for i in range(1, len(compressed_list)):
        next_value = compressed_list[i]
        if next_value in values:
            curr_string = values[next_value]
        else:
            curr_string = values[current_value] + last_character
        text += curr_string
        last_character = curr_string[0]
        values[value] = values[current_value] + last_character
        value += 1
        current_value = next_value
    return text

def get_compressed_list_from_binary(data_in_binary):
    extra_bits_needed = int(data_in_binary[0:8], 2)
    compressed_binary = data_in_binary[8+extra_bits_needed:]
    compressed_list = []
    for i in range(0, len(compressed_binary), 12):
        value = int(compressed_binary[i:i+12], 2)
        compressed_list.append(value)
    return compressed_list
