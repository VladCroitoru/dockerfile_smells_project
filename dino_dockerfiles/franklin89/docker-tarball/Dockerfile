FROM nginx:latest

MAINTAINER Matteo Locher (matteo.locher@ml-software.ch)

EXPOSE 80

# Install dependencies
RUN apt-get update && apt-get install bzip2

# Copy archived webpage
COPY src/ /tmp/

# Join splitted archive files
RUN cat /tmp/web.tar.gz.* > /tmp/backup.tar.gz.joined

# Unarchive tar files
RUN cd tmp && tar -xf backup.tar.gz.joined

# move the extracted data to /usr/share/nginx/html
RUN cd /tmp/src && mv * /usr/share/nginx/html

# remove temporary folder again
RUN rm -rf /tmp 