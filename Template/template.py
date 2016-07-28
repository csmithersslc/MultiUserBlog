import os
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
	loader = jinja2.FileSystemLoader(os.path.dirname(__file__) + "/templates"))

class MainHandler(webapp2.RequestHandler):
	def get(self):
		template = JINJA_ENVIRONMENT.get_template('index.html')
		self.response.out.write(template)


app = webapp2.WSGIApplication([
('/', MainHandler), 
], debug=True)
