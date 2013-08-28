# coding=utf-8
"""Tasks for setting up sphinx."""
import fabtools
from fabric.api import task, sudo, fastprint
from fabric.colors import green, blue


@task
def setup_latex():
    """Install latex and friends needed to generate sphinx PDFs."""
    fastprint(blue('Setting up LaTeX'))
    fabtools.deb.update_index(quiet=True)
    fabtools.require.deb.package('texlive-latex-extra')
    fabtools.require.deb.package('texinfo')
    fabtools.require.deb.package('texlive-fonts-recommended')
    fastprint(green('Setting up LaTeX completed'))


@task
def setup_sphinx():
    """Install sphinx from pip.

    We prefer packages from pip as ubuntu packages are usually old.
    To build the Documentation we also need to check and update the
    subjacent docutils installation"""
    fastprint(blue('Setting up Sphinx'))
    if fabtools.is_installed('docutils-common'):
        sudo('apt-get remove docutils-common')
    if fabtools.is_installed('docutils-doc'):
        sudo('apt-get remove docutils-doc')
    if fabtools.is_installed('python-docutils'):
        sudo('apt-get remove python-docutils')
    sudo('pip install --upgrade docutils==0.10')
    sudo('pip install sphinx')
    fastprint(green('Setting up Sphinx completed'))


@task
def setup_transifex():
    """Install transifex client."""
    fastprint(blue('Setting up transifex command line client'))
    sudo('pip install transifex-client')
    fastprint(green('Setting up transifex command line client completed'))
