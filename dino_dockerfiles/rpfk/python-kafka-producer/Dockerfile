FROM python:2-onbuild

ENV ASSIGNMENT_URL https://raw.githubusercontent.com/rpfk/python-kafka-producer-assignment/master/assignment.json
ENV KAFKA_ADDRESS localhost:21

ADD Producer.py /
ADD Factory/ /Factory/
ADD run.py /

CMD python run.py --kafka-address=$KAFKA_ADDRESS --assignment-url=$ASSIGNMENT_URL