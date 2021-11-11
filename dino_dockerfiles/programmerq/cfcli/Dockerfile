FROM node
RUN npm install -g cloudflare-cli
RUN apt-get -y update && apt-get -y install gettext-base && apt-get -y clean
ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD cfcli
