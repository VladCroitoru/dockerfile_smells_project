FROM mattmcd/pcr 

MAINTAINER Matt McDonnell "matt@matt-mcdonnell.com"

ENV HOME /home/ubuntu

ENV MDA_DATA_DIR /home/ubuntu/Work/Data

RUN mkdir -p /home/ubuntu/Work

WORKDIR /home/ubuntu/Work

COPY . /home/ubuntu/Work/PyAnalysis

COPY data/FTSE100.csv /home/ubuntu/Work/Data/FTSE100/FTSE100.csv

CMD ["python", "/home/ubuntu/Work/PyAnalysis/download_intraday.py", "--do-copy"]

