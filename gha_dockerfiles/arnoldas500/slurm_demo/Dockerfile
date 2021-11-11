FROM tensorflow/tensorflow:latest-gpu
#copy python reqs and install
RUN apt-get update && apt-get install -y
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
#should also copy any code you will need to run project ex:
COPY . /raid/jpan/slurm_project
WORKDIR /raid/jpan/slurm_project
CMD python /raid/jpan/slurm_project/app.py
