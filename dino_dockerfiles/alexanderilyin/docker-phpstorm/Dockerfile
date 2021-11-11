FROM java

MAINTAINER Alexander Ilyin <alexander@ilyin.eu>

ENV VERSION 2016.1
ENV CONFIG_DIR .PhpStorm2016.1
ENV INSTALL_DIR PhpStorm-145.258.2

VOLUME /root/${CONFIG_DIR}/config/eval
VOLUME /project

RUN cd /opt/ && curl --location --silent --show-error http://download.jetbrains.com/webide/PhpStorm-${VERSION}.tar.gz | tar xzv

WORKDIR /opt/${INSTALL_DIR}

ENTRYPOINT ["bin/inspect.sh"]

CMD ["/project", "/project/.idea/inspectionProfiles/Project_Default.xml", "/project/output", "-d", "/project", "-v2"]
