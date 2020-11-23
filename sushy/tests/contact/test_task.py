from sushy.extensions import mail
from sushy.blueprints.contact.tasks import deliver_contact_email


class TestTask(object):
    def test_deliver_support_email(self):
        form = {
            'email': 'foo@bar.com',
            'message': 'Test message from sushy.'
        }

        with mail.record_messages() as outbox:
            deliver_contact_email(form.get('email'), form.get('message'))

            assert len(outbox) == 1
            assert form.get('email') in outbox[0].body
