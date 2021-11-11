FROM python:3.8

WORKDIR /app

RUN apt-get update -y
RUN apt-get install -y texlive-xetex texlive-fonts-recommended texlive-latex-recommended

RUN pip install jupyter nbconvert pyppeteer matplotlib numpy pandas


EXPOSE 8888

CMD [ "jupyter", "notebook", "--allow-root", "--port=8888", "--no-browser", "--ip=0.0.0.0"]

