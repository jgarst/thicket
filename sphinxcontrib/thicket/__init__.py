from .thicket import ThicketDomain


def setup(app):
    app.add_domain(ThicketDomain)

    return {
        'version': '0.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }

