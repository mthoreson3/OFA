from setuptools import setup, find_packages


ofa_name = 'OFA'

pkgs = [ofa_name]

found_pkgs = find_packages(exclude=['fairseq', 'fairseq.*', 'ofa_module'])

prefixed_pkgs = [ofa_name+'.'+pkg for pkg in found_pkgs]

pkg_dirs = {ofa_name: '.'}

for i, pkg in enumerate(found_pkgs):
    pkg_dir = './' + pkg.replace('.', '/')
    pkg_dirs[prefixed_pkgs[i]] = pkg_dir
    pkgs.append(prefixed_pkgs[i])

setup(
        name='OFA',
        packages=pkgs,
        package_dir=pkg_dirs,
        package_data={"": ["*.txt", "*.json", "*.bpe"]}
)
