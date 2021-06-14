from django.shortcuts import render 
from django.urls import reverse
from django.http import HttpResponseRedirect
from Printingportal.auth import get_sign_in_url, get_token_from_code, store_token, store_user, remove_user_and_token, get_user


#major content
#signin
#signout
#callback


def main(request):

    return render(request,'main.html')

def sign_in(request):
  # Get the sign-in URL
  sign_in_url, state = get_sign_in_url()
  # Save the expected state so we can validate in the callback
  request.session['auth_state'] = state
  # Redirect to the Azure sign-in page
  return HttpResponseRedirect(sign_in_url)

def sign_out(request):
  # Clear out the user and token
  remove_user_and_token(request)

  return HttpResponseRedirect('main')

def callback(request):
  # Get the state saved in session
  expected_state = request.session.pop('auth_state', '')
  # Make the token request
  token = get_token_from_code(request.get_full_path(), expected_state)

  # Get the user's profile
  user = get_user(token)

  # Save token and user
  store_token(request, token)
  store_user(request, user)

  return HttpResponseRedirect('home')