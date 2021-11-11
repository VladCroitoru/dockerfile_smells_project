FROM python:3.9
EXPOSE 8501

COPY sandmark-nightly-client-crontab /etc/cron.d/sandmark-nightly-client-crontab
RUN apt-get update && apt-get -y install sudo git wget cron vim && \
    pip install --no-cache-dir streamlit nested_dict seaborn multipledispatch 
RUN chmod 0644 /etc/cron.d/sandmark-nightly-client-crontab && \
    crontab /etc/cron.d/sandmark-nightly-client-crontab
RUN git clone https://github.com/ocaml-bench/sandmark-nightly.git
WORKDIR /sandmark-nightly/

CMD streamlit run app/app.py
