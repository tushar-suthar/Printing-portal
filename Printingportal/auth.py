from requests_oauthlib import OAuth2Session
import os
import time

# This is necessary for testing with non-HTTPS localhost
# Remove this if deploying to production
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# This is necessary because Azure does not guarantee
# to return scopes in the same case and order as requested
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'
os.environ['OAUTHLIB_IGNORE_SCOPE_CHANGE'] = '1'

authorize_url = '{0}{1}'.format("https://login.microsoftonline.com/850aa78d-94e1-4bc6-9cf3-8c11b530701c", "/oauth2/v2.0/authorize")
token_url = '{0}{1}'.format("https://login.microsoftonline.com/850aa78d-94e1-4bc6-9cf3-8c11b530701c", "/oauth2/v2.0/token")

# Method to generate a sign-in url
def get_sign_in_url():
  # Initialize the OAuth client
  aad_auth = OAuth2Session("67a6bd75-52d5-4837-a21f-05eac382221e",
    scope="openid profile offline_access user.read calendars.read",
    redirect_uri="http://localhost:5000/callback"
  )

  sign_in_url, state = aad_auth.authorization_url(authorize_url, prompt='login')

  return sign_in_url, state

# Method to exchange auth code for access token
def get_token_from_code(callback_url, expected_state):
  # Initialize the OAuth client
  aad_auth = OAuth2Session("67a6bd75-52d5-4837-a21f-05eac382221e",
    state=expected_state,
    scope="openid profile offline_access user.read calendars.read",
    redirect_uri="http://localhost:5000/callback"
  )

  token = aad_auth.fetch_token(token_url,
    client_secret = "TPP.3L1r~UYpM2Lz_7bxDu7ISaj.86R.Oz",
    authorization_response=callback_url)

  return token


def store_token(request, token):
      request.session['oauth_token'] = token



# <GetTokenSnippet>
def get_token(request):
  token = request.session['oauth_token']
  if token != None:
    # Check expiration
    now = time.time()
    # Subtract 5 minutes from expiration to account for clock skew
    expire_time = token['expires_at'] - 300
    if now >= expire_time:
      # Refresh the token
      aad_auth = OAuth2Session("67a6bd75-52d5-4837-a21f-05eac382221e",
        token = token,
        scope="openid profile offline_access user.read calendars.read",
        redirect_uri="http://localhost:5000/callback"
      )

      refresh_params = {
        'client_id': "67a6bd75-52d5-4837-a21f-05eac382221e",
        'client_secret': "TPP.3L1r~UYpM2Lz_7bxDu7ISaj.86R.Oz",
      }
      new_token = aad_auth.refresh_token(token_url, **refresh_params)

      # Save new token
      store_token(request, new_token)

      # Return new access token
      return new_token

    else:
      # Token still valid, just return it
      return token
# </GetTokenSnippet>

def remove_user_and_token(request):
  if 'oauth_token' in request.session:
    del request.session['oauth_token']

  if 'user' in request.session:
    del request.session['user']

def get_user(token):
  graph_client = OAuth2Session(token=token)
  # Send GET to /me
  user = graph_client.get('{0}/me'.format('https://graph.microsoft.com/v1.0'))
  # Return the JSON result
  return user.json()

def store_user(request, user):
  request.session['user'] = {
    'is_authenticated': True,
    'name': user['displayName'],
    'email': user['mail'],
    'roll_number': user['surname'],
    'shopkeeper_status': True if(user['mail'] == 'abc@gmail.com') else False
  }