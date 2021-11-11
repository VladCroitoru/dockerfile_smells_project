FROM jupyter/datascience-notebook:python-3.7.6
WORKDIR /home/jovyan/work
ADD ./requirements.txt /home/jovyan/work/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8888
EXPOSE 6006
ADD . /home/jovyan/work
