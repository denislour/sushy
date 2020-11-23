from utils.flask_mailplus import send_template_message
from sushy.app import create_celery_app

celery = create_celery_app()


@celery.task()
def deliver_contact_email(email, message):
    """
    Send a contact e-mail.
    """
    ctx = {'email': email, 'message': message}

    send_template_message(
        subject='[Sushy] Contact',
        sender=email,
        recipients=[celery.conf.get('MAIL_USERNAME')],
        reply_to=email,
        template='contact/mail/index', ctx=ctx,
    )

    return None
