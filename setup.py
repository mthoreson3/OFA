from setuptools import setup, find_namespace_packages


ofa_name = 'OFA'

pkgs = [ofa_name]

found_pkgs = find_namespace_packages(exclude=['fairseq', 'fairseq.*',
                                              'ofa_module', 'run_scripts*', 
                                              'build*', 'dist*'])

prefixed_pkgs = [ofa_name+'.'+pkg for pkg in found_pkgs]

pkg_dirs = {ofa_name: '.'}

for i, pkg in enumerate(found_pkgs):
    pkg_dir = './' + pkg.replace('.', '/')
    pkg_dirs[prefixed_pkgs[i]] = pkg_dir
    pkgs.append(prefixed_pkgs[i])

print(pkgs)
print(pkg_dirs)

setup(
        name='OFA',
        version='0.0.0',
        author='Junyang Lin and Yang An',
        packages=pkgs,
        package_dir=pkg_dirs,
        package_data={"": ["*.txt", "*.json", "*.bpe", "*.gz"]},
        zip_safe=False
)
