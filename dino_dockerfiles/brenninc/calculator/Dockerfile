FROM ubuntu:14.04
MAINTAINER Christian Brenninkmeijer <Christian.Brenninkmeijer@manchester.ac.uk>

LABEL "description"="An example docker app using python as a calculator"

#Install python via apt-get
RUN apt-get update && apt-get install -y python

#copy in the code
COPY calculator.py calculator.py

ENTRYPOINT ["python","calculator.py"]

CMD ["1","+","2","*","3"]


