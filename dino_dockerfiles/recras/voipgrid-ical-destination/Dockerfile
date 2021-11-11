FROM python:3-onbuild

RUN useradd --system flask

EXPOSE 5000

USER flask

CMD [ "python", "/usr/src/app/main.py" ]
