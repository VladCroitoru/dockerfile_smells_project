FROM urgemerge/chromium-pulseaudio@sha256:21d8120ff7857afb0c18d4abf098549de169782e652437441c3c7778a755e46f
RUN \
    adduser --disabled-password --gecos "" user && \
    apt-get clean all
USER user
WORKDIR /home/user
RUN \
    mkdir /home/user/data
ENTRYPOINT ["chromium", "--user-data-dir=/home/user/data"]
CMD []