FROM ubuntu:14.04

RUN apt-get update && apt-get install clang wget xz-utils -y
RUN wget "https://github.com/cgcgbcbc/ceagle-absref-docker/releases/download/1.0/ceagle-absref-1.0.tar.gz"
RUN tar -xvzf ceagle-absref-1.0.tar.gz
ADD ./entrypoint.sh ./entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
