# Pull base image
FROM python:3.9

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /statistic

# Install pipenv and dependencies
RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install --system --deploy --ignore-pipfile

# Copy project
COPY . .

# Run project
COPY app/consumer.py /
#COPY event-loop-entrypoint.sh /event-loop-entrypoint.sh
COPY ./entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//g' /entrypoint.sh
RUN #chmod +x /event-loop-entrypoint.sh
RUN chmod +x /entrypoint.sh


CMD ["/bin/bash", "/entrypoint.sh", "fastapi"] && ["/bin/bash", "/entrypoint.sh", "consumer"]

#ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
#ENTRYPOINT ["/bin/bash", "/event-loop-entrypoint.sh"]