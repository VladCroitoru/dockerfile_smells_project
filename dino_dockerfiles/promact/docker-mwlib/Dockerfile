FROM python:2.7.10
ENV DEBIAN_FRONTEND noninteractive
ENV HOME            /root
ENV LC_ALL          C.UTF-8
ENV LANG            en_US.UTF-8
ENV LANGUAGE        en_US.UTF-8
RUN apt-get update && apt-get install imagemagick libmagick++-dev libgraphicsmagick1-dev libjpeg-dev zlib1g-dev libfreetype6-dev libxft-dev libffi-dev gcc g++ make libz-dev libfreetype6-dev liblcms2-dev libxml2-dev libxslt-dev ocaml-nox \
 texlive-latex-recommended ploticus dvipng imagemagick pdftk python-dev python-virtualenv git-core python-imaging python-lxml -y

RUN pip install --trusted-host pypi.pediapress.com -i http://pypi.pediapress.com/simple/ mwlib && \
 pip install reportlab && \
 pip install --trusted-host pypi.pediapress.com -i http://pypi.pediapress.com/simple/ mwlib.rl

RUN pip install supervisor
ADD supervisord.conf /etc/
 
EXPOSE 8899

CMD ["/usr/local/bin/supervisord","-c","/etc/supervisord.conf","-n"]






