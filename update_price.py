import base64
import sys

if __name__ == "__main__":
    exec(base64.b64decode(sys.argv[1]))
