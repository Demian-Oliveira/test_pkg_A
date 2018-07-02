import pkg_resources  # part of setuptools

# https://uoftcoders.github.io/studyGroup/lessons/python/packages/lesson/
# https://github.com/UofTCoders/studyGroup/blob/gh-pages/lessons/python/packages/lesson.md
# https://github.com/jladan/package_demo/blob/master/setup.py


class PackageA:
    def __init__(self):
        pass

    def get_version(self):
        # require = lower(name) -> name='PackageA',
        version = pkg_resources.require("packagea")[0].version
        return version

    def print_version(self):
        print('Package_A: {}'.format(self.get_version()))
