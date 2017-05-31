from flask import render_template, Blueprint, session, redirect, url_for, request
from sort_books import cur


rank_blueprint = Blueprint('rank_blueprint', __name__)


@rank_blueprint.route('/ranking')
def rank():

    cur.execute("""
    SELECT r.id_r, r.name 
    FROM librarians.borrows AS b, librarians.readers AS r 
    WHERE b.give_back='1' AND r.id_r=b.name_id;
    """)

    ranks = {}

    for i in cur.fetchall():
        if int(i[0]) in ranks:
            ranks[int(i[0])]['count'] += 1
        else:
            ranks[int(i[0])] = {}
            ranks[int(i[0])]['count'] = 1
            ranks[int(i[0])]['name'] = i[1].split(' ')[0]

    ranks = sorted(ranks.items(), key=lambda item: item[1]['count'], reverse=True)
    rank = []
    for r in range(10):
        try:
            rank.append(ranks[r])
        except IndexError:
            break

    return render_template('rank.html', ranks=rank)
