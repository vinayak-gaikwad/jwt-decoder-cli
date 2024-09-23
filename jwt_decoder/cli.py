import sys
import json
import jwt
from jwt.exceptions import DecodeError

def decode_jwt(token):
    try:
        header = jwt.get_unverified_header(token)
        payload = jwt.decode(token, options={"verify_signature": False})

        result = {
            "header": header,
            "payload": payload
        }

        print(json.dumps(result, indent=2))
    except DecodeError as e:
        print(f"Error decoding token: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main():
    if len(sys.argv) == 1:
        token = sys.stdin.read().strip()
    elif len(sys.argv) == 2:
        token = sys.argv[1]
    else:
        print("Usage: jwt-decoder [<jwt_token>]", file=sys.stderr)
        print("   or: echo <jwt_token> | jwt-decoder", file=sys.stderr)
        sys.exit(1)

    if not token:
        print("No JWT token provided", file=sys.stderr)
        sys.exit(1)

    decode_jwt(token)

if __name__ == "__main__":
    main()
