from blogapp import create_app, db
from blogapp.models import User, Blog, Profile

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Blog': Blog, 'Profile': Profile}

if __name__ == '__main__':
    app.run(debug=True)
