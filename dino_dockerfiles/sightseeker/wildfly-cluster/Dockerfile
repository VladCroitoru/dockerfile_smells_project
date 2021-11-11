# ベースとなるイメージ
FROM jboss/wildfly:10.1.0.Final

# 環境変数
ENV JBOSS_HOME=/opt/jboss/wildfly

USER root
# WildFly を設定する CLIスクリプトを配置
COPY setup-wildfly.cli /tmp

# ------------------------------
# WildFlyの設定
# ------------------------------
USER jboss
# CLI スクリプトを実行して、JConnector や コネクションプール の設定などをする
RUN /opt/jboss/wildfly/bin/jboss-cli.sh --file=/tmp/setup-wildfly.cli
# WildFly の管理ユーザを作成
RUN /opt/jboss/wildfly/bin/add-user.sh admin password --silent
RUN rm -rf /opt/jboss/wildfly/standalone/configuration/standalone_xml_history

COPY entrypoint.sh /

ENTRYPOINT ["sh", "/entrypoint.sh"]
