import click
from flask.cli import with_appcontext
from .utils import get_cv_by_id


@click.command('show')
@click.argument('type')
@click.argument('cv_id', type=int)
@with_appcontext
def show_command(type, cv_id):
    cv = get_cv_by_id(cv_id)
    if not cv:
        click.echo('CV not found', err=True)
        return

    if type == 'personal':
        click.echo(cv.get('personal', 'No personal information available'))
    elif type == 'experience':
        click.echo(cv.get('experience', 'No experience information available'))
    elif type == 'education':
        click.echo(cv.get('education', 'No education information available'))
    else:
        click.echo(
            'Invalid type specified. Use "personal", "experience", or "education".',
            err=True,
        )
