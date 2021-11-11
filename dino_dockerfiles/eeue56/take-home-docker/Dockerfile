FROM node:5.5.0

RUN npm install -g elm@0.16

ENV LC_ALL C.UTF-8

RUN git clone https://github.com/NoRedInk/take-home.git /src

COPY run_with_cred.sh /src/run.sh

WORKDIR /src
RUN export LANG=en_US.UTF-8
RUN npm install -y
RUN chmod +x run.sh
CMD bash run.sh

EXPOSE 8080
