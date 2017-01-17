import os
import flickrapi

api_key = os.environ.get('FLICKR_KEY')
api_secret = os.environ.get('FLICKR_SECRET')
import requests_oauthlib

# OAuth URLs
request_token_url = 'https://www.flickr.com/services/oauth/request_token'
access_token_url = 'https://www.flickr.com/services/oauth/access_token'
authorization_url = 'https://www.flickr.com/services/oauth/authorize'

sess = requests_oauthlib.OAuth1Session(client_key=api_key, client_secret=api_secret,
    signature_method=u'HMAC-SHA1', signature_type=u'AUTH_HEADER',
    callback_uri='oob')

# First step, fetch the request token:
request_token = sess.fetch_request_token(request_token_url)
oauth_token = request_token.get('oauth_token')
oauth_token_secret = request_token.get('oauth_token_secret')
print('token='+oauth_token)
print('token_secret='+oauth_token_secret)

# Second step, follow this link and authorize:
print (sess.authorization_url(authorization_url))

# Third step, fetch the access token:
pin = input('Paste the pin here.')
sess.params['oauth_verifier'] = pin
r = sess.get(access_token_url + '?oauth_token=' + oauth_token)
print (r)
#print (sess.parse_authorization_response(redirect_response))
#print (sess.fetch_access_token(access_token_url))

# Done! You can now make authenticated requests using the token and token secret.

#flickr = flickrapi.FlickrAPI(api_key, api_secret)
#flickr.get_request_token(oauth_callback='oob')
#authorize_url = flickr.auth_url(perms='read')
#print(authorize_url)

