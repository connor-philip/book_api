FROM python:3.5-slim
LABEL maintainer="connor.philip12@hotmail.com"

USER root

WORKDIR /app
ARG testServerIP

ENV testServerIP $testServerIP

COPY environment/setup_scripts/ /app/book_api/environment/setup_scripts
COPY environment/requirement_files/feature_test_requirements.txt /app/book_api/requirements.txt

RUN ["bash", "/app/book_api/environment/setup_scripts/pip_install_packages.sh"]


CMD ["behave", "--format", "progress", "book_api/tests/feature_tests/features"]
