# (Packages/Libraries) Miscellaneous
from setuptools import setup, find_packages
from setuptools.command.install import install

class CustomInstall(install):
    def run(self):
        print("Installing IntelliGenes...")
        install.run(self)
        print("Installed IntelliGenes!")

setup(
    name = 'intelligenes',
    version = '1.1',
    author = 'William DeGroat',
    author_email = 'will.degroat@rutgers.edu',
    description = 'IntelliGenes: AI/ML pipeline for predictive analyses using multi-genomic profiles.',    
    url = 'https://github.com/drzeeshanahmed/intelligenes',
    packages = find_packages(),  
    classifiers = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ], 
    install_requires = [
        'altgraph==0.17.4',
        'cloudpickle==3.0.0',
        'contourpy==1.2.0',
        'cycler==0.12.1',
        'fonttools==4.47.2',
        'joblib==1.3.2',
        'kiwisolver==1.4.5',
        'llvmlite==0.42.0',
        'macholib==1.16.3',
        'matplotlib==3.8.2',
        'numba==0.59.0',
        'numpy==1.26.3',
        'packaging==23.2',
        'pandas==2.2.0',
        'pillow==10.2.0',
        'pyinstaller==6.3.0',
        'pyinstaller-hooks-contrib==2024.0',
        'pyparsing==3.1.1',
        'python-dateutil==2.8.2',
        'pytz==2024.1',
        'scikit-learn==1.4.0',
        'scipy==1.12.0',
        'seaborn==0.13.2',
        'shap==0.44.1',
        'six==1.16.0',
        'slicer==0.0.7',
        'threadpoolctl==3.2.0',
        'tqdm==4.66.1',
        'tzdata==2023.4',
        'xgboost==2.0.3',
    ],
    python_requires = '>=3.6',
    entry_points = {
        'console_scripts': [
            'igenes_predict=intelligenes.classification:main',
            'igenes_select=intelligenes.selection:main',
            'igenes=intelligenes.intelligenes:main',
        ]
    },
    include_package_data  = True,
    license = 'GNU General Public License v3.0',
    cmdclass = {
        'install': CustomInstall,
    }
)
