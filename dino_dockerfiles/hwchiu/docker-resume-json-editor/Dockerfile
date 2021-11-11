FROM node:0.10

RUN apt-get install -y git

WORKDIR /
RUN git clone https://github.com/hwchiu/resume-editor &&\
cd resume-editor &&\
npm install


WORKDIR /resume-editor
CMD python -m SimpleHTTPServer 8001
