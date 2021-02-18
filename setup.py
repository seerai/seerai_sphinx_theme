from setuptools import setup
from io import open
from seerai_sphinx_theme import __version__

setup(
    name = 'seerai_sphinx_theme',
    version =__version__,
    author = 'Shift Lab',
    author_email= 'info@shiftlabny.com',
    url="https://github.com/seerai/seerai_sphinx_theme",
    docs_url="https://github.com/seerai/seerai_sphinx_theme",
    description='SeerAI Sphinx Theme',
    py_modules = ['seerai_sphinx_theme'],
    packages = ['seerai_sphinx_theme'],
    include_package_data=True,
    zip_safe=False,
    package_data={'seerai_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/fonts/*.*',
        'static/images/*.*',
        'theme_variables.jinja'
    ]},
    entry_points = {
        'sphinx.html_themes': [
            'seerai_sphinx_theme = seerai_sphinx_theme',
        ]
    },
    license= 'MIT License',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation"
    ],
    install_requires=[
       'sphinx'
    ]
)
