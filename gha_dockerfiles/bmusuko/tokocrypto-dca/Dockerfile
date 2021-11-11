FROM node:12-alpine

# Add package file
WORKDIR /app
COPY package.json ./
COPY yarn.lock ./

# Copy source
COPY src ./src
COPY prisma ./prisma
COPY tsconfig.json ./tsconfig.json

# Install deps
RUN yarn
RUN /app/node_modules/.bin/prisma generate --schema=/app/prisma/schema.prisma

# Build dist
RUN yarn build

CMD yarn start