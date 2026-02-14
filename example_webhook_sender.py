from http_client import AcmeHTTPClient

with AcmeHTTPClient(
    mtls_cert=("pki/acme-webhook-client.crt", "pki/acme-webhook-client.key"),
    ca_cert="pki/acme-dev-root-ca.crt",
    timeout=5.0,
) as client:

    payload = {
        "event": "user.created",
        "user_id": "12345"
    }

    r = client.post("https://service.example.com/acme-webhook-consumer", json=payload)
    print(r.status_code)
    print(r.text)
