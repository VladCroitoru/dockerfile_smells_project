FROM ubuntu:latest

run apt-get update && apt-get -y upgrade && apt-get -y install git python python-pip sqlite3 wget curl
run mkdir -p /monique && cd /monique && \
    git clone https://github.com/monique-dashboards/monique-tables && \
    git clone https://github.com/monique-dashboards/monique-api && \
    git clone https://github.com/monique-dashboards/monique-web &&\
    pip install -r /monique/monique-api/requirements.txt && \
    pip install -r /monique/monique-web/requirements.txt
run pip install gunicorn

# seed the tables
run migrations_dir=$(python -c 'from os.path import dirname; from mqe import migrations; print(dirname(migrations.__file__))') && \
    cat "$migrations_dir"/*.sqlite3 | sqlite3 /var/lib/monique.db &&\
    echo "create table user(user_id, email, password, created, user_data, api_key);" | sqlite3 /var/lib/monique.db
    #wget https://raw.githubusercontent.com/monique-dashboards/monique/master/examples/createdashboard.py &&\
    #python createdashboard.py
expose 8100 8101
copy docker_start.sh /
cmd /docker_start.sh

