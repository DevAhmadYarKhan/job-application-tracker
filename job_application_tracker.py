from app import app

# The following block of code is not part of the tutorial
# I have added it to make running and debugging the app simpler
if __name__ == "__main__":
    app.run(debug=True)

import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Job

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Job': Job}