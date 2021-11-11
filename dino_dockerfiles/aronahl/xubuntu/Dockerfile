FROM ubuntu:16.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get dist-upgrade -y  && \
    apt-get install -y curl software-properties-common  && \
    curl http://winswitch.org/gpg.asc | apt-key add - && \
    echo "deb http://winswitch.org/ xenial main" > /etc/apt/sources.list.d/winswitch.list && \
    add-apt-repository universe  && \
    apt-get update && \
    apt-get install -y xpra xubuntu-desktop chromium-browser xnest && \
    mv /usr/bin/chromium-browser /usr/bin/chromium-browser.real && \
    adduser user < /dev/null && \
    apt-get autoclean -y && \
    apt-get clean -y && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/* 
ADD chromium-browser /usr/bin/
ADD start.sh /usr/local/bin/
ADD xubuntu-sudoers /etc/sudoers.d/
USER user
ENTRYPOINT [ "/usr/local/bin/start.sh" ]
CMD [ ]
