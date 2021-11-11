ARG ENVIRONMENT=production

FROM node:16-alpine3.14 as build_development
WORKDIR /app
COPY package-lock.json package-lock.json
COPY package.json package.json
RUN npm i

FROM node:16-alpine3.14 as build_production
WORKDIR /app
COPY dist dist

FROM build_${ENVIRONMENT}

CMD ["node", "dist/main.js"]
