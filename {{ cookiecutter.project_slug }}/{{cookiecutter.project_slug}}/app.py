# -*- coding: utf-8 -*-
"""
App runner
"""
# System imports
# Third-party imports
from vulcano.app.classes import VulcanoApp

# Local imports
from {{ cookiecutter.project_slug }}.example_module import example_functions


# Create the App
APP = VulcanoApp()

# Register the module
APP.module(example_functions)


def main():
    APP.run()

# Execute the application
if __name__ == '__main__':
    main()