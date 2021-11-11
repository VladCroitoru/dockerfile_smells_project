FROM        insilicotox/lazar-dev
MAINTAINER  Denis Gebele <gebele@in-silico.ch>

USER        ist
WORKDIR     /home/ist

RUN         cd lazar && \
            git checkout "ORN"

RUN         cd lazar-gui && \
            git checkout "ORN"

RUN         git clone https://github.com/swagger-api/swagger-ui.git
COPY        index.html /home/ist/swagger-ui/dist/index.html

COPY        start.sh /home/ist/start.sh
COPY        test.sh /home/ist/test.sh
COPY        service-test.rb /home/ist/service-test.rb
WORKDIR     /home/ist
RUN         sudo chmod +x /home/ist/start.sh
RUN         sudo chmod +x /home/ist/test.sh
ENTRYPOINT  ["/home/ist/start.sh"]

