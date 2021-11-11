FROM python:3.6.1
ADD requirements.txt /
ADD vmcontrol.py /
RUN pip install -r /requirements.txt
CMD ["/vmcontrol.py", "help"]

