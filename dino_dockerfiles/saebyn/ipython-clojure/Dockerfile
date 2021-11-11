FROM java:7

RUN mkdir /d

WORKDIR /d

ENV P_HOME /d/program
ENV CLOJURE_VERSION 1.6.0

RUN apt-get update && apt-get install -y curl wget vim unzip cmake g++ gcc

RUN  mkdir /d/download && mkdir /d/build && mkdir $P_HOME && mkdir /d/notebook



#python
RUN apt-get install -y libbz2-dev libgdbm-dev liblzma-dev libreadline-dev libsqlite3-dev libssl-dev tcl-dev tk-dev dpkg-dev libzmq3-dev python-dev python-pip
RUN pip install ipython[notebook] 

#lein
ADD https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein /bin/lein
RUN chmod a+x /bin/lein
ENV LEIN_ROOT 1


#clojure
RUN cd download && wget http://repo1.maven.org/maven2/org/clojure/clojure/$CLOJURE_VERSION/clojure-$CLOJURE_VERSION.zip && unzip clojure-$CLOJURE_VERSION && mv clojure-$CLOJURE_VERSION $P_HOME
ENV CLOJURE_HOME $P_HOME/clojure-$CLOJURE_VERSION


ENV PATH $PATH:$CLOJURE_HOME/bin
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/lib

RUN ipython profile create clojure && \
    cd /root/.ipython/profile_clojure && \
    mv ipython_config.py ipython_config.py.bak && \
    rm static/custom/custom.js && \
    rm static/custom/custom.css
ADD add/kernel.json /root/.ipython/kernels/clojure/
ADD add/ipython_config.py /root/.ipython/profile_clojure/
ADD add/custom.js /root/.ipython/profile_clojure/static/custom/
ADD add/custom.css /root/.ipython/profile_clojure/static/custom/


EXPOSE 8888

ADD . /d/build/ipython_clojure
RUN cd /d/build/ipython_clojure && make

CMD ipython notebook --ip=0.0.0.0  --profile clojure --notebook-dir=/d/notebook

