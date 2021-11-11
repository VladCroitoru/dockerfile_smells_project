FROM debian:latest

RUN apt update -y && \
    apt upgrade -y && \
    apt install lintian vim git -y

COPY .bashrc /root/.bashrc
COPY corrections /usr/share/lintian/data/spelling/
COPY fix_typo.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/fix_typo.sh

CMD ["bash"]
