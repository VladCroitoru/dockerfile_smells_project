FROM qnib/dplain-node

ARG RC_VERSION=latest
RUN mkdir -p /opt/rocketchat \
 && apt-get update \
 && apt-get install -y graphicsmagick build-essential \
 && curl -SLf "https://rocket.chat/releases/${RC_VERSION}/download" | tar xfz - -C /opt/rocketchat \
 && echo
RUN echo \
 && cd /opt/rocketchat/bundle/programs/server \
 && npm install \
 && npm cache clear

ENV MONGO_URL=mongodb://rocketchat_database:27017/rocketchat \
    HOME=/data/rocketchat \
    PORT=3000 \
    ROOT_URL=http://0.0.0.0:3000 \
    Accounts_AvatarStorePath=/app/uploads
VOLUME ["/data/rocketchat"]
COPY opt/qnib/rocketchat/bin/start.sh /opt/qnib/rocketchat/bin/
CMD ["/opt/qnib/rocketchat/bin/start.sh"]
