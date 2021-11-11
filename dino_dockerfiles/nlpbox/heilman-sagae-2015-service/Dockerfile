FROM nlpbox/heilman-sagae-2015:2018-10-27


RUN pip3 install hug==2.4.0 pexpect==4.5.0 pytest==3.5.1

WORKDIR /opt/hs2015_service
ADD hs2015_hug_api.py test_api.py /opt/hs2015_service/
EXPOSE 8080

ENTRYPOINT ["hug"]
CMD ["-f", "hs2015_hug_api.py"]
