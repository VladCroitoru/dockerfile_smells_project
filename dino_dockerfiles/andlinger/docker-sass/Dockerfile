FROM node:14-alpine

RUN apk update \
  && apk add --no-cache jq optipng jpegoptim

RUN wget -q -O /usr/bin/yq $(wget -q -O - https://api.github.com/repos/mikefarah/yq/releases/latest | jq -r '.assets[] | select(.name == "yq_linux_amd64") | .browser_download_url') \
  && chmod +x /usr/bin/yq
RUN npm install -g svgo sass

ENTRYPOINT ["/usr/bin/env"]