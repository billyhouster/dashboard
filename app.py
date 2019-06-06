
import os

import flask

import blueprints.docker
import blueprints.jenkins
import blueprints.gitlab
import blueprints.sign_in

app = flask.Flask(__name__)

app.register_blueprint(blueprints.docker.blueprint)
app.register_blueprint(blueprints.jenkins.blueprint)
app.register_blueprint(blueprints.gitlab.blueprint)
app.register_blueprint(blueprints.sign_in.blueprint)

@app.route('/', methods=[ 'GET' ])
def index():
    return flask.redirect('/docker')
    
if __name__ == '__main__':

    os.environ['FLASK_APP'] = 'app.py'
    os.environ['FLASK_ENV'] = 'development'

    app.run(host='0.0.0.0')

    