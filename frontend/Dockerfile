# Use the official Node.js 14 image as a base
FROM node:18

# Set the working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json files
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of your app's source code from your host to your image filesystem.
COPY . .

# Expose port 3000 to be accessible from the outside
EXPOSE 3000

# Start the development server
CMD ["npm", "run", "dev"]