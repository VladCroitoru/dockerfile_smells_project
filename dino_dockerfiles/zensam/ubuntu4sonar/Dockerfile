FROM ubuntu:xenial

# ENV TERM=xterm

RUN apt-get update \
    && apt-get install -y curl dnsutils build-essential libssl-dev openssl nodejs sudo wget
    # && apt-get install -y dnsutils build-essential libssl-dev openssl sudo \
    # && echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers \
    # && rm -rf /var/lib/apt/lists/*

############################################
# Configure Jenkins
############################################
# Switch to user jenkins
# USER jenkins
