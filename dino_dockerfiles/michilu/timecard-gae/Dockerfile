FROM michilu/gae-tap

RUN mkdir /timecard-gae

WORKDIR /tmp
COPY packages.txt /tmp/packages.txt
RUN \
  pip install --quiet -r packages.txt &&\
  rm -rf /tmp/*

WORKDIR /timecard-gae
ADD . /timecard-gae
