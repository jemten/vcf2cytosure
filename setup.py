from setuptools import setup

setup(
	name='vcf2cytosure',
	version='0.1',
	author='Marcel Martin',
	author_email='marcel.martin@scilifelab.se',
	url='https://github.com/NBISweden/vcf2cytosure',
	description='Convert VCF with structural variations to CytoSure format',
	#long_description=long_description,
	license='MIT',
	#packages=[],
	py_modules=['vcf2cytosure'],
	install_requires=['lxml', 'cyvcf2'],
	entry_points={'console_scripts': ['vcf2cytosure=vcf2cytosure:main']},
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Environment :: Console",
		"Intended Audience :: Science/Research",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Programming Language :: Python :: 3",
		"Topic :: Scientific/Engineering :: Bio-Informatics"
	]
)
