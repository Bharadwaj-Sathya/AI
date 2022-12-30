def select(cursor, age, city, order):
    if age is not None:
        cursor.execute(f"SELECT name FROM people WHERE age={age} ORDER BY id {order}")
        rows = list(cursor.fetchall())
        result = [row[0] for row in rows]
        return result
    elif city is not None:
        cursor.execute(f"SELECT name FROM people WHERE city={city} ORDER BY id {order}")
        rows = list(cursor.fetchall())
        result = [row[0] for row in rows]
        return result



def select(cursor, age, city, order):
    if age is not None:
        cursor.execute("SELECT name FROM people WHERE age='%s' ORDER BY id '%s'", (age, order))
        rows = list(cursor.fetchall())
        result = list(itertools.chain(*rows))
        return result
    elif city is not None:
        cursor.execute("SELECT name FROM people WHERE city='%s' ORDER BY id '%s'", (city, order))
        rows = list(cursor.fetchall())
        result = list(itertools.chain(*rows))
        return result


def select(cursor, age, city, order):
    if age is not None:
        cursor.execute("SELECT name FROM people WHERE age=? ORDER BY id ?", (age, order))
        rows = list(cursor.fetchall())
        result = list(itertools.chain(*rows))
        return result
    elif city is not None:
        cursor.execute("SELECT name FROM people WHERE city=? ORDER BY id ?", (city, order))
        rows = list(cursor.fetchall())
        result = list(itertools.chain(*rows))
        return result