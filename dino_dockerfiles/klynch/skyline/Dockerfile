FROM python:2.7.9
MAINTAINER Kevin Lynch <klynch@squarespace.com>

RUN apt-get update && \
    apt-get install gfortran \
                    libatlas-base-dev \
                    libblas-dev -yy && \
    apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#pip dependency resolution does not allow numpy and scipy to be installed in the requirements file (scipy depends on
#numpy in an odd way). Solution is to install these two explicitly
RUN pip install numpy==1.9.2 && \
    pip install scipy==0.15.1

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

COPY . /usr/src/app

ENTRYPOINT [ "python", "./skyline.py" ]
CMD [ "-h" ]
