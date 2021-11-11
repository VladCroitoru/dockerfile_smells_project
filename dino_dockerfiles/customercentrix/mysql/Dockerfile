FROM customercentrix/ubuntu

# MySQL 5.6

RUN  date -u +"%Y-%m-%d %H:%M:%S" && apt-get update \
  && date -u +"%Y-%m-%d %H:%M:%S" && DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-server-5.6 \
  && date -u +"%Y-%m-%d %H:%M:%S" && rm -rf /var/lib/apt/lists/* \
  && date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/^\(bind-address\s.*\)/#\1\nskip-name-resolve/' /etc/mysql/my.cnf \
  #&& date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/^\(bind-address\s\).*/\1 0\.0\.0\.0/' /etc/mysql/my.cnf \
  && date -u +"%Y-%m-%d %H:%M:%S" && sed -i 's/^\(log_error\s.*\)/# \1/' /etc/mysql/my.cnf \
  && date -u +"%Y-%m-%d %H:%M:%S" && echo "mysqld_safe &" > /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S" && echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S" && echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" WITH GRANT OPTION;'" >> /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S" && echo "mysql -e 'CREATE DATABASE ls_test_db;'" >> /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S" && echo "mysql -e 'GRANT ALL PRIVILEGES ON ls_test_db.* TO \"ls_test_user\"@\"%\" IDENTIFIED BY \"lspw\";'" >> /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S" && echo "mysql -e 'CREATE DATABASE ls_dev_db;'" >> /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S" && echo "mysql -e 'GRANT ALL PRIVILEGES ON ls_dev_db.* TO \"ls_dev_user\"@\"%\" IDENTIFIED BY \"lspw\";'" >> /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S" && echo "mysql -e 'CREATE DATABASE ls_jobs_db;'" >> /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S" && echo "mysql -e 'GRANT ALL PRIVILEGES ON ls_jobs_db.* TO \"ls_job_user\"@\"%\" IDENTIFIED BY \"lspw\";'" >> /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S" && echo "mysql -e 'CREATE DATABASE wb_dev_db;'" >> /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S" && echo "mysql -e 'GRANT ALL PRIVILEGES ON wb_dev_db.* TO \"wb_dev_user\"@\"%\" IDENTIFIED BY \"wbpw\";'" >> /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S" && bash /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S" && rm -f /tmp/config \
  && date -u +"%Y-%m-%d %H:%M:%S"

CMD ["mysqld_safe"]

EXPOSE 3306
