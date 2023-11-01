import requests

# Set up OAuth credentials
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'
redirect_uri = 'YOUR_REDIRECT_URI'

# Step 1: Get authorization code
authorization_url = f'https://accounts.google.com/o/oauth2/auth?' \
                     f'client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&scope=https://www.googleapis.com/auth/fitness.activity.read'
print(f'Visit the following URL and authorize access: {authorization_url}')
authorization_code = input('Enter the authorization code: ')

# Step 2: Get access token
access_token_url = 'https://accounts.google.com/o/oauth2/token'
access_token_payload = {
    'code': authorization_code,
    'client_id': client_id,
    'client_secret': client_secret,
    'redirect_uri': redirect_uri,
    'grant_type': 'authorization_code'
}

access_token_response = requests.post(access_token_url, data=access_token_payload)
access_token = access_token_response.json()['access_token']

# Step 3: Make API request to get heart rate data
heart_rate_url = 'https://www.googleapis.com/fitness/v1/users/me/dataSources/derived:com.google.heart_rate.bpm:com.google.android.gms:merge_heart_rate_bpm/datasets/1596154385153000000-1596154385153000000'
headers = {'Authorization': f'Bearer {access_token}'}

response = requests.get(heart_rate_url, headers=headers)

if response.status_code == 200:
    print(response.json())
else:
    print(f'Error fetching data. Status code: {response.status_code}')
