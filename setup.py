from setuptools import setup


setup(
    name='helloworld',
    install_requires=[
        'Django',
        'em_tools',
        'uwsgi',
        'prometheus_client',
        'setuptools_scm',
    ],
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
)
