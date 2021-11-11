FROM python:3.8
# Install third party requirements
COPY requirements.txt /home/requirements.txt
RUN pip install -r /home/requirements.txt


COPY setup_scripts/wait-for-it.sh /wait-for-it.sh


# Install the station package
COPY . /home
RUN pip install /home

CMD ["python", "/home/station/run_station.py"]


