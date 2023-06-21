import os
from git import Repo

local_repo = os.path.join(os.getcwd(), 'github_repo')
destination = "main"

def get_status(repo, path):
    for item in repo.index.diff(None):
        print("[!] изменение в файле" + item.a_path)
    


def clone_repo():
    if os.path.exists(local_repo):
        print("[*] Локальный репозиторий найден, запущено обновление локального репозитория")
        repo = Repo(local_repo)
        origin = repo.remotes.origin
        origin.pull(destination)
        get_status(repo=repo,path=local_repo)
        print("[*] Локальный репозиторий обновлён")
    else:
        print("[*] Локальный репозиторий не найден, запуск клонирования")
        Repo.clone_from("git@github.com:NoFreaze/test.git", local_repo, 
                    branch=destination)
        print("[*] Локальный репозиторий склонирован")

def main():
    clone_repo()


if __name__ == "__main__":
    main()
