FROM circleci/openjdk:8-jdk-browsers

RUN apt-get update && \
        apt-get install ruby &&\
        rm -rf /var/lib/apt/lists/*

RUN gem install bundler

# GHR
ADD https://github.com/tcnksm/ghr/releases/download/v0.5.4/ghr_v0.5.4_linux_amd64.zip /tmp
RUN unzip /tmp/ghr_v0.5.4_linux_amd64.zip  -d /usr/local/bin && rm /tmp/ghr_v0.5.4_linux_amd64.zip
