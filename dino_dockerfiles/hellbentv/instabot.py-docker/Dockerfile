FROM bitnami/minideb
RUN apt-get update && apt-get -y install vim git python-pip
RUN git clone https://github.com/LevPasha/instabot.py \
  && cd instabot.py \
  && pip install requests
ADD clean.patch /instabot.py/
RUN cd /instabot.py\
  && git apply clean.patch
CMD python /instabot.py/example.py
