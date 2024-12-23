from flask import (Blueprint, flash, g, redirect, request, url_for, render_template)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)



@bp.route('/create', methods=('GET','POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        author_id = g.user['id']
        error = None

        if not title:
            error = 'Title is Required'
        elif not body:
            error = 'Content is Required'
        elif error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                'VALUES (?,?,?)',
                (title,body,author_id)
            )
            db.commit()
            return redirect(url_for('blog.index'))
    return render_template('blog/create.html')


# both delete and update will fetch a post, and compare user id with logged_in user.
# lets write a function to just fetch a post with id, to avoid duplicating code for delete and update


def get_post(id, check_author=True):
    post = get_db().execute(
         'SELECT p.id, title, body, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post Id {id} doesn't exist")

    if  check_author and post['author_id'] != g.user['id']:
         abort(403)
    return post



@bp.route('/<int:id>/update', methods = ('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)
    
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None
        
        if not title:
            error = 'Title is Required.'


        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ?'
                ' WHERE id = ?',
                (title, body, id)
            )

            db.commit()
        return redirect(url_for('blog.index'))
    
    # errors, stay on same page
    return  render_template('blog/update.html', post=post)


# delete api

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))

    




    