from setuptools import setup

package_name = 'motor_kontrol'

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
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ana_script = motor_kontrol.kontrol_motor:main',
            'dummy_script = motor_kontrol.dummy_motor:main',
            'klavye_script = motor_kontrol.klavye_kontrol:main'
        ],
    },
)
