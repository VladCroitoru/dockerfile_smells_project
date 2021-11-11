FROM fedora
RUN dnf -y install tree curl tar gzip
WORKDIR /work
RUN curl -LO https://github.com/mozilla/geckodriver/releases/download/v0.20.0/geckodriver-v0.20.0-linux64.tar.gz
RUN tar xvfz geckodriver-v0.20.0-linux64.tar.gz

FROM fedora
RUN dnf -y install python3-pip firefox && \
    dnf clean all && \
    rm -r -f /var/lib/yum
RUN pip3 install --upgrade pip
RUN pip3 install selenium
RUN pip3 install xlrd
COPY --from=0 /work/geckodriver /usr/local/bin/geckodriver
