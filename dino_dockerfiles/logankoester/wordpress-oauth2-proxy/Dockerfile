FROM node
EXPOSE 80 433

ENV HOST="example.com" \
    TARGET="localhost" \
    TARGET_SCHEME="http" \
    TARGET_PREPEND="" \
    HTTP_PORT="80" \
    HTTPS_PORT="443" \
    HTTPS_FORCE="false" \
    KEY_FILE="server.key" \
    CERT_FILE="server.crt" \
    DB_URI="mongodb://localhost/auth" \
    SESSION_SECRET="changeme" \
    OAUTH_CLIENT_ID="changeme" \
    OAUTH_CLIENT_SECRET="changeme" \
    OAUTH_URL="https://wordpress.example" \
    OAUTH_CALLBACK_URL="https://service.example/auth/wordpress/callback"

ADD . /usr/src/wordpress-oauth2-proxy
WORKDIR /usr/src/wordpress-oauth2-proxy
RUN npm install
ENTRYPOINT ["node", "index.js"]
