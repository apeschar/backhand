#!/usr/bin/env python2.7

from subprocess import Popen
import re

import web

urls = (
    '/vi', 'vi'
)

class vi:
    def POST(self):
        i = web.input()
        u = i.url
        if not re.match(r'sftp://\w+@[a-z0-9_.-]+/[\x21-\x77]*', u):
            raise Exception, 'invalid url'
        Popen(['mvim', '--servername', 'hq', '--remote-tab', u])
        return ''

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
