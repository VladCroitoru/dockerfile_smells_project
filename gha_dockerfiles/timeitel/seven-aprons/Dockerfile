FROM node:current-alpine AS base
WORKDIR /base
COPY package*.json ./
RUN npm install
COPY . .

FROM base AS build
ARG NEXT_PUBLIC_STRIPE_KEY
ENV NEXT_PUBLIC_STRIPE_KEY=${NEXT_PUBLIC_STRIPE_KEY}
ENV NODE_OPTIONS=--openssl-legacy-provider
WORKDIR /build
COPY --from=base /base ./
RUN npm run build

FROM node:current-alpine AS production
WORKDIR /app
COPY --from=build /build/package*.json ./
COPY --from=build /build/.next ./.next
COPY --from=build /build/public ./public
RUN npm install next

EXPOSE 3000
CMD npm run start