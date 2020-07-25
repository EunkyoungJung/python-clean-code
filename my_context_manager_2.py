def stop_database():
    run("systemctl stop postgresql.service")


def start_database():
    run("systemctl start postgresql.service")


def db_backup():
    run("pg_dump database")


class dbhandler_decorator(contextlib.ContextDecorato):
    def __enter__(self):
        stop_database()

    def __exit__(self, ext_type, ex_value, ex_traceback):
        start_database()


@dbhandler_decorator()
def offline_backup():
    run("pg_dump database")

