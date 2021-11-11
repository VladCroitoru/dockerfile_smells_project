FROM ubuntu
MAINTAINER FinalDuty <root@finalduty.me>
CMD /bin/bash

ADD https://raw.githubusercontent.com/finalduty/configs/master/.vimrc /root/
ADD https://raw.githubusercontent.com/finalduty/configs/master/.bashrc /root/

RUN sed -i -e '/^$/d' -e '/^#/d' -e '/^deb-src/d' -e 's/archive\.ubuntu\.com/mirror.webhost.co.nz/' /etc/apt/sources.list
RUN apt-get update && apt-get upgrade -y; apt-get clean -y &>/dev/null
RUN apt-get install vim curl -y; apt-get clean -y &>/dev/null

