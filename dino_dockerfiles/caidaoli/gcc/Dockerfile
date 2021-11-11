from gcc
MAINTAINER Li YaLei <caidaoli@gmail.com>
# 备份原源列表
# RUN mv /etc/apt/sources.list /etc/apt/sources.list.backup
# 替换阿里云源
#ADD ./sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y cmake zlib1g-dev  git-core  libssl-dev zsh libjsoncpp-dev libevent-dev vim wget curl  unixodbc-dev uuid-dev
RUN wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh || true
#RUN wget https://github.com/msgpack/msgpack-c/releases/download/cpp-2.0.0/msgpack-2.0.0.tar.gz && mkdir /msgpack && tar xzf msgpack-2.0.0.tar.gz -C /msgpack && cd /msgpack/msgpack-2.0.0 && cmake -DMSGPACK_CXX11=ON . && make install
ADD https://github.com/msgpack/msgpack-c/releases/download/cpp-2.0.0/msgpack-2.0.0.tar.gz /tmp
RUN cd /tmp && tar xzf msgpack-2.0.0.tar.gz  && cd /tmp/msgpack-2.0.0 && cmake -DMSGPACK_CXX11=ON . && make install && rm -rf /tmp

ADD ./zshrc /root/.zshrc

VOLUME ["/app"]
workdir "/app"
#ENTRYPOINT ["zsh"]
