FROM alpine:3.4

# Install base packages
RUN apk update && apk add --no-cache build-base bash wget curl make nodejs ruby ruby-bundler ruby-rdoc ruby-irb ruby-dev

RUN gem install github-markup redcarpet RedCloth org-ruby creole asciidoctor

COPY server.js /app/server.js

RUN (cd /app && npm install express body-parser randomstring)

CMD node /app/server.js
