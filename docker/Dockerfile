FROM python:3.12

# Le tag Python sera injecté depuis GitHub Actions
ARG PACKAGE_VERSION

# Installer le paquet depuis Test PyPI avec la bonne version
RUN pip install -i https://test.pypi.org/simple/ nrvplinet==${PACKAGE_VERSION}

# Import une première fois pour compiler les fichiers .mod
RUN python3 -c "import nrvplinet"