import secrets
import string

alphanum = string.ascii_letters + string.digits
#alphanum = string.hexdigits
password = ''.join(secrets.choice(alphanum) for i in range(10))

print(password)