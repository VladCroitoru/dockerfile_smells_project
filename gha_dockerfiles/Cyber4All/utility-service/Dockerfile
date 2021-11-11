# Build Stage 
FROM node:12 as build
WORKDIR /build
COPY . .
COPY package.json package-lock.json* .env* ./
RUN npm install
RUN npm test
RUN npm run build

# ----------------------------------------------------------------
# SERVE STAGE
# ----------------------------------------------------------------
FROM node:12-alpine as serve
WORKDIR /opt/app
COPY package.json package-lock.json* .env* ./
COPY --from=build /build/dist ./dist
RUN npm install --only=prod
EXPOSE 9000
CMD ["node", "dist/app.js"]