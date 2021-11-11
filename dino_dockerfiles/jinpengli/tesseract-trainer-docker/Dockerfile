#
# Dockerfile for tesseract
#

FROM ubuntu:16.04
MAINTAINER kev <mr.li.jinpeng@gmail.com>

RUN set -xe \
    && echo "deb http://us.archive.ubuntu.com/ubuntu trusty main universe" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y autoconf \
                          build-essential \
                          git \
                          libcairo2 \
                          libcairo2-dev \
                          libgomp1 \
                          libicu55 \
                          libicu-dev \
                          liblept4 \
                          libleptonica-dev \
                          libpango1.0-0 \
                          libpango1.0-dev \
                          libtool \
                          libicu-dev \
                          fonts-wqy-zenhei \
    && git clone https://github.com/tesseract-ocr/tesseract.git \
        && cd tesseract \
        && ./autogen.sh \
        && ./configure \
        && make install \
        && make training \
        && make training-install \
        && ldconfig \
        && cd .. \
    && git clone https://github.com/tesseract-ocr/langdata.git \
    && git clone https://github.com/tesseract-ocr/tessdata.git \
        && cd tessdata \
        && mv * /usr/local/share/tessdata/ \
        && cd .. 
#    && apt-get purge --auto-remove -y autoconf \
#                                      build-essential \
#                                      git \
#                                      libcairo2-dev \
#                                      libicu-dev \
#                                      libleptonica-dev \
#                                      libpango1.0-dev \
#                                      libtool \
#    && rm -rf tesseract tessdata /var/cache/apk/*


RUN git clone https://github.com/JinpengLI/tesseract-trainer-docker.git /root/tesseract-trainer-docker 
RUN set -xe && cd /root/tesseract-trainer-docker/example_train && ls && ./train.sh

## build a ssh server so that the user cannot use it from ssh
RUN apt-get update && apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:screencast' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
