FROM combro2k/debian-debootstrap:8

ENV FULL_NAME=fullname \
    EMAIL_ADDRESS=example@example.org \
    GPG_PASSWORD=example \
    INSTALL_LOG=/var/log/build.log

ADD resources/bin/ /usr/local/bin/

RUN /bin/bash -l -c 'bash /usr/local/bin/setup.sh build'

ADD resources/etc/ /etc/

RUN /bin/bash -l -c 'bash /usr/local/bin/setup.sh post_install' | tee -a ${INSTALL_LOG} > /dev/null 2>&1 || exit 1

EXPOSE 80

VOLUME /opt/aptly

CMD ["/usr/local/bin/run"]
