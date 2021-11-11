# this image contains files from https://github.com/venthur/python-ardrone

FROM python:2-alpine
MAINTAINER Michal Kvasnica <michal.kvasnica@gmail.com>

WORKDIR /root
COPY requirements.txt /root/
RUN pip install -r requirements.txt

COPY *.py /root/
ENTRYPOINT ["python", "wspydrone.py"]

# docker build -t kvasnica/wspydrone .
# docker push kvasnica/wspydrone

# IMPORTANT: need to expose host interfaces since docker needs to connect to the drone via wifi
# docker run -it --net=host kvasnica/wspydrone

