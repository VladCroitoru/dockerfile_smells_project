FROM opencpu/ubuntu-20.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y texlive-full latexmk evince aspell aspell-en && \
  apt-get clean

# Change environment to Japanese(Character and DateTime)
ENV LANG ja_JP.UTF-8
ENV LC_ALL ja_JP.UTF-8
RUN sed -i '$d' /etc/locale.gen \
  && echo "ja_JP.UTF-8 UTF-8" >> /etc/locale.gen \
	&& locale-gen ja_JP.UTF-8 \
	&& /usr/sbin/update-locale LANG=ja_JP.UTF-8 LANGUAGE="ja_JP:ja"
RUN /bin/bash -c "source /etc/default/locale"
RUN ln -sf  /usr/share/zoneinfo/Asia/Tokyo /etc/localtime


USER root
# Start non-daemonized webserver
CMD /usr/lib/rstudio-server/bin/rserver && apachectl -DFOREGROUND
