import orm
from models import User, Blog, Comment

async def test():
	await orm.create_pool(user='www-date', password='www-date',database='awesome')
	u =User(name='Test', email='Test@example.com', password='123456',image='about:blank')
	await u.save()

for x in test():
	pass
	
