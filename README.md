# jupyter-jub-oauth
[JupyterHub](https://github.com/jupyterhub/jupyterhub) with [Google OAuth](https://developers.google.com/identity/protocols/OAuth2).

The idea is that all of the generic, reusable config lives in the `ninjaben/jupyter-jub-oauth` Dockerfile.

Then all of the site-specific config, like SSL and users, goes in a separate [`deploy-helper`](https://github.com/benjamin-heasly/jupyter-hub-oauth/blob/master/deploy-helper) script and gets mounted into the Docker container at run time.

### Deployment
To do your own deployment, you'd copy the `deploy-helper`, edit it with your own site-specific config, and run it.  Or just use the `deploy-helper` as documentation for how to work with `ninjaben/jupyter-jub-oauth`.  You do you!

Here are the site-specific configs you need:
 - Google account email addresses for known users.  At least one admin (you!).
 - A domain name where you'll host your JupyterHub.  You can use `lvh.me` to point back at localhost, which is great for testing.
 - OAuth Web app Client Id and Client Secred obtained from your [Google Developer Console](https://console.developers.google.com/apis/credentials).
 - Your own SSL certificate and key.  Or, the `deploy-helper` can self-sign one for you.

# Thanks
This image was inspired by the jupyterhub official [oauthenticator example](https://github.com/jupyterhub/oauthenticator/tree/master/example).  Thanks!
