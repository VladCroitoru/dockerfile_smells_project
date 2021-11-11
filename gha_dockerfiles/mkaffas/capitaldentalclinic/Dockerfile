FROM odoo:14.0

USER root
RUN apt-get update && apt-get upgrade -y && apt-get install -y git
# Create other addons directory
RUN mkdir /mnt/extra-addons/3rd-party-addons \
    && chown odoo: /mnt/extra-addons/3rd-party-addons
# Setting SSH
RUN mkdir /root/.ssh/ \
    && touch /root/.ssh/known_hosts \
    && ssh-keyscan github.com >> /root/.ssh/known_hosts
ADD id_rsa /root/.ssh/id_rsa
RUN chmod 700 /root/.ssh/id_rsa \
    && chown -R root:root /root/.ssh
# Clone Enterprise Addons
RUN git clone -b '14.0' --single-branch --depth 1 \
    git@github.com:MuhamdAbdRhman/enterprise.git /mnt/enterprise-addons
# Install Requirements
ADD requirements.txt ./
RUN pip3 install -r requirements.txt

USER odoo
