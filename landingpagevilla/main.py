#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import urllib
import jinja2
import webapp2
import json
import cgi
from google.appengine.ext import ndb
from webapp2 import Route
from webapp2_extras.routes import DomainRoute
from enviarcorreo import enviarCorreo


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainPage(webapp2.RequestHandler):
        def get(self):
                template = JINJA_ENVIRONMENT.get_template('static/index.html')
                template_values=[]
                self.response.write(template.render(template_values))

import logging

class SendComments(webapp2.RequestHandler):
        def post(self):
	    name =cgi.escape(self.request.get("name"))
            email=cgi.escape(self.request.get("email"))
            phone =cgi.escape(self.request.get("phone"))
            message =cgi.escape(self.request.get("message"))
            enviarCorreo(name,email,phone,message)
            self.response.out.write("send")

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sendcomments', SendComments),

], debug=True)
