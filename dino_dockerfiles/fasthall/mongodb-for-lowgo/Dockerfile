FROM mongo:3.7

RUN apt update
RUN apt install python python-requests python-yaml -y
COPY report.py /
COPY docker-entrypoint.sh /usr/local/bin
CMD ["docker-entrypoint.sh"]