FROM debian:stretch-slim

ARG RUNNER_VERSION="2.308.0"
ARG token="AO5GQ76BWFGDUGIW4MM4EDTE7SYEQ"
ARG labels="Linux"
ARG dir="_work"
ARG name="Runner"
ARG url="https://github.com/NoFreaze/Md-SA2-24-23"

ENV GITHUB_RUNNER_TOKEN=${token}
ENV URL_REPO=${url}
ENV R_NAME=${name}
ENV R_LABELS=${labels}
ENV WORK_DIR=${dir}

RUN set -e \
    && echo "deb http://archive.debian.org/debian stretch main contrib non-free" > /etc/apt/sources.list \
    && apt update \
    && apt install wget tar sudo -y \
    && wget https://github.com/docker/compose/releases/download/1.24.0/docker-compose-Linux-x86_64 \
    && mv docker-compose-Linux-x86_64 docker-compose \
    && sudo mv docker-compose /usr/local/bin/ \
    && sudo chmod +x /usr/local/bin/docker-compose \
    && mkdir action-runner && cd action-runner \
    && wget https://github.com/actions/runner/releases/download/v2.308.0/actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz \
    && tar xzf ./actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz \
    && rm -rf ./actions-runner-linux-x64-${RUNNER_VERSION}.tar.gz \
    && useradd runner -G sudo \
    && touch /etc/sudoers.d/runner \
    && echo "runner  ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/runner \
    && chmod 777 /action-runner/ \
    && ./bin/installdependencies.sh \
    && apt remove wget -y \
    && apt clean && apt autoremove -y \
    && rm -rf /var/cache/apt \
    && rm -rf /root/.cache \
    && rm -rf /action-runner/externals \
    && sudo -u runner /action-runner/config.sh --url ${URL_REPO} --token ${GITHUB_RUNNER_TOKEN} \
    --name ${R_NAME} --labels ${R_LABELS} --work ${WORK_DIR}

COPY docker-compose.yml /docker-compose.yml

ENTRYPOINT sudo -u runner /action-runner/run.sh 
    
