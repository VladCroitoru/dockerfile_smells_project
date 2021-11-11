FROM nicholsn/niquery
MAINTAINER Nolan Nichols <orcid.org/0000-0003-1099-3328>
ENV UPDATED "Sun Aug 24 13:20:01 PDT 2014"

RUN pip install flower 

EXPOSE 5555
ADD run.sh run.sh
RUN chmod +x run.sh
CMD ./run.sh
