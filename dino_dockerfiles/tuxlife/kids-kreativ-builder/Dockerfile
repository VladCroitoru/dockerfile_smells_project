FROM golang:stretch
MAINTAINER matthias@tuxlife.net

RUN echo "deb http://packages.cloud.google.com/apt cloud-sdk-stretch main" | tee /etc/apt/sources.list.d/google-cloud-sdk.list \
    && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - \
    && curl -sL https://deb.nodesource.com/setup_9.x | bash -
RUN apt-get update && apt-get install -y google-cloud-sdk google-cloud-sdk-app-engine-go unzip nodejs
  # 'vendor' funktioniert mit gcloud nicht. Die Pakete müssen alle mit 'go get ...' installiert werden
RUN go get \
        github.com/appleboy/gin-jwt \
        github.com/auth0/go-jwt-middleware \
        github.com/dgrijalva/jwt-go \
        github.com/getsentry/raven-go \
        github.com/gin-contrib/cors \
        github.com/gin-contrib/sentry \
        github.com/gin-contrib/sessions \
        github.com/gin-gonic/gin \
        github.com/joho/godotenv \
        github.com/manucorporat/stats \
        golang.org/x/oauth2 \
        google.golang.org/appengine \
        gopkg.in/dgrijalva/jwt-go.v3
RUN npm install -g yarn
RUN yarn global add @angular/cli
RUN ng set --global packageManager=yarn
CMD /bin/bash
