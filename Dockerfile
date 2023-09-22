FROM python:3.11
# 
WORKDIR /code


COPY ./requirements.prod.txt /code/requirements.txt

# Update the package list and install OpenJDK 8
COPY --from=openjdk:8-jre-slim /usr/local/openjdk-8 /usr/local/openjdk-8

# set java env variable
ENV JAVA_HOME /usr/local/openjdk-8
RUN update-alternatives --install /usr/bin/java java /usr/local/openjdk-8/bin/java 1


RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN python -m spacy download en_core_web_sm



COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--workers", "2", "--host", "0.0.0.0", "--port", "8000"]