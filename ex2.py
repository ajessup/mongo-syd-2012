import mongokit
import datetime
import common

'''
Example 2 demonstrates a couple of ways in which you can validate an object
before mongokit will commit it. Also shows off the default_values attribute.
'''

@common.con.register
class BlogPost(mongokit.Document):
	__collection__ = 'posts'
	structure = {
		'title': unicode,
		'body': unicode,
		'author': mongokit.ObjectId,
		'date_creation': datetime.datetime,
		'rank':int,
		'comments':[{
			'author': mongokit.ObjectId,
			'comment': unicode,
		}]
	}
	required_fields = ['title', 'author', 'date_creation']
	default_values = {
		'rank':0,
		'date_creation':datetime.datetime.utcnow
	}
	def validate(self, *args, **kwargs):
		assert self['date_creation'] < datetime.datetime.utcnow()
		super(BlogPost, self).validate(*args, **kwargs)
