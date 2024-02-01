from django.contrib.auth.hashers import make_password
from django.conf import settings
settings.configure()
# Your plaintext password
plaintext_password = "HIPOPKAdidopka"

# Hash the password
hashed_password = make_password(plaintext_password)
print(hashed_password)
# Store or use the hashed password as needed

