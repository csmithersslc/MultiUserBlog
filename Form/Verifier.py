import webapp2

form = """
<form method = "post">
	What is your birthday?
	<br>

	<label> Month:
		<input type="dropdown" name="month">
	</label>
	
	<label>Day:
		<input type="text" name="day">
	</label>
	
	<label>Year:	
		<input type="text" name="year">
	</label>

	<br>
	<br>
	<input type="submit">
</form>
"""



class MainPage(webapp2.RequestHandler):
	def get(self):
		#self.response.headers['ContentType'] = 'text/plain'
		self.response.write(form)

	def post(self):
		self.response.out.write("OK.  Thanks!")

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)