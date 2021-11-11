FROM node:10

WORKDIR /usr/src/app

ENV PORT 8080
ENV HOST 0.0.0.0

# Copy package.json and package-lock.json
COPY package*.json ./

RUN npm install --only=production

COPY . .

# Build
RUN npm run build

# Start service
CMD npm start
