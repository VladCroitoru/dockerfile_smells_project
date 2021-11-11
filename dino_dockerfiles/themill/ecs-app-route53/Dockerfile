FROM debian

MAINTAINER Robert Gornall @ The Mill (KHobbits - dkr@khobbits.co.uk)

RUN apt-get update && apt-get install -y curl

ADD cli53-linux-amd64 cli53
RUN chmod +x cli53

ADD update.sh update.sh
RUN chmod +x update.sh

CMD ["/bin/bash", "update.sh"]