# 開発環境用コマンド
ALL: run
build:
	docker build -t pyramid-todo-app .
run:
	docker run -it --rm -p 6543:6543 --name pyramid-todo-app pyramid-todo-app pserve development.ini --reload
shell:
	docker run -it --rm -p 6543:6543 --name pyramid-todo-app pyramid-todo-app pshell development.ini
