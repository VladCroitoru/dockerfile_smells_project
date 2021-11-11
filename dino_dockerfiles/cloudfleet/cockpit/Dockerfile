# cloudfleet cockpit
#
# VERSION 0.2

FROM dockerfile/nodejs

ADD . $HOME/cockpit
RUN cd $HOME/cockpit/; scripts/install.sh

# If you want to run the container without starting up cockpit specify --entrypoint="/bin/bash" on run
# ENTRYPOINT ["$HOME/cockpit/scripts/start.sh"]

CMD $HOME/cockpit/scripts/start.sh

EXPOSE 3000
EXPOSE 80
