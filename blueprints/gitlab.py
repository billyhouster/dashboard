import flask
import requests

ACCESS_TOKEN = 'ZJq5CCjhSzZV4e3Hbj8d'

PROJECTS_URL = 'https://gitlab.com/api/v4/projects?owned=true&private_token={}'.format(ACCESS_TOKEN)
PROJECT_COMMITS = 'https://gitlab.com/api/v4/projects/12680270/repository/commits?private_token={}'.format(ACCESS_TOKEN)

CREATE_PROJECT_URL = 'https://gitlab.com/api/v4/projects/user/4906833?name=rest-project&private_token={}'.format(ACCESS_TOKEN)

blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET' ])
def get_gitlab():

    r = requests.post(CREATE_PROJECT_URL)
    print(r.json())

    context = {
        'page': 'gitlab',
        'projects': requests.get(PROJECTS_URL).json(),
        'commits': requests.get(PROJECT_COMMITS).json(),
    }

    return flask.render_template('gitlab.html', context=context)

@blueprint.route('/gitlab/<int:projectid>', methods=[ 'GET' ])
def get_project_commits(projectid):

    PROJECT_COMMITS = 'https://gitlab.com/api/v4/projects/' + str(projectid) + '/repository/commits?private_token={}'.format(ACCESS_TOKEN)
    
    context = {
        'page': 'gitlab',
        'projects': requests.get(PROJECTS_URL).json(),
        'commits': requests.get(PROJECT_COMMITS).json(),
    }

    return flask.render_template('gitlab_commit.html', context=context)
