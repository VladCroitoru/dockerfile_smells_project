FROM fnndsc/ubuntu-python3
MAINTAINER fnndsc "dev@babymri.org"

RUN apt-get update \
  && apt-get install -y xinetd \
  && apt-get install -y dcmtk \
  && pip install pypx==0.9

EXPOSE 10402
COPY ./docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
#CMD ["service", "xinetd", "start"]
CMD ["/usr/sbin/xinetd", "-dontfork"]
