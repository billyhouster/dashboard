
import flask
import ldap3

blueprint = flask.Blueprint('sign_in', __name__)

@blueprint.route('/sign-in', methods=[ 'GET' ])
def get_sign_in():

    context = {
        'page': 'sign-in',
        'route': {
            'isPublic': True
        }
    }

    return flask.render_template('sign-in.html', context=context)

@blueprint.route('/sign-in', methods=[ 'POST' ])
def post_sign_in():

    server =ldap3.Server('ldap://127.0.0.1:389')
    connection = ldap3.Connection(
        server,
        'cn=admin,dc=dexter,dc=com,dc=br',
        '4linux'
    )
    try:
        connection.bind()
    except:
        return flask.redirect('/sign-in')
    print('DSDSDSDSDSDS')
    email = flask.request.form['email']
    password = flask.request.form['password']

    connection.search(
        'uid={},dc=dexter,dc=com,dc=br'.format(email),
        '(objectClass=person)',
        attributes=[ 'userPassword' ]
    )
    try:
        response = connection.entries[0]
        saved_password = response.userPassword.value.decode()
        if password != saved_password:
            return flask.redirect('/sign-in')
    except:
        return flask.redirect('/sign-in')

    return flask.redirect('/docker')