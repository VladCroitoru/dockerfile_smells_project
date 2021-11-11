FROM doncieux/sferes2:latest
RUN apt-get install -y libsdl-dev
RUN cd /git/ && git clone https://github.com/sferes2/fastsim.git && git clone https://github.com/sferes2/nn2.git && git clone https://github.com/doncieux/collectball.git
RUN cd /git/sferes2/modules && ln -s /git/fastsim && ln -s /git/nn2
RUN cd /git/sferes2/exp/ && ln -s /git/collectball
RUN cd /git/sferes2 && echo fastsim > modules.conf && echo nn2 >> modules.conf
RUN cd /git/sferes2/ && ./waf configure --tbb=/deps/tbb2017_20161128oss && ./waf build --exp=collectball
