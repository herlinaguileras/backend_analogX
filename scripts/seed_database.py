"""
AnalogX — Planetary Analog Discovery Engine
Módulo: scripts.seed_database
Descripción: CLI runner para la inicialización y carga de base de datos SQLite (analogx.db).
"""

import os
import sys

# Asegurar backend en PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core.seed import seed_database

if __name__ == "__main__":
    seed_database()
