FROM python:3.5-slim
LABEL maintainer="connor.philip12@hotmail.com"

USER root

WORKDIR /app
ARG databaseIP

ENV databaseIP $databaseIP
ENV book_api_logs "/var/log/book_api_logs/"

COPY environment/setup_scripts/ /app/book_api/environment/setup_scripts
COPY setup.py /app/book_api/setup.py
COPY program /app/book_api/program

RUN ["bash", "/app/book_api/environment/setup_scripts/pip_install_packages.sh"]

CMD ["python3", "tests/unit_tests/run_unit_tests.py"]
