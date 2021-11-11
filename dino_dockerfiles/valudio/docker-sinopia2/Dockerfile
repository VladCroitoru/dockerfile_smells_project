FROM node
LABEL maintainer="Valudio <development@valudio.com>"
RUN mkdir -p /opt/sinopia/storage
WORKDIR /opt/sinopia
RUN npm install js-yaml sinopia2
ADD /config.yaml /tmp/config.yaml
ADD /start.sh /opt/sinopia/start.sh
CMD ["sh", "/opt/sinopia/start.sh"]
EXPOSE 4873
VOLUME /opt/sinopia