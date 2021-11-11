FROM python/latest

WORKDIR .
RUN apt-get install sudo neofetch -y
RUN pip install -r -U requirements.txt
CMD ["python3", "-m", "Wylie"]
