from setuptools import setup, find_packages
setup(
        name='OFA', 
        packages=find_packages(
            include=[
                'ofa_module',
                'criterions',
                'data',
                'models',
                'tasks'
                'utils']
        )
)