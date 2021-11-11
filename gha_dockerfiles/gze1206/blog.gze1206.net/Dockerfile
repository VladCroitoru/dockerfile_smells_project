FROM node:lts

# Locale & Timezone
ENV LANG C.UTF-8
ENV TZ Asia/Seoul

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install vim -y && \
    yarn global add @vue/cli && \
    yarn global add @vue/cli-init

EXPOSE 3000
WORKDIR /root

CMD tail -f /dev/null