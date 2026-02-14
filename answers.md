1. What assumptions and design choices did you make? Why? What are the trade-offs? 
I kept the PKI intentionally simple — single Dev/UAT root CA and file based certs — just to prove the mTLS flow end-to-end. I avoided overengineering (no intermediates, no automation) since this is a prototype. Tradeoff is weaker isolation and key handling, but it keeps testing fast and easy to reason about.

2. How would you productionize this implementation?
In prod I’d move cert issuance to ACM PCA or similar and store keys in Vault/Secrets Manager instead of disk. Short lived client certs + rotation would be key. I’d also add logging around TLS failures and probly layer request signing on top for defense in depth.

3. Write instructions/documentation for other security engineers at Acme Co to manage/maintain this implementation.
Treat the root CA like core security infrastructure — rotate it only through a planned process since it anchors trust for everything downstream. Only the public CA cert should ever be shared externally; the private key stays tightly controlled. If a client cert is compromised, revoke it and issue a new one rather than trying to workaround the risk. From an operational side, expirations are usually the biggest source of outages, so having alerting and visibility into cert lifecycles is pretty important.
jtkftenkerbglluevunkrglvvitdhljlugdbjbvbdtkj

4. Write instructions for the end customer to validate that the new webhooks sent from Acme’s SaaS have mTLS.
Customers need to require client cert auth on their HTTPS endpoint and trust the Acme CA. They should confirm the TLS handshake shows the acme-webhook-client identity. If requests work without a cert, config is wrong.

5. What other security mechanisms can be used instead of mTLS? Why would customers ask for mTLS vs the other mechanisms?
You could use HMAC signatures, API tokens, JWTs, or IP allowlists. Those are simpler but rely on shared secrets or headers. Teams ask for mTLS because identity is enforced at the transport layer and fits zero-trust models, even tho setup is a bit heavier.

