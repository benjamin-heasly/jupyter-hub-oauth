# Configuration file for Jupyter Hub

c = get_config()

# Path to SSL certificate and key
c.JupyterHub.ssl_key = '/srv/oauthenticator/ssl/ssl.key'
c.JupyterHub.ssl_cert = '/srv/oauthenticator/ssl/ssl.crt'

# Logging
c.JupyterHub.log_level = 'DEBUG'

# Shared notebooks
c.Spawner.notebook_dir = '/srv/ipython/examples'
c.Spawner.args = ['--NotebookApp.default_url=/notebooks']

# OAuth and user configuration
c.JupyterHub.authenticator_class = 'oauthenticator.LocalGoogleOAuthenticator'

c.LocalGoogleOAuthenticator.create_system_users = True
c.Authenticator.add_user_cmd = ['adduser', '--force-badname', '-q', '--gecos', '""', '--ingroup', 'jupyter', '--disabled-password']

c.Authenticator.whitelist = whitelist = set()
c.Authenticator.admin_users = admin = set()


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

c.LocalGoogleOAuthenticator.client_id = os.environ['OAUTH_CLIENT_ID']
c.LocalGoogleOAuthenticator.client_secret = os.environ['OAUTH_CLIENT_SECRET']
c.LocalGoogleOAuthenticator.oauth_callback_url = os.environ['OAUTH_CALLBACK_URL']


