# Configuration file for Jupyter Hub

c = get_config()

# Path to SSL key file for the public facing interface of the proxy
# 
# Use with ssl_cert
c.JupyterHub.ssl_key = '/srv/oauthenticator/ssl/ssl.key'

# Path to SSL certificate file for the public facing interface of the proxy
# 
# Use with ssl_key
c.JupyterHub.ssl_cert = '/srv/oauthenticator/ssl/ssl.crt'

c.JupyterHub.log_level = 10
c.JupyterHub.authenticator_class = 'oauthenticator.GoogleOAuthenticator'

c.Authenticator.whitelist = whitelist = set()
c.JupyterHub.admin_users = admin = set()

import os
import sys

join = os.path.join

here = os.path.dirname(__file__)
root = os.environ.get('OAUTHENTICATOR_DIR', here)
sys.path.insert(0, root)

with open(join(root, 'userlist')) as f:
    for line in f:
        if not line:
            continue
        parts = line.split()
        name = parts[0]
        whitelist.add(name)
        if len(parts) > 1 and parts[1] == 'admin':
            admin.add(name)

c.GoogleOAuthenticator.client_id = os.environ['OAUTH_CLIENT_ID']
c.GoogleOAuthenticator.client_secret = os.environ['OAUTH_CLIENT_SECRET']
c.GoogleOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']

# ssl config
ssl = join(root, 'ssl')
keyfile = join(ssl, 'ssl.key')
certfile = join(ssl, 'ssl.cert')
if os.path.exists(keyfile):
    c.JupyterHub.ssl_key = keyfile
if os.path.exists(certfile):
    c.JupyterHub.ssl_cert = certfile

