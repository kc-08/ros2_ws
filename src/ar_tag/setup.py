from setuptools import find_packages, setup

package_name = 'ar_tag'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kailync',
    maintainer_email='kailync@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'tag_test_node = ar_tag.tag_test_node:main',
            'obstacle_node = ar_tag.obstacle_node:main',
            'AR_tag_detector_node = ar_tag.AR_tag_detector_node:main'
        ],
    },
)
