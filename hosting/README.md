# Hosting Documentation

## POC Phase Hosting
Hosting is done by `render.com` & `Vercel`

- Frontend: Next.js on Vercel
- Backend: FastAPI on render.com

## Production Hosting (50 Users)

Option A: Upgrade Vercel & render.com to Pro version to avoid major cloud providers can simplify this stack.

- Vercel Costs: $240/yr
- Render.com Costs: $240/yr

Logic set for production build is once `user > 50` then go to either Google Cloud, Azure & AWS.