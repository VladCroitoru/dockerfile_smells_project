FROM ubuntu

RUN dpkg-divert --local --rename --add /sbin/initctl
RUN ln -s /bin/true /sbin/initctl

RUN apt-get install -y sudo curl

RUN curl http://apt.basho.com/gpg/basho.apt.key | sudo apt-key add -
RUN sudo bash -c "echo deb http://apt.basho.com precise main > /etc/apt/sources.list.d/basho.list"
RUN sudo apt-get update

RUN sudo apt-get install -y riak

RUN sed -i -e 's/127.0.0.1/0.0.0.0/' /etc/riak/app.config
RUN echo "ulimit -n 4096" >> /etc/default/riak

CMD riak start && tail -f /var/log/riak/console.log
