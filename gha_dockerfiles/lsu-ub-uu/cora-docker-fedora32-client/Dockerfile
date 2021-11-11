FROM fedora:33
# Set a useful default locale
RUN echo "export LANG=en_US.UTF-8" > /opt/export_LANG.sh
RUN echo "export LANGUAGE=en_US.UTF-8" >> /opt/export_LANG.sh
RUN echo "export LC_ALL=en_US.UTF-8" >> /opt/export_LANG.sh
ENV BASH_ENV=/opt/export_LANG.sh \
    ENV=/opt/export_LANG.sh \
    PROMPT_COMMAND="source /opt/export_LANG.sh"
    
RUN useradd -d "/home/client" -u 1000 -U -m -s /bin/bash client

RUN dnf clean all && \
  dnf install \
  glibc-langpack-en \
  google-noto-sans-runic* \
  google-noto-sans-math-fonts \
  google-noto-sans-arabic* \
  webkit2gtk3 \
  wget \
  telnet \
  nano \
  lsof \
  tar \
  less \
  htop \
  git \
  java-1.8.0-openjdk \
  -y && \
  dnf clean all
  
#  java-1.8.0-openjdk java-1.8.0-openjdk-devel \
#  java-1.8.0-openjdk-javadoc java-1.8.0-openjdk-javadoc-zip \
#  java-1.8.0-openjdk-src \
#RUN wget -O - https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/download/jdk8u192-b12/OpenJDK8U-jdk_x64_linux_hotspot_8u192b12.tar.gz | tar zxf - -C /home/client
#COPY files/fontconfig.properties /home/client/jdk8u192-b12/lib/

COPY files/fedora /home/client/

COPY files/entrypoint.sh /home/client/
RUN chmod a+x /home/client/entrypoint.sh

RUN touch /home/client/.gitconfig

RUN chown client:client /home/client -R

RUN mkdir /home/client/records
RUN chown client:client /home/client/records

USER client

CMD  /home/client/entrypoint.sh
