import mongokit

'''
Common boilerplate for setting up the DB connection. Normally you'd use something
a bit more sophisticated to handle this config.
'''

con = mongokit.Connection()
db = con['mongo_syd_2012']