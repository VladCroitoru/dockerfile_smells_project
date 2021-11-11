FROM node:16.10-alpine AS builder

ENV NEXT_PUBLIC_APP_URL https://ChevCast.tv
ENV NEXT_PUBLIC_CHEVCAST_DISCORD https://discord.gg/d7Rr6Xw
ENV NEXT_PUBLIC_CHEVCAST_FACEBOOK https://www.facebook.com/ChevCastTV
ENV NEXT_PUBLIC_CHEVCAST_TWITCH https://twitch.tv/ChevCast
ENV NEXT_PUBLIC_CHEVCAST_TWITTER https://twitter.com/ChevCast
ENV NEXT_PUBLIC_CHEVCAST_YOUTUBE https://www.youtube.com/channel/UC9sAMOGfyW5wgWuKfbm7VTA

# Check https://github.com/nodejs/docker-node/tree/b4117f9333da4138b03a546ec926ef50a31506c3#nodealpine to understand why libc6-compat might be needed.
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY . .
RUN npm ci
RUN npm run build

ENV NODE_ENV production

RUN addgroup -g 1001 -S nodejs
RUN adduser -S nextjs -u 1001
RUN chown nextjs:nodejs ./.next

USER nextjs

EXPOSE 3000

# Next.js collects completely anonymous telemetry data about general usage.
# Learn more here: https://nextjs.org/telemetry
# Uncomment the following line in case you want to disable telemetry.
# ENV NEXT_TELEMETRY_DISABLED 1

CMD ["npm", "start"]