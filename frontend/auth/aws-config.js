import dotenv from 'dotenv';

dotenv.config();

const awsconfig = {
  Auth: {
    region: process.env.NEXT_PUBLIC_AWS_REGION,
    userPoolId: process.env.NEXT_PUBLIC_USER_POOL_ID,
    userPoolWebClientId: process.env.NEXT_PUBLIC_USER_POOL_WEB_CLIENT_ID,
    identityPoolId: process.env.NEXT_PUBLIC_IDENTITY_POOL_ID,
    oauth: {
      domain: process.env.NEXT_PUBLIC_OAUTH_DOMAIN,
      scope: ['openid', 'profile', 'email'],
      redirectSignIn: process.env.NEXT_PUBLIC_REDIRECT_SIGN_IN,
      redirectSignOut: process.env.NEXT_PUBLIC_REDIRECT_SIGN_OUT,
      responseType: process.env.NEXT_PUBLIC_RESPONSE_TYPE,
    },
  },
};

export default awsconfig;
