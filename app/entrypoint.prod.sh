#! /bin/sh
if [ " $ DATABASE " = "postgres" ]
    then
        echo "En attente de postgres ..."
        while ! nc -z $ SQL_HOST $ SQL_PORT ; do
            sleep 0 .1
        done
    echo
    "PostgreSQL a démarré"
fi
exec
"$@"