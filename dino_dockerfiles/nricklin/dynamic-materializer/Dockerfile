FROM nricklin/gdal2.3

RUN apt-get install -y python-pip unzip
RUN pip install -U pip
RUN pip install boto3
RUN pip install tiletanic
ADD dynamic.py /dynamic.py
ADD task.py /task.py

CMD python /task.py