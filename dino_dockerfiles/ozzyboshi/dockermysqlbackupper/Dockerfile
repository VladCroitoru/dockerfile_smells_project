From ubuntu:16.04
MAINTAINER Ozzyboshi <gun101@email.it>

ENV DEBIAN_FRONTEND noninteractive

# Automysqlbackup installation
RUN apt-get update && apt-get -y install automysqlbackup curl unzip man-db

# Rclone installation
RUN curl -O http://downloads.rclone.org/rclone-current-linux-amd64.zip
RUN unzip rclone-current-linux-amd64.zip
RUN cd rclone-*-linux-amd64 && cp rclone /usr/sbin/ && chown root:root /usr/sbin/rclone && chmod 755 /usr/sbin/rclone && mkdir -p /usr/local/share/man/man1 && cp rclone.1 /usr/local/share/man/man1/ && mandb && rm /rclone-current-linux-amd64.zip

# Add custom scripts
ADD mysqlbackupper.sh /mysqlbackupper.sh
ADD mysqluploader.sh /mysqluploader.sh
RUN chmod +x /mysqlbackupper.sh /mysqluploader.sh

CMD ["/mysqlbackupper.sh"]

