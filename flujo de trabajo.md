# 1. Crear el entorno (.venv)
python -m venv .venv

# 2. Activar el entorno
# En Linux/macOS:
source .venv/bin/activate
# En Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt