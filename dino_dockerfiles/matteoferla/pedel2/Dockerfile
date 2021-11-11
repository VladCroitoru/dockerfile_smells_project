FROM centos/python-36-centos7
WORKDIR /opt/app-root/src
COPY . /opt/app-root/src/
ENTRYPOINT ["container-entrypoint"]


EXPOSE  8080
USER 1001

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python", "app.py", "-p 8080"]