from tinydb import TinyDB, Query


def find_form(data: dict, db: TinyDB) -> str | dict:
    query = Query()
    for key in data.keys():
        print(db.search(query.contains(str(key))))
