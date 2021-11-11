
FROM ubuntu:focal-20210921

MAINTAINER YasuhiroABE <yasu-abe@u-aizu.ac.jp>

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get upgrade -y \
	&& DEBIAN_FRONTEND=noninteractive apt-get install -y \
	file sdaps texlive-lang-cjk texlive-xetex

## ommitting the "--no-install-recommends" option.

COPY files /files
RUN cp /files/defs.py /usr/lib/python3/dist-packages/sdaps/defs.py
RUN cp /files/template.py /usr/lib/python3/dist-packages/sdaps/template.py
RUN cp /files/answers.py /usr/lib/python3/dist-packages/sdaps/report/answers.py
RUN cp /files/buddies.py /usr/lib/python3/dist-packages/sdaps/report/buddies.py
RUN cp /files/__init__.py /usr/lib/python3/dist-packages/sdaps/reporttex/__init__.py
RUN cp /files/sdapsreport.cls /usr/share/sdaps/tex/sdapsreport.cls
RUN cp /files/latex.py /usr/lib/python3/dist-packages/sdaps/utils/latex.py

WORKDIR /

ENV WORKING_DIR /proj
RUN mkdir $WORKING_DIR
VOLUME $WORKING_DIR

COPY run.sh /run.sh
RUN chmod a+rx /run.sh

RUN groupadd sdaps
RUN useradd -m -g sdaps sdaps
USER sdaps

ENTRYPOINT ["/run.sh"]
CMD ["--help"]
