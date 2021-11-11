FROM python:2.7.12
RUN pip install Janome==0.2.8
RUN pip install summpy==0.2.1
RUN pip install pulp==1.6.1
CMD ["python", "-m", "summpy.server", "-h", "0.0.0.0", "-p", "8080"]
