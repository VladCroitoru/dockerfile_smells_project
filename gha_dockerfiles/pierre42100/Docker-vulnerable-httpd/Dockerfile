# This image of HTTPD has known vulnerabilities
FROM httpd:2.4.18

# This command is added to bypass root restriction
RUN chmod a+rwx -R /usr/local/apache2/logs/
