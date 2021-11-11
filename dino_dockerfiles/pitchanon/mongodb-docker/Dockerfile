FROM mongo:3.4

MAINTAINER Pitchanon Dumrongsiri <Pitchanon.d@gmail.com>

ENV AUTH yes
ENV STORAGE_ENGINE wiredTiger
ENV JOURNALING yes


ADD run.sh /run.sh
ADD set_mongodb_password.sh /set_mongodb_password.sh
RUN chmod +x /run.sh
RUN chmod +x /set_mongodb_password.sh

ENTRYPOINT ["/run.sh"]
