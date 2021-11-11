FROM vladus2000/alpine-base-glibc-user
MAINTAINER vladus2000 <docker@matt.land>

COPY shiz/ /

ENV STARTUP_CMD="/spider --headless"

RUN \
        /update.sh && \
	wget https://spideroak.com/release/spideroak/slack_tar_x64 && \
	tar zxvf slack_tar_x64 && \
	rm -f slack_tar_x64

CMD /bin/ash -c /startup.sh

VOLUME /root/.config/SpiderOakONE/
VOLUME /home/user/.config/SpiderOakONE/
VOLUME /root/SpiderOak Hive/
VOLUME /home/user/SpiderOak Hive/

