FROM ubuntu:17.10
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y libdancer2-perl && \
    apt-get install -y nginx curl build-essential

RUN curl -L http://cpanmin.us | perl - App::cpanminus
#RUN cpanm Dancer2
RUN cpanm Games::Sudoku::Component::Controller

EXPOSE 3000
COPY . /sudoku

CMD plackup bin/app.psgi

