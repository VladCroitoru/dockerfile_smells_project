FROM alpine

WORKDIR /code

ENV APK_PACKAGES bash alpine-sdk ca-certificates
ENV NODE_ENV production

RUN apk \
    --update-cache \
    --update add \
    "nodejs<8.0.0" \
    "nodejs-npm" \
    ${APK_PACKAGES} \
    && rm -rf /var/cache/apk/*

EXPOSE 9090

COPY package.json ./

# Build
RUN npm install && npm cache clean

COPY . .

ENTRYPOINT ["node", "src/sig-server/bin.js"]

