# STAGE ONE: Build our React APP
FROM node:12.14.0 as build
ARG NPM_TOKEN

USER root

WORKDIR /app

# Copy NPM package files
COPY package.json .
COPY .npmrc .

# RUN npm install
RUN npm cache clean --force
RUN npm install

# Copy the remaining files over
# and build a production build
COPY . .
RUN npm run production
RUN rm -r .npmrc

# Setup an HTTPD server
FROM node:12.14.0

WORKDIR /app

# Copy production files
COPY --from=build /app/index.html .
COPY --from=build /app/index.js .
COPY --from=build /app/sitemap.xml .
COPY --from=build /app/dist dist/
COPY --from=build /app/express-only.package.json ./package.json
RUN npm install

# Start webserver on port 80
CMD ["npm", "run", "serve"]