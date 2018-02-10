from distutils.core import setup
from setup_local import *

setup(
	py_modules=(m.__name__,),
	url='http://robertdick.org/python/mods.html',
	version=m.__version__,
	name=m.__name__,
	description=m.__doc__.split('\n')[0],
	long_description=m.__doc__,
	download_url = 'http://robertdick.org/python/%s-%s.tar.gz' %
		(m.__name__, m.__version__),
	author = m.__author__,
	author_email = m.__author_email__,
	license = 'modified Python',
	classifiers=classifiers,
)
