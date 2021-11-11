# dependencies
FROM node:16-alpine as dependencies
WORKDIR /usr/src/app

COPY package*.json ./
COPY backend/package*.json ./backend/
COPY frontend/package*.json ./frontend/
RUN npm ci

# backend and frontend are built separately to enable aggressive caching and parallelism

# build the backend
FROM dependencies as build-backend
COPY backend ./backend
RUN npm run build -w backend

# build the frontend
FROM dependencies as build-frontend
COPY frontend ./frontend
RUN npm run build -w frontend

# execution
FROM node:16-alpine
WORKDIR /usr/src/app

# - install PRODUCTION dependencies
COPY package*.json ./
COPY backend/package*.json ./backend/
COPY frontend/package*.json ./frontend/
RUN npm ci --production

# - add the already compiled code
COPY server.js ./
COPY --from=build-backend /usr/src/app/backend/build ./backend/build
COPY --from=build-frontend /usr/src/app/frontend/build ./frontend/build

# - ports
EXPOSE 8080

# - start the server ("production" skips the build step)
CMD ["npm", "run", "production"]
