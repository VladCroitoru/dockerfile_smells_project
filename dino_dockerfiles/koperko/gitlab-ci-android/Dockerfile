FROM ubuntu:16.04
MAINTAINER koperko

ENV VERSION_BUILD_TOOLS "28.0.3"
ENV VERSION_TARGET_SDK "28"

ENV ANDROID_HOME "/sdk"
RUN echo "export ANDROID_HOME=/sdk" >> /etc/profile
ENV PATH "$PATH:${ANDROID_HOME}/tools"
ENV DEBIAN_FRONTEND noninteractive

RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive
RUN  dpkg-divert --local --rename --add /sbin/initctl
#RUN  ln -s /bin/true /sbin/initctl

# Use local cached debs from host (saves your bandwidth!)
# Change ip below to that of your apt-cacher-ng host
# Or comment this line out if you do not wish to use caching
#ADD 71-apt-cacher-ng /etc/apt/apt.conf.d/71-apt-cacher-ng

RUN echo "deb http://archive.ubuntu.com/ubuntu trusty main universe" >> /etc/apt/sources.list
RUN apt-get -y update
# socat can be used to proxy an external port and make it look like it is local
RUN apt-get -y install ca-certificates socat openssh-server supervisor rpl pwgen
RUN mkdir /var/run/sshd
ADD sshd.conf /etc/supervisor/conf.d/sshd.conf

# Ubuntu 14.04 by default only allows non pwd based root login
# We disable that but also create an .ssh dir so you can copy
# up your key. NOTE: This is not a particularly robust setup 
# security wise and we recommend to NOT expose ssh as a public
# service.
#RUN rpl "PermitRootLogin without-password" "PermitRootLogin yes" /etc/ssh/sshd_config
RUN mkdir /root/.ssh
RUN chmod o-rwx /root/.ssh

#######

RUN apt-get -qq update && \
    apt-get install -qqy --no-install-recommends \
      curl \
      html2text \
      openjdk-8-jdk \
      libc6-i386 \
      lib32stdc++6 \
      lib32gcc1 \
      lib32ncurses5 \
      lib32z1 \
      unzip \
      git \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN rm -f /etc/ssl/certs/java/cacerts; \
    /var/lib/dpkg/info/ca-certificates-java.postinst configure

ADD https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip /tools.zip
RUN unzip /tools.zip -d /sdk && \
    rm -v /tools.zip

RUN echo y | /sdk/tools/bin/sdkmanager "platforms;android-28"
RUN echo y | /sdk/tools/bin/sdkmanager "platform-tools"
RUN echo y | /sdk/tools/bin/sdkmanager "build-tools;28.0.3"
RUN echo y | /sdk/tools/bin/sdkmanager "extras;android;m2repository"
RUN echo y | /sdk/tools/bin/sdkmanager "extras;google;m2repository"
RUN echo y | /sdk/tools/bin/sdkmanager "extras;google;google_play_services"

# Open port 22 so linked containers can see it
EXPOSE 22

ADD android-sdk-license /sdk/licenses/android-sdk-license

CMD service ssh start
