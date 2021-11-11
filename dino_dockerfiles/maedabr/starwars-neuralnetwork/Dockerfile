FROM maedabr/torch-rnn

RUN mkdir -p /code/data
WORKDIR /code/data
ADD *.sh ./
RUN bash ./download_binaries.sh
