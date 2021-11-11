FROM debian:latest
MAINTAINER Marc Rooding <admin@webresource.nl>

RUN apt-get update && apt-get install -y gnumeric curl

COPY ./ssconvert-xls-to-csv.sh /ssconvert-xls-to-csv.sh

ENTRYPOINT ["/ssconvert-xls-to-csv.sh"]