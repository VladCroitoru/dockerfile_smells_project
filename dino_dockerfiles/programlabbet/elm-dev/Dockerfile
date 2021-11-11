FROM node:7
MAINTAINER Anders Hansson <anders@programlabbet.se>
RUN apt-get update -y && apt-get install -y rsync && apt-get clean -y
RUN npm install -g yarn
RUN yarn global add elm@0.18.0
RUN yarn global add elm-github-install
RUN mkdir -p /app /app-sync
VOLUME /app
VOLUME /app-sync
WORKDIR /app-sync
COPY *.sh /
RUN chmod 755 /*.sh
CMD ["/bin/bash", "-c", "/start.sh"]
