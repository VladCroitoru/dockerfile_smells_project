# ベースとなるイメージ
FROM jboss/wildfly:13.0.0.Final

# 環境変数
ENV JBOSS_HOME=/opt/jboss/wildfly

USER root
RUN rpm -ivh http://dev.mysql.com/get/mysql57-community-release-el7-7.noarch.rpm
RUN yum install -y net-tools mysql
# WildFly を設定する CLIスクリプトを配置
COPY assets/setup-wildfly.cli /tmp
# MySQL JConnector をダウンロード
ADD https://repo1.maven.org/maven2/mysql/mysql-connector-java/5.1.34/mysql-connector-java-5.1.34.jar /tmp
RUN chown jboss:jboss /tmp/setup-wildfly.cli /tmp/mysql-connector-java-5.1.34.jar


# ------------------------------
# WildFlyの設定
# ------------------------------
USER jboss
# CLI スクリプトを実行して、JConnector や コネクションプール の設定などをする
RUN /opt/jboss/wildfly/bin/jboss-cli.sh --file=/tmp/setup-wildfly.cli
# WildFly の管理ユーザを作成
RUN /opt/jboss/wildfly/bin/add-user.sh admin password --silent
RUN rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history

COPY assets/entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]
