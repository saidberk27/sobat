from setuptools import setup

package_name = 'halka_gorev'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='said',
    maintainer_email='said@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dummy_mesafe = halka_gorev.dummy_mesafe_sensoru:main',
            'halka_arama = halka_gorev.halka_arama:main',
            'mesafe_sensoru_oku = halka_gorev.mesafe_sensor_oku_node'
        ],
    },
)
