FROM ubuntu
RUN apt-get update
RUN apt-get install -y git-core
RUN git clone https://github.com/rembo10/headphones
RUN apt-get install -y --reinstall python2.7
ENTRYPOINT cd headphones && python Headphones.py
# Now running at http://localhost:8181
