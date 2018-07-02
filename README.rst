===================
Header 1
===================

**Header 2**

1 - To prove this works, we can run `python setup.py develop`:
    You will see:
        running develop
        running egg_info
        creating PackageA.egg-info
        writing PackageA.egg-info/PKG-INFO
        writing dependency_links to PackageA.egg-info/dependency_links.txt
        writing top-level names to PackageA.egg-info/top_level.txt
        writing manifest file 'PackageA.egg-info/SOURCES.txt'
        reading manifest file 'PackageA.egg-info/SOURCES.txt'
        writing manifest file 'PackageA.egg-info/SOURCES.txt'
        running build_ext
        Creating /Users/xxxxxx/lib/python3.6/site-packages/PackageA.egg-link (link to .)
        Adding PackageA 0.0.2 to easy-install.pth file

        Installed /Users/xxxxxx/test_pkg_A
        Processing dependencies for PackageA==0.0.2
        Finished processing dependencies for PackageA==0.0.2

2 - To create a tag:
    a) git tag v0.0.3
    b) git push --tags
