# =============================================================================
# Based on naqoda/mysql
#
# MySQL client with additional configuration
# 
# =============================================================================
FROM mysql:latest

RUN { \
  echo '[mysqld]'; \
  echo 'sql_mode = NO_ENGINE_SUBSTITUTION'; \
  echo 'default-storage-engine = innodb'; \
  } > /etc/mysql/conf.d/custom.cnf

RUN { \
  echo '[mysqld]'; \
  echo 'character-set-server = utf8'; \
  echo 'collation-server = utf8_unicode_ci'; \
  echo '[client]'; \
  echo 'default-character-set=utf8'; \
  } > /etc/mysql/conf.d/charset.cnf

CMD ["mysqld"]