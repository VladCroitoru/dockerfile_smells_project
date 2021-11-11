FROM node:14

# --build-arg
ARG PUBLIC_URL
ENV PUBLIC_URL=$PUBLIC_URL

# Install frontend dependencies
WORKDIR /usr/src/app/client
COPY client/package.json client/package-lock.json ./
RUN npm ci

# Install backend dependencies
WORKDIR /usr/src/app/server
COPY server/package.json server/package-lock.json ./
RUN npm ci

# Build frontend
WORKDIR /usr/src/app
COPY client client/
WORKDIR /usr/src/app/client
RUN npm run build
RUN cp -r build/ ../server/build

# Copy backend
WORKDIR /usr/src/app
COPY server server/
WORKDIR /usr/src/app/server

EXPOSE 3001

CMD npm run start:prod