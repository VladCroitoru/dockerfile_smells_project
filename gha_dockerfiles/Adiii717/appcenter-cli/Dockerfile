FROM node:alpine
RUN apk add --no-cache bash
RUN npm install -g appcenter-cli
ENV APK_FILE_PATH=""
ENV USER_NAME=""
ENV PROJECT_NAME=""
ENV APP_CENTER_TOKEN=""
COPY entrypoint.sh /usr/bin/entrypoint.sh
RUN chmod +x /usr/bin/entrypoint.sh
WORKDIR /app
ENTRYPOINT [ "/usr/bin/entrypoint.sh" ]