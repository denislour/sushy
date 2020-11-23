from flask import render_template
from sushy.extensions import mail


def send_template_message(template=None, ctx=None, *args, **kwargs):
    """
        Send email with template.
    """

    if ctx is None:
        ctx = {}
    if template is not None:
        if 'body' in kwargs:
            raise Exception('You cannot have a both template and body args')
        if 'html' in kwargs:
            raise Exception('You cannot have a both template and html args')
    kwargs['body'] = _try_render_template(template, **ctx)
    kwargs['html'] = _try_render_template(template, ext="html", **ctx)
    mail.send_message(*args, **kwargs)


def _try_render_template(template_path, ext='txt', **kwargs):
    """
        Put render template to try except.
    """
    try:
        return render_template('{0}.{1}'.format(template_path, ext), **kwargs)
    except IOError:
        pass
