FROM phedoreanu/archlinux-oracle-jdk

MAINTAINER Adrian Fedoreanu <adrian.fedoreanu@gmail.com>

RUN curl -O http://downloads.typesafe.com/typesafe-activator/1.3.5/typesafe-activator-1.3.5.zip
RUN unzip -qq typesafe-activator-1.3.5 \ 
	&& rm typesafe-activator-1.3.5.zip 

ENV PATH $PATH:/activator-dist-1.3.5:/activator-dist-1.3.5/bin

EXPOSE 9000 8888
RUN mkdir -p /app
WORKDIR /app

CMD ["activator", "run"]
