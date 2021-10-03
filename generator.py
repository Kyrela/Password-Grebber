import base64
"""
The program generator. You will find here everything that you need to complete
yourself for set up the program.
"""


# modes are the name of the different modes you want to be existing
modes = (
    "Classic",                  # mode 0
    "with no special characters",  # mode 1
    "with no digit",            # mode 2
    "text only",                # mode 3
)

def generate(key: str, mode=0) -> str:
    """
    Generate a password according to the given key, for the specified mode

    :param key: The key used to generate the password
    :param mode: The generation mode
    :return: the generated password
    """
 # You can edit "random" with anything

    if mode == 0:
        key = "random" + key
        message_bytes = key.encode('UTF-8')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('UTF-8')
        chiffre = base64_message + str(len(base64_message))
        end = chiffre + "*"
        return end
    elif mode == 1:
        key = "random" + key
        message_bytes = key.encode('UTF-8')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('UTF-8')
        end = base64_message + str(len(base64_message))
        return end
    elif mode == 2:
        key = "random" + key
        message_bytes = key.encode('UTF-8')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('UTF-8')
        end = base64_message + "*"
        return end
    elif mode == 3:
        key = "random" + key
        message_bytes = key.encode('UTF-8')
        end = base64.b64encode(message_bytes)
        return end
