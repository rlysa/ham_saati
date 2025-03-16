"""
Файл setup.py для сборки и установки пакета ham_saati.
Использует setuptools для упаковки Flask-приложения.
"""

from setuptools import setup

setup(
    name="ham_saati",
    version="0.1",
    py_modules=["main"],
    include_package_data=True,  #включает файлы статики и шаблонов
    install_requires=[
        line.strip() for line in open("requirements.txt") if line.strip()
    ],
    entry_points={
        "console_scripts": [
            "ham_saati=main:app.run"
        ]
    },
)
