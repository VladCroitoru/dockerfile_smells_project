# docker build --tag ccarcaci/apispecmd-ts .
# docker run --rm --env INPUT_SPEC=input/petstore.yaml --env OUTPUT_MARKDOWN=output/petstore.md --env OUTPUT_PDF=output/petstore.pdf --volume $PWD/openapi/examples:/app/input --volume $PWD/openapi/examples/output:/app/output --name apispecmd-ts ccarcaci/apispecmd-ts:latest

FROM node:fermium-alpine3.14

WORKDIR /app

# Installs latest Chromium (89) package.
RUN apk add --no-cache \
      chromium \
      nss \
      freetype \
      harfbuzz \
      ca-certificates \
      ttf-freefont

# Tell Puppeteer to skip installing Chrome. We'll be using the installed package.
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true \
    PUPPETEER_EXECUTABLE_PATH=/usr/bin/chromium-browser

# Puppeteer v6.0.0 works with Chromium 89.
RUN npm install --global puppeteer@6.0.0
RUN npm install --global @bitacode/apispecmd-ts

CMD [ "apispecmd-ts" ]
