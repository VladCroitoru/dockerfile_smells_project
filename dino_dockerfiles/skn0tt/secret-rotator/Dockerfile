FROM node:12

WORKDIR /app

# Build `lib`
COPY lib/yarn.lock lib/package.json ./lib/
RUN yarn --cwd lib

COPY lib/tsconfig.json ./lib/
COPY lib/src/ ./lib/src/
RUN yarn --cwd lib build

# Build `api`
COPY api/yarn.lock api/package.json ./api/
RUN yarn --cwd api

COPY api/tsconfig.json ./api/
COPY api/src/ ./api/src/
RUN yarn --cwd api build

EXPOSE 3000

CMD node api/dist/index.js
