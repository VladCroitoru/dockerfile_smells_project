FROM google/cloud-sdk

RUN apt-get update && apt-get install -y gnupg

COPY backup /usr/bin/backup
RUN chmod +x /usr/bin/backup
RUN mkdir /scratch

CMD ["/usr/bin/backup"]
