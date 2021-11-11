
FROM nlpbox/rstviewer:2018-05-31-2

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip && \
    pip3 install hug sh pytest pexpect==4.6.0 pillow==5.1.0 imagehash==4.0

WORKDIR /opt/rstviewer_service
ADD rstviewer_hug_api.py /opt/rstviewer_service/
ADD tests/* /opt/rstviewer_service/tests/
EXPOSE 8000


ENTRYPOINT ["hug"]
CMD ["-f", "rstviewer_hug_api.py"]
