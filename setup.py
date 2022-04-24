from setuptools import setup, find_namespace_packages
setup(
        name='OFA', 
        packages=['OFA', 'OFA.data', 'OFA.models', 'OFA.tasks', 'OFA.criterions', 'OFA.utils'],
        package_dir={
            'OFA':'.',
            'OFA.data':'./data',
            'OFA.models':'./models',
            'OFA.tasks':'./tasks',
            'OFA.criterions':'./criterions',
            'OFA.utils':'./utils' 
        },
        package_data={"": ["*.txt", "*.json", "*.bpe"]}
)
