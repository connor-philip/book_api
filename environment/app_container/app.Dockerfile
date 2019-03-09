FROM ubuntu:16.04
LABEL maintainer="connor.philip12@hotmail.com"

USER root

ARG databaseIP

COPY environment/setup_scripts/ /var/www/book_api/environment/setup_scripts
COPY setup.py /var/www/book_api/setup.py
COPY program /var/www/book_api/program
COPY environment/app_container/book_api.conf /etc/apache2/sites-available/

# Install all required packages from apt using the setup scripts
RUN ["bash", "/var/www/book_api/environment/setup_scripts/apt_install_apache.sh"]
RUN ["bash", "/var/www/book_api/environment/setup_scripts/apt_install_python3.sh"]
RUN ["bash", "/var/www/book_api/environment/setup_scripts/pip_install_packages.sh"]

# Env variables
ENV databaseIP $databaseIP
ENV book_api_logs "/var/log/book_api_logs/"

# Create log file and set perms
RUN mkdir /var/log/book_api_logs/
RUN usermod -a -G root www-data
RUN chmod 770 /var/log/book_api_logs/

# Disable default conf, and enable book_api conf
RUN a2dissite 000-default
RUN a2ensite book_api

EXPOSE 80

# Start the apache2 service
ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
