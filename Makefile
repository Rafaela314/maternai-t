ifneq (,$(wildcard .env.local))
include .env
export
endif

postgres:
	docker run --name postgres_birth --network bank-network -p 5432:5432 -e POSTGRES_USER=$${POSTGRES_USER} -e POSTGRES_PASSWORD=$${POSTGRES_PASSWORD} -d postgres

createdb:
	docker exec -it postgres_birth createdb --username=$${POSTGRES_USER} --owner=$${POSTGRES_USER} $${POSTGRES_DB}

dropdb:
	docker exec -it postgres_birth dropdb $${POSTGRES_DB}

.PHONY: postgres createdb dropdb 