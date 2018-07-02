from setuptools import setup

setup(
    # Needed to silence warnings
    name='PackageA',
    url='https://github.com/dmyanster/test_pkg_A',
    author='Dmyan',
    author_email='dmyan@qwerty.com',
    # Needed to actually package something
    packages=['packagea'],

    # # Needed for dependencies
    # install_requires=['numpy'],

    # *strongly* suggested for sharing
    #
    # git tag v0.0.2
    # git push --tags
    #
    version='0.0.2',
    license='private test code',
    description='any description',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.rst').read(),
    # # if there are any scripts
    # scripts=['scripts/hello.py'],
)