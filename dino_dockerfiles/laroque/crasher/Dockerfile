ARG img_user=amd64
ARG img_repo=debian
ARG img_tag=9

FROM ${img_user}/${img_repo}:${img_tag}

RUN apt-get update && apt-get install -y build-essential gdb

COPY crasher.cc /usr/local/src/crasher.cc

RUN g++ -std=c++11 -lpthread -o /usr/local/bin/example_crasher /usr/local/src/crasher.cc
CMD ["gdb", "--return-child-result", "-ex", "run", "-ex", "bt", "-ex", "quit", "--batch", "--args", "/usr/local/bin/example_crasher", "13"]
