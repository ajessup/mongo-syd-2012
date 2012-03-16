import mongokit
import datetime
import common

'''
Example 1 is our base model. Very simple, but already MongoKit gives us some validation
for free.
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