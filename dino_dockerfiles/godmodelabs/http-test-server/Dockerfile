FROM ruby:slim
LABEL maintainer="IT-Operations <it-operations@boerse-go.de>"

RUN apt-get update -y && \
    apt-get install -y ruby-sinatra ruby-json && \
    apt-get clean && rm -r /var/lib/apt/lists/*

EXPOSE 4567
ADD . /

ENTRYPOINT ["rackup"]
CMD ["-o","0.0.0.0"]
