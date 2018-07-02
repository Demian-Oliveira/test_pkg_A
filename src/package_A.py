import pkg_resources  # part of setuptools

# https://uoftcoders.github.io/studyGroup/lessons/python/packages/lesson/
# https://github.com/UofTCoders/studyGroup/blob/gh-pages/lessons/python/packages/lesson.md
# https://github.com/jladan/package_demo/blob/master/setup.py


class PackageA:
    def __init__(self):
        pass

    # https://stackoverflow.com/questions/2058802/how-can-i-get-the-version-defined-in-setup-py-setuptools-in-my-package
    # https://www.programcreek.com/python/example/325/pkg_resources.require
    # https://github.com/mseri/xapitodict/blob/master/setup.py
    def get_version(self):
        version = pkg_resources.require("packagea")[0].version
        return version

    def print_version(self):
        print('Package_A: {}'.format(self.get_version()))


if __name__ == '__main__':
    pkg = PackageA()
    pkg.print_version()
    print('teste')
