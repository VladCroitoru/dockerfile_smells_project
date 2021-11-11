FROM jpetazzo/dind
MAINTAINER emihat <hattori.emi@imsbio.co.jp>
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install git python build-essential && \
    apt-get clean
RUN git clone https://github.com/galaxyproject/galaxy/
RUN cd galaxy && \
    git checkout -b master origin/master
ADD ./files/galaxy.ini /galaxy/config/galaxy.ini
ADD ./files/tool_conf.xml /galaxy/config/tool_conf.xml
ADD ./files/run_first.sh /galaxy/run_first.sh
ADD ./files/welcome.html /galaxy/static/welcome.html
ADD ./files/myTools /galaxy/tools/myTools
ADD ./files/universe.sqlite /galaxy/database/universe.sqlite
ADD ./files/start.sh /start.sh
ADD ./files/scripts /scripts
RUN sh /galaxy/run_first.sh
RUN mkdir /data
EXPOSE 8082
CMD ["sh", "/start.sh"]
