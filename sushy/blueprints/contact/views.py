from flask import Blueprint, flash, redirect, request, url_for, render_template

from sushy.blueprints.contact.form import ContactForm

contact = Blueprint('contact', __name__, template_folder='templates')
contact.route('/contact', methods=['POST', 'GET'])


def index():
    form = ContactForm()
    if form.validate_on_submit():
        # This prevents circular imports.
        from sushy.blueprints.contact.task import delivery_contact_email
        delivery_contact_email.delay(
            request.form.get('email'),
            request.form.get('message'),
        )
        flash('Thanks, expect a response shortly.', 'success')
        return redirect(url_for('contact.index'))
    return render_template('contact.index.j2')
