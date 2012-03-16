import mongokit
import datetime
import common
import zlib
import bson.binary

'''
Example 4 adds a simple custom type that compresses values behind the scenes using zlib, and stores
them as binary representations
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

class CompressedUnicode(mongokit.CustomType):
	mongo_type = bson.binary.Binary
	python_type = unicode

	def to_bson(self, value):
		return bson.binary.Binary(zlib.compress(str(value)))

	def to_python(self, value):
		return unicode(zlib.decompress(str(value)))

@common.con.register
class BlogPost(Base):
	__collection__ = 'posts'
	structure = {
		'title': unicode,
		'body': CompressedUnicode(),
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
