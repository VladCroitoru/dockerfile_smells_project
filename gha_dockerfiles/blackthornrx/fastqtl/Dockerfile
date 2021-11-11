FROM 315553526860.dkr.ecr.us-east-1.amazonaws.com/fastqtl_base:1.0.2

RUN apt install pigz -y
RUN echo 'pigz --stdout -p2 -d $1' > /usr/bin/pcat
RUN chmod a+x /usr/bin/pcat

COPY . /fastqtl
COPY entrypoint.sh /

ENTRYPOINT ["bash", "-c", "/entrypoint.sh"]
