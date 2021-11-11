FROM python:3.7

COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt
RUN pip install SQLAlchemy

RUN mkdir /project
COPY scripts/ /project/scripts/

RUN chmod u+x /project/scripts/init.sh
ENTRYPOINT ["/project/scripts/init.sh"]