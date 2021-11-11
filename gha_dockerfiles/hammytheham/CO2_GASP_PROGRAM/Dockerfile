FROM public.ecr.aws/lts/ubuntu:latest
RUN echo Updating existing packages, installing and upgrading python and pip.
RUN apt-get update -y
FROM osgeo/gdal:ubuntu-small-latest
FROM continuumio/miniconda3
WORKDIR /app
# Create the environment:
COPY environment.yml .
RUN conda env create -f environment.yml
# Make RUN commands use the new environment:
RUN echo "conda activate myenv" >> ~/.bashrc
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# Demonstrate the environment is activated:
RUN echo "Make sure flask is installed:"
RUN python -c "import flask"

RUN echo Copy service directory

COPY ./service /co2gaspService
#RUN ls
#COPY /co2gaspService/server.py ./
#COPY /co2gaspService/entrypoint.sh ./

WORKDIR /co2gaspService

#RUN ["chmod", "+x","./entrypoint.sh"]
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "myenv", "python","server.py"]
