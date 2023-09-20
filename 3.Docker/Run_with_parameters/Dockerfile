FROM debian:stretch-slim

ARG RUNNER_VERSION="2.308.0"

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
    && rm -rf /action-runner/externals 

COPY composefile/docker-compose.yml /docker-compose.yml

ENTRYPOINT sudo -u runner /action-runner/config.sh \
    --url ${URL_REPO} --token ${GITHUB_RUNNER_TOKEN} \
    --runnergroup ${R_GROUP} \
    --name ${R_NAME} \
    --labels ${R_LABELS} \
    --work ${WORK_DIR} \
    && sudo -u runner /action-runner/run.sh
