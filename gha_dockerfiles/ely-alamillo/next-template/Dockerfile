FROM node:lts as dependencies

WORKDIR /next-starter-template
COPY package.json package-lock.json ./
RUN npm ci

FROM node:lts as builder
WORKDIR /next-starter-template
COPY . .
COPY --from=dependencies /next-starter-template/node_modules ./node_modules
RUN npm run build

FROM node:lts as runner
WORKDIR /next-starter-template
ENV NODE_ENV production
# If you are using a custom next.config.js file, uncomment this line.
COPY --from=builder /next-starter-template/next.config.js ./
COPY --from=builder /next-starter-template/public ./public
COPY --from=builder /next-starter-template/.next ./.next
COPY --from=builder /next-starter-template/node_modules ./node_modules
COPY --from=builder /next-starter-template/package.json ./package.json

EXPOSE 3000
CMD ["npm", "start"]