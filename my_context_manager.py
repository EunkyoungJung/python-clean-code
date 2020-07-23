import contextlib


def stop_database():
    run("systemctl stop postgresql.service")


def start_database():
    run("systemctl start postgresql.service")


def db_backup():
    run("pg_dump database")


@contextlib.contextmanager
def db_handler():
    stop_database()
    yield
    start_database()


if __name__ == "__main__":
    with db_handler():
        db_backup()
