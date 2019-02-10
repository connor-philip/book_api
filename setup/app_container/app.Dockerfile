FROM ubuntu:16.04
LABEL maintainer="connor.philip12@hotmail.com"

USER root
ARG databaseIP

COPY setup/setup_scripts/ /var/setup/setup_scripts
COPY program /var/www/book_api
COPY setup/app_container/book_api.conf /etc/apache2/sites-available/

# Install all required packages from apt using the setup scripts
RUN ["bash", "/var/setup/setup_scripts/apt_install_apache.sh"]
RUN ["bash", "/var/setup/setup_scripts/apt_install_python3.sh"]
RUN ["bash", "/var/setup/setup_scripts/pip_install_packages.sh"]

# Env variables
ENV databaseIP $databaseIP

# Disable default conf, and enable book_api conf
RUN a2dissite 000-default
RUN a2ensite book_api

# Start the apache2 service
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
