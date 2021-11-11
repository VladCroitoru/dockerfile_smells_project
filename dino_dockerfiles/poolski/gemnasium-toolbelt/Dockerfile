FROM debian

ENV VERSION 1.0.3

RUN apt-get update && \
 	apt-get install -qy wget && \
 	wget -q https://github.com/gemnasium/toolbelt/releases/download/1.0.3/gemnasium-toolbelt_1.0.3_amd64.deb -O /tmp/gemnasium.deb && \
 	dpkg -i /tmp/gemnasium.deb

CMD /bin/bash
