FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
# RUN npm install --production
# Creating a dummy package.json in the step before would be better, 
# but for skeleton we can just create index.js directly.
# Using a simple script to init package.json if missing logic in a real build.
# For this skeleton, we assume src is mounted or copied.
COPY . .
# We will create a minimal server without dependencies for the skeleton "hello"
CMD ["node", "src/index.js"]
