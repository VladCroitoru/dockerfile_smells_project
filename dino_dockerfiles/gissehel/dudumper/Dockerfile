FROM ubuntu as builder

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && \
    apt install -y g++ make git apt-transport-https curl perl
RUN apt install -y gnupg2
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - 
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt update && \
    apt install -y nodejs yarn
RUN npm install -g coffeescript pug-cli stylus uglify-es
RUN mkdir -p /work
COPY . /work
RUN cd /work/web && \
    make clean all
RUN cd /work/src && \
    make clean all && \
    echo "All is OK..."

FROM scratch
COPY --from=builder "/work/src/dudumper" /dudumper
ENTRYPOINT [ "/dudumper" ]



