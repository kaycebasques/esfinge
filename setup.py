import setuptools

setuptools.setup(
    name='esfinge',
    version='0.0.10',
    packages=['esfinge'],
    install_requires=[],
    package_data={
        'esfinge': [
            'layout.html',
            'theme.conf',
            'esfinge.css',
            'page.html'
        ]
    }
)
