FROM ubuntu:latest

# Installing needed soft
RUN apt-get update -y && \
    apt-get -y install curl unzip vim

# Adding scripts and rsync conf
COPY rclone.conf /root/.config/rclone/
COPY *.sh /

RUN chmod +x /*.sh

RUN /install_rclone.sh

CMD ["sh", "-c", "/run.sh"]
