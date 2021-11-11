FROM ruby
MAINTAINER Emre Demirors <emre.x.demirors@gmail.com>

RUN gem install wmls -v 0.1.15
RUN git clone https://github.com/wellstorm/wmls.git /root/wmls

WORKDIR /root/wmls

COPY run.sh /root/run.sh

ENTRYPOINT ["/root/run.sh"]
CMD ["query_v14/get_all_wells.xml", "-a", "get"]
