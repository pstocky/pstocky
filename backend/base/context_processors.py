# -*- coding:utf-8 -*-


def site_info(request):
    return {'brand_logo': 'DjangoStarterKit',  # show in navbar
            'nav_list': (
                ('/', 'Home'),
                ('/admin', 'Admin'),
            ),
            }
