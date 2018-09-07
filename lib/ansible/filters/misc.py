

def format2(what, fmt):
    return fmt % what


def domain2dn(domain):
    return ','.join('DC=%s' % s for s in domain.split('.'))


class FilterModule(object):
    '''Custom filters'''

    def filters(self):
        return {
            'format2': format2,
            'domain2dn': domain2dn,
        }

