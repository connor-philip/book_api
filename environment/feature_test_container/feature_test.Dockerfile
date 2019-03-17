FROM ubuntu:16.04
LABEL maintainer="connor.philip12@hotmail.com"

USER root

WORKDIR /app
ARG testServerIP
ARG testDatabaseIP

ENV testServerIP $testServerIP
ENV testDatabaseIP $testDatabaseIP

COPY environment/setup_scripts/ /app/book_api/environment/setup_scripts
COPY environment/requirement_files/feature_test_requirements.txt /app/book_api/requirements.txt

RUN ["bash", "/app/book_api/environment/setup_scripts/apt_install_python3.sh"]
RUN ["bash", "/app/book_api/environment/setup_scripts/pip_install_packages.sh"]
RUN ["bash", "/app/book_api/environment/setup_scripts/apt_install_mongodb.sh"]


CMD ["behave", "--format", "progress", "book_api/tests/feature_tests/features"]
