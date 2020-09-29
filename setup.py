from setuptools import setup

setup(
    name='EBMultiApp',
    version='0.1.0',
    description='Deploy multiple applications/services/websites on a single Elastic Beanstalk environment. Fork from ElasticDeploy',
    keywords='aws elastic beanstalk multi deployment',
    url='https://github.com/tscheiki/ElasticDeploy',
    author='Asdrubal Gonzalez',
    author_email='agpenton@gmail.com',
    license='MIT',
    packages=['eb_multi_app'],
    entry_points={
        'console_scripts': ['eb_multi_app=eb_multi_app.main:main'],
    },
    include_package_data=True,
    zip_safe=True
)
