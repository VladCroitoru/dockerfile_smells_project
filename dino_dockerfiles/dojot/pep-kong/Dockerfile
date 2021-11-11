FROM kong:0.10
MAINTAINER Alexandre Vasconcellos, alexv@cpqd.com.br

RUN yum install -y unzip &&  luarocks install json4lua && \
    echo "export LUA_PATH='./?.lua;/usr/share/lua/5.1/?.lua;/usr/share/lua/5.1/?/init.lua;/usr/lib64/lua/5.1/?.lua;/usr/lib64/lua/5.1/?/init.lua;/usr/local/share/lua/5.1/?.lua'" >> ~/.bashrc

RUN mkdir -p /home/pepkong/src && cp /etc/kong/kong.conf.default /etc/kong/kong.conf

COPY pepkong-*.rockspec /home/pepkong/
COPY src/ /home/pepkong/src

RUN cd /home/pepkong && luarocks make

RUN echo "custom_plugins = pepkong" >> /etc/kong/kong.conf
