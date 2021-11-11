
FROM ubuntu

MAINTAINER Marcin Mazurek <marcin.mazurek@allegrogroup.com>

# Install necessary packages.
RUN apt-get update && \
    apt-get install -y python-pip sqlite git && \
    apt-get clean

RUN pip install flask flask-httpauth


EXPOSE 5000

RUN git clone https://github.com/mazek/LiveNewsBoard.git /root/lnb

WORKDIR /root/lnb

# Initialize sqlite db.
RUN /root/lnb/lwb_db.py

# Clean-up
RUN apt-get clean

EXPOSE 5000
CMD python /root/lnb/lwb.py

