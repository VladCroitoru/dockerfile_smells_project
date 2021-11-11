FROM mhart/alpine-node:10.16.0

RUN apk add --no-cache python3 bc git libexif udev chromium chromium-chromedriver xvfb ttf-freefont curl bash jq
RUN python3 -m pip install boto3

ENV CHROME_BIN chromium-browser
