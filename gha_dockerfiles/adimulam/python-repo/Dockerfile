#FROM python:3.8-slim-buster
FROM public.ecr.aws/blockbuster/python3.8:latest
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
