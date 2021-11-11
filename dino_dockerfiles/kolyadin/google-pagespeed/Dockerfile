FROM node:7-alpine

MAINTAINER aleksey.kolyadin@isobar.ru

RUN npm install --global psi-v4

# Save compatibility to classic psi
RUN cd /usr/local/bin/ && ln -s /usr/local/bin/psi-v4 ./psi

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["--help"]