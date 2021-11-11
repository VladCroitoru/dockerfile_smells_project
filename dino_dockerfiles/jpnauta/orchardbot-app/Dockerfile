FROM node:8-alpine

RUN apk add --no-cache python make g++  # Epoll

RUN mkdir /app/
WORKDIR /app/

# Install dependencies
COPY package.json .
COPY package-lock.json .
RUN npm install

# Build ./dist folder
COPY src/ src/
COPY bin/ bin/
COPY gulpfile.babel.js .
COPY .babelrc .
RUN npm run build

# Remove dev dependencies
RUN rm -r src/

CMD ["npm", "run", "start:api"]
