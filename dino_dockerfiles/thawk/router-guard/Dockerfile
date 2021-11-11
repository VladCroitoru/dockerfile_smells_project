FROM python:3

WORKDIR /app

ADD . .
RUN pip install --trusted-host pypi.python.org -r requirements.txt

VOLUME [ "/cfg" ]

ENTRYPOINT [ "python", "router_guard.py", "-c", "/cfg/config.yaml", "guard" ]

