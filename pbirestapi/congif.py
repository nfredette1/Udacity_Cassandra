from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

TENANT_ID = '08a83339-90e7-49bf-9075-957ccd561bf1'
CLIENT_ID = '3097a40e-b90d-46c9-a918-a213cd99de0b'
CLIENT_SECRET = 'hRB8Q~s-jEHwQotVeHLzU_sUrvreErRarslQ_dnS'

KEYVAULT_NAME = 'KV-KEY-CRMDATA'
KEYVAULT_URI = f'https://{KEYVAULT_NAME}.vault.azure.net/'

_credential = ClientSecretCredential( 
        tenant_id=TENANT_ID,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
)

_sc = SecretClient(vault_url=KEYVAULT_URI, credential=_credential)
pbikey = _sc.get_secret('PowerbisecretsKey').value
pbisecret = _sc.get_secret('PowerbisecretsId').value