FROM ubuntu:focal

MAINTAINER Sebastian Syska (syska.seb@gmail.com)

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update -y && apt install -y \
python3 \
python3-dev \
pip

COPY requirements.txt aimachine /aimachine/

RUN pip install -r aimachine/requirements.txt

CMD ["python3","-m","aimachine"]
