# Authetication Documentation

Authentication is done by `Cognito` for the providers of Github, Google & Microsoft.

Base connection in `auth/aws-config.js` with implementation in frontend/ dir.  See following steps for frontend integration

## Step 1

```bash
npm install aws-amplify @aws-amplify/ui-react dotenv
```

## Step 2 

Update .env
```bash
NEXT_PUBLIC_AWS_REGION=us-east-1
NEXT_PUBLIC_USER_POOL_ID=us-east-1_XXXXXXXXX
NEXT_PUBLIC_USER_POOL_WEB_CLIENT_ID=XXXXXXXXXXXXXXXXXXXXXX
NEXT_PUBLIC_IDENTITY_POOL_ID=us-east-1:XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
NEXT_PUBLIC_OAUTH_DOMAIN=your-cognito-domain.auth.us-east-1.amazoncognito.com
NEXT_PUBLIC_REDIRECT_SIGN_IN=http://localhost:3000/
NEXT_PUBLIC_REDIRECT_SIGN_OUT=http://localhost:3000/
NEXT_PUBLIC_RESPONSE_TYPE=code
```
