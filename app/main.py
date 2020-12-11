from flask import Flask, request, abort, render_template
from flaskext.mysql import MySQL
import logging

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'bai3ohdohT'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'
app.config['MYSQL_DATABASE_DB'] = 'test'
mysql.init_app(app)

logger = logging.getLogger('requestInfo')
handler = logging.FileHandler('/logs/access.log')
formatter = logging.Formatter('%(asctime)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

SIMPLEDEPS = {
    'l1ct6xp6tpft': 'gh4gg34',
    'eihoS4zee5Ii': 'ae9ieC',
    'jie8Yeaesi9X': 'Po3oom',
    'Yai0auEikei0': 'Me1ii7',
    'aeP2jeaiH7io': 'ieW5ie',
    'aet0MuMooS8u': 'veiw4I',
    'iuT6eiEek0Mu': 'eeNgi6',
    'gf32d2vcj442': 'lkvo24',
    'n3m1k2zgjj56': ['lk90pj', 'control', 'asde11'],
    'p0065nzbtghr': 'hg3f2d',
    'kl3j5h32nhj4': ['qh44j3', 'surveiller', 'po89uo'],
    'thq019nhqmz8': 'nba67x',
    'lm3b22b1nqjc': 'a09bku',
    'nh3k21hd73h4': 'phgoo9',
    'hgt54rt3qrv5': 'i67u77',
    'lfi32bbjfu93': ['qng1f3', 'windowpane', '35129'],
    'j4b2yh9fdh32': 'ffdj3v',
    'Che7eiUa9xek': 'abi1Lu',
    'to0HeimaM2uc': 'Pue6Ee',
}

METHODS = {
    'eeNgi6': 'POST',
    'ffdj3v': 'POST'
}

@app.before_request
def log_info():
    path = request.full_path if request.query_string else request.path
    if (request.content_length or 0) <= 16 * 1024 * 1024:
        data = str(request.get_data()).lstrip('b')
    else:
        data = "Very big body"
    logger.debug(
        '%s %s %s %s', request.remote_addr, request.method, repr(path), data
    )


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/application/<firstpart>/interface/<secondpart>/handle', methods=["GET", "POST"])
def handler(firstpart, secondpart):
    dep_id = firstpart + secondpart
    if dep_id in SIMPLEDEPS:
        if isinstance(SIMPLEDEPS[dep_id], list):
            param_name, check_param, check_val = SIMPLEDEPS[dep_id]
            if request.args.get(check_param) != check_val:
                abort(404)
            else:
                param = request.args.get(param_name)
                return db_request(param)
        method = METHODS.get(SIMPLEDEPS[dep_id], "GET")
        if method != request.method:
            abort(404)
        if method == "POST":
            param = request.form.get(SIMPLEDEPS[dep_id])
        else:
            param = request.args.get(SIMPLEDEPS[dep_id])
        return db_request(param)
    else:
        abort(404)

@app.route('/application/givemescript', methods=["POST"])
def script_sender():
    return app.send_static_file('dynamically-loaded-script.html')

@app.route('/Che7ei/request')
def request16():
    return render_template('request16.html')

@app.route('/new_feature')
def request17():
    return render_template('request17.html')

def db_request(param):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, name FROM testusers WHERE id='%s'" % param)
    except cursor.Error as e:
        conn.close()
        return str(e)
    conn.close()
    return str(cursor.fetchall())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
