FROM mwaeckerlin/ubuntu-base
MAINTAINER mwaeckerlin

ENV PORT 8000
EXPOSE ${PORT}

RUN apt-get update && apt-get install -y safechat
RUN useradd -r -s /bin/false safechat
RUN chown safechat.safechat /etc/safechat.json
ADD start.sh /start.sh
WORKDIR /usr/share/safechat/nodejs
USER safechat
CMD  /start.sh
