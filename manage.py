#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

#http://localhost:8000/car-details/compare-prices/


def main():
    """Run administrative tasks."""
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "djangoProject__veprintcev_bronislav__main.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        message = (
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        )
        raise ImportError(message) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()



