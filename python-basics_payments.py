#!/usr/bin/python3

import base64

base64_encoded = 'c2hvcElkOjEyMzQuc2NpZDo0MzIxLmN1c3RvbWVyTnVtYmVyOmFiYzAwMC5zaG9wQXJ0aWNsZUlkOjU2Nzg5MC5wYXltZW50VHlwZTpBQy5vcmRlck51bWJlcjphYmMxMTExMTExLmN1c3ROYW1lOkpvaG4gRG9lLmN1c3RBZGRyOtCc0L7RgdC60LLQsCwg0LAv0Y8gMTAwLm9yZGVyRGV0YWlsczrQodGH0LDRgdGC0YzQtSDQtNC70Y8g0LLRgdC10YUsINCyINC/0LDQutC10YLQuNC60LDRhSwg0YDQvtGB0YHRi9C/0YzRjg=='

def decode_base64_to_dict(base64_encoded):
    base64_decoded_dict = {}
    base64_decoded_dict_chunks = base64.b64decode(base64_encoded).decode("utf-8").split('.')   
    for chunk in base64_decoded_dict_chunks:
        key, value = chunk.split(':')
        if value.isnumeric():
            value = int(value)
        base64_decoded_dict[key] = value
    return base64_decoded_dict

def print_dict(base64_decoded_dict):
    for key, value in base64_decoded_dict.items():
        print('{key}: {value}'.format(key = key, value = value))

def main():
    base64_decoded_dict = decode_base64_to_dict(base64_encoded)
    print_dict(base64_decoded_dict)        

if __name__ == "__main__":
    main()
