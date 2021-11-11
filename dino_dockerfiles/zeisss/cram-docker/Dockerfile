FROM python:2.7.18

ENV HOME /root
WORKDIR /root
ADD https://bitheap.org/cram/cram-0.6.tar.gz /root/cram-0.6.tar.gz
RUN tar xfz /root/cram-0.6.tar.gz
 
ENTRYPOINT ["/root/cram-0.6/cram.py"]
CMD []
