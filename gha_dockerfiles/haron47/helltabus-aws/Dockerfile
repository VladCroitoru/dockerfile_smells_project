FROM node:14.16.0-alpine3.11 as builder
WORKDIR /app

COPY package.json ./
COPY ./tsconfig.json ./

RUN npm install

COPY . .
## compile typescript
RUN npm run build
## remove packages of devDependencies
# RUN npm prune --production
# ===================================================
FROM node:14.16.0-alpine3.11 as runtime
WORKDIR /app

# ENV NODE_ENV="development"
# ENV DOCKER_ENV="development"
# ENV PORT=5000
## Copy the necessary files form builder
COPY --from=builder "/app/dist/" "/app/dist/"
COPY --from=builder "/app/node_modules/" "/app/node_modules/"
COPY --from=builder "/app/package.json" "/app/package.json"


EXPOSE 3000
CMD ["npm", "run", "start"]