# FROM goude/runcom-linux:v3.3.0
FROM goude/runcom-linux:latest
MAINTAINER Daniel Goude <daniel@goude.se>

USER runcom
WORKDIR /home/runcom

RUN \
  git clone https://github.com/goude/jupyter-virtualenv.git && \
  cd jupyter-virtualenv && \
  ./setup.sh && \
  ln -s start-jupyter.sh ~/start.sh && \
  echo "jupyter-virtualenv $(date --iso-8601=seconds)" >> /home/runcom/.runcom-log
