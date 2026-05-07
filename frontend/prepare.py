#!/usr/bin/env python
"""
Script auxiliar para preparar la aplicación Django para producción
Recolecta archivos estáticos y realiza migraciones
"""

import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.core.management import call_command

def main():
    print("\n=== Preparando aplicación para producción ===\n")
    
    # Recolectar archivos estáticos
    print("1. Recolectando archivos estáticos...")
    try:
        call_command('collectstatic', '--noinput', verbosity=0)
        print("   ✓ Archivos estáticos recolectados\n")
    except Exception as e:
        print(f"   ✗ Error: {e}\n")
        return 1
    
    # Realizar migraciones
    print("2. Aplicando migraciones...")
    try:
        call_command('migrate', verbosity=0)
        print("   ✓ Migraciones aplicadas\n")
    except Exception as e:
        print(f"   ✗ Error: {e}\n")
        return 1
    
    print("=== Preparación completada ===\n")
    print("Ahora puedes desplegar la aplicación en Render\n")
    return 0

if __name__ == '__main__':
    sys.exit(main())
