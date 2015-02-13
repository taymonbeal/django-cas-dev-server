from setuptools import setup

setup(
    name='django-cas-dev-server',
    version='0.1.0',
    description='Extends the Django development server to include a local CAS server.',
    url='https://github.com/TaymonB/django-cas-dev-server',
    author='Taymon A. Beal',
    author_email='taymonbeal@gmail.com',
    license='MIT',
    platforms=['OS Independent'],
    keywords='development django cas',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Software Development',
    ],
    packages=['cas_dev_server'],
    install_requires=[
        'Django>=1.7',
        'django-mama-cas',
    ],
)