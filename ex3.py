import mongokit
import datetime
import common

'''
Example 3 seperates out the logic behind the 'date_creation' field so that it can
be re-used in other models.
'''

class Base(mongokit.Document):
	structure = {
		'date_creation': datetime.datetime,
	}
	required_fields = ['date_creation']
	default_values = {
		'date_creation':datetime.datetime.utcnow
	}

	def validate(self, *args, **kwargs):
		assert self['date_creation'] < datetime.datetime.utcnow()
		super(Base, self).validate(*args, **kwargs)

@common.con.register
class BlogPost(Base):
	__collection__ = 'posts'
	structure = {
		'title': unicode,
		'body': unicode,
		'author': mongokit.ObjectId,
		'rank':int,
		'comments':[{
			'author': mongokit.ObjectId,
			'comment': unicode,
		}]
	}
	required_fields = ['title', 'author']
	default_values = {
		'rank':0,
	}
