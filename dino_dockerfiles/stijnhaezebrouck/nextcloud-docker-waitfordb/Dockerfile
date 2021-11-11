FROM wonderfall/nextcloud:latest

COPY wait-for-db.sh /usr/local/bin/wait-for-db.sh
RUN chmod a+x /usr/local/bin/wait-for-db.sh
CMD ["wait-for-db.sh", "run.sh"]
