FROM rubicks/dev
MAINTAINER rubicks

RUN useradd luser
WORKDIR /home/luser
ADD . /home/luser
CMD /bin/bash ./build-o-matic.sh
