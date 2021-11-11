# https://docs.docker.com/engine/examples/running_ssh_service/
FROM ubuntu:16.04

ENV GITHUB_USER_NAME nabeken

RUN apt-get update && apt-get install -y openssh-server curl
RUN mkdir /var/run/sshd
RUN mkdir /root/.ssh && chmod 0700 /root/.ssh

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

ADD start.sh /start.sh

EXPOSE 22
CMD ["/start.sh"]
