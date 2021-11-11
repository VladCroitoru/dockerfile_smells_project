FROM ubuntu
RUN apt-get install -y git-core
RUN git clone https://github.com/pillone/usntssearch.git
RUN apt-get install -y --reinstall python2.7
ENTRYPOINT cd usntssearch/NZBmegasearch && python mega2.py
# Now running at http://localhost:5000
