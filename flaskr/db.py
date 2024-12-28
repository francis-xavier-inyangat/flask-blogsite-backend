
from flask import current_app, g
import psycopg2
from psycopg2.extras import DictCursor



def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            current_app.config['DATABASE_URL'],
            cursor_factory=DictCursor
        )
        
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# initialize the database
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        sql_script = f.read().decode('utf-8')
        cur = db.cursor()
        # Split the SQL script and execute non-empty, non-whitespace statements
        for statement in sql_script.split(';'):
            if statement.strip():  # Skip empty or whitespace-only statements
                cur.execute(statement.strip())
        db.commit()
        cur.close()



# register the app
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

import click

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')
