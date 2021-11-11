FROM alpine:3.5
MAINTAINER ninthwalker <ninthwalker@gmail.com>

#copy slack-welcome files
COPY . /slack-welcome
WORKDIR /slack-welcome

# ---------------------------------------------
# THESE WERE THE COMMANDS IN PHUSION.
# RUN mkdir -p /etc/my_init.d && \
# mkdir -p /etc/service/httpserver
# ADD /root/add_web_body.sh /etc/my_init.d/add_web_body.sh
# ADD /root/httpserver.sh /etc/service/httpserver/run
# ----------------------------------------------------

RUN apk --no-cache add \
nodejs

RUN npm install

CMD ["npm", "start"]
