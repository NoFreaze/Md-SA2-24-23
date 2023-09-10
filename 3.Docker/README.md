Сборка с параметрами. По умолчанию значение каждого параметра указано в Dockerfile и они не являются обязательными при запуске.

Пример docker build -t imagename . --build-arg token=runner-token 
                                     --build-arg name=name
                                     --build-arg labels=label1,label2
                                     --build-arg dir=work-dir
                                     --build-arg url=url-repo


Запуск образа.
docker run -d -v /var/run/docker.sock:/var/run/docker.sock imagename

В файле githubaction.yml описан сценарий запуска задачи на бегунах. 
Если необходимо чтобы контейнеры, запущенные через бегуна умирали вместе с бегуном, то нужно убрать параметр -d
_______________________________________________________________________________________________________________

Запуск с параметрами
docker run -d --env-file env -v /var/run/docker.sock:/var/run/docker.sock imagename

