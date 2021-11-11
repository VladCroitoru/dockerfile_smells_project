FROM transistor1/netextender
MAINTAINER Cecile Tonglet <cecile.tonglet@gmail.com>

ADD https://raw.githubusercontent.com/guilhem/apt-get-install/master/apt-get-install /usr/bin/
RUN chmod +x /usr/bin/apt-get-install

RUN apt-get-install dropbear

RUN mkdir /root/.ssh

ENTRYPOINT ["/bin/bash"]
CMD ["-c", "cat /authorized_keys > /root/.ssh/authorized_keys && (dropbear -E; exec /netextender/netExtenderClient/netExtender)"]
