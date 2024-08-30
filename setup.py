import setuptools

setuptools.setup(
    url='https://github.com/splewis/sm-builder',
    scripts=['scripts/smbuilder', 'scripts/smstruct', 'scripts/smversion'],
    package_data={'smbuilder': ['plugins/*.sp', 'plugins/smbuild']},
)
