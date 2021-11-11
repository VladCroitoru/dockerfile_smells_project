FROM docker:stable

WORKDIR /app

RUN apk add --no-cache \
  certbot \
  curl \
  bash

RUN wget -O ./updateSecret.sh https://gist.githubusercontent.com/chrisns/3b10035acac131904bc1d28a80fb02df/raw/d4a63792c4d03d1dd0f77ddfb96f7b48d5c5b7dc/updateSecret.sh \
  && chmod +x ./updateSecret.sh

ENV PATH=${PATH}:/app
COPY update-godaddy.sh run.sh ./

ENTRYPOINT []
CMD ./run.sh
