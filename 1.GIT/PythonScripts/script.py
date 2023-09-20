#!/usr/bin/python3
import os
from argparse import ArgumentParser, Namespace
from git import Repo
import git

local_repo_directory = os.getcwd()
destination = "main"

def clone_repo(ssh_string, folder):
    if folder != None:
        local_repo_directory = os.path.join(os.getcwd(), folder)
    
    print("[-] Рабочий репозиторий " + local_repo_directory)

    if os.path.exists(local_repo_directory):
        repo = Repo(local_repo_directory)
        print("[*] Локальный репозиторий найден, запущено обновление локального репозитория.")
        repo = git.Repo(local_repo_directory)
        origin = repo.remotes.origin
        origin.pull(destination)
        #get_status(repo=repo,path=local_repo_directory)
        print("[*] Локальный репозиторий обновлён.")
    else:
        print("[*] Локальный репозиторий не найден, запуск клонирования.")
        Repo.clone_from(ssh_string, local_repo_directory, branch=destination)
        print("[*] Локальный репозиторий склонирован.")

def create_branch(branch_name, folder):
    if folder != None:
        local_repo_directory = os.path.join(os.getcwd(), folder)
    
    print("[-] Рабочий репозиторий " + local_repo_directory)

    repo = Repo(local_repo_directory)
    branch = repo.create_head(branch_name)
    branch.checkout()
    print("[*] Создана ветка " + branch_name + ".")
    print("[*] Осуществлен переход на новую ветку.")

def add_and_commit_canges(message, folder):
    if folder != None:
        local_repo_directory = os.path.join(os.getcwd(), folder)
    
    print("[-] Рабочий репозиторий " + local_repo_directory)
    repo = Repo(local_repo_directory)
    repo.git.add(".")
    print("[+]Файлы добавлены в index")
    repo.git.commit("-m", message)
    print("[*]Коммит создан")

def push_changes(branch_name, folder):
    if folder != None:
        local_repo_directory = os.path.join(os.getcwd(), folder)
    
    print("[-] Рабочий репозиторий " + local_repo_directory)
    repo = Repo(local_repo_directory)
    repo.git.push("--set-upstream", 'origin', branch_name)

def main():
    parser = ArgumentParser(description="Выберите 1 из параметров (-u, -c, -a, -p) для взаимодействия с репозиторием.\r\n Параметры -O и -L являются опциональными и могут быть использованы одновременно.")
    parser.add_argument("-u", "--update", help="Загрузка/обновление репозитория", action="store_true")
    parser.add_argument("-c", "--create_branch", help="Создание ветки и переключение на неё", action="store_true")
    parser.add_argument("-a", "--add_and_commit", help="Добавление файлов в index и созадние коммита", action="store_true")
    parser.add_argument("-p", "--push", help="Отправка изменений на удалённый сервер", action="store_true")
    parser.add_argument("-O", "--origin", default="git@github.com:NoFreaze/test.git", help="Ссылка на репозиторий с доступом по SSH")
    parser.add_argument("-F", "--folder", default=None, help="Папка локального репозитория. По умолчанию репозиторий = текущий каталог")
    args: Namespace = parser.parse_args()
    
    if args.update:
        ssh_string = args.origin
        print(ssh_string)   
        clone_repo(args.origin, args.folder)
    elif args.create_branch:
        print("Введите название новой ветки:")
        name_branch = input()
        create_branch(name_branch, args.folder)
    elif args.push:
        print("Введите название ветки:")
        name_branch = input()
        push_changes(name_branch, args.folder)
    elif args.add_and_commit:
        print("Введите текст коммита:")
        message = input()
        add_and_commit_canges(message, args.folder)

if __name__ == "__main__":
    main()
