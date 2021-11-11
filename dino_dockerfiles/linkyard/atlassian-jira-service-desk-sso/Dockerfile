FROM cptactionhank/atlassian-jira-service-desk:3.3.1
MAINTAINER Mario Siegenthaler <mario.siegenthaler@linkyard.ch>

# Enable SSO for Service Desk Users
# see https://resolution.atlassian.net/wiki/display/SSSO/Single+Sign+on+for+JIRA+Service+Desk
USER root:root
COPY samlsso-authenticator-1.1.1.jar /opt/atlassian/jira/atlassian-jira/WEB-INF/lib/
RUN sed -i 's/com.atlassian.jira.security.login.JiraSeraphAuthenticator/com.resolution.samlsso.authenticator.JiraSsoAuthenticator/' \
        /opt/atlassian/jira/atlassian-jira/WEB-INF/classes/seraph-config.xml
USER daemon:daemon
