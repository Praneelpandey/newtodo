from cryptography.hazmat.primitives.serialization import pkcs12
from cryptography.hazmat.primitives import serialization
from cryptography import x509
import base64

# Load Private Key
with open("ios.key", "rb") as f:
    key = serialization.load_pem_private_key(f.read(), password=None)

# Load Certificate (Apple usually provides it in DER format)
with open("ios_development.cer", "rb") as f:
    cert_data = f.read()
    cert = x509.load_der_x509_certificate(cert_data)

# Create the .p12 package
p12_data = pkcs12.serialize_key_and_certificates(
    name=b"ios_dev",
    key=key,
    cert=cert,
    cas=None,
    encryption_algorithm=serialization.BestAvailableEncryption(b"github_password")
)

# Write out the .p12 file
with open("ios.p12", "wb") as f:
    f.write(p12_data)

# Generate Base64 for the .p12 (for GitHub Secrets)
with open("tmp_cert.b64", "w") as f:
    f.write(base64.b64encode(p12_data).decode("utf-8"))

# Generate Base64 for the Provisioning Profile (for GitHub Secrets)
with open("TodoApp_Development_Profile.mobileprovision", "rb") as f:
    pp_data = f.read()

with open("tmp_pp.b64", "w") as f:
    f.write(base64.b64encode(pp_data).decode("utf-8"))

print("SUCCESS! Generated ios.p12 and Base64 strings for GitHub Actions.")
