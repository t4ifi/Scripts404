@echo off
echo ========================================
echo  Compilando Clonador de Usuarios
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no está instalado o no está en el PATH
    echo Por favor instala Python desde https://www.python.org/
    pause
    exit /b 1
)

echo [1/3] Instalando PyInstaller (si no está instalado)...
python -m pip install pyinstaller

echo.
echo [2/3] Compilando a ejecutable (optimizado para antivirus)...
python -m PyInstaller --onefile --windowed --icon=NONE --name="ClonadorUsuarios" --noupx --clean clone_user.py

echo.
echo [3/3] Limpiando archivos temporales...
rmdir /s /q build
del ClonadorUsuarios.spec

echo.
echo ========================================
echo  COMPILACION COMPLETADA
echo ========================================
echo.
echo El archivo .exe se encuentra en la carpeta "dist"
echo Nombre: ClonadorUsuarios.exe
echo.
echo IMPORTANTE: Ejecuta el .exe como ADMINISTRADOR para
echo poder crear usuarios correctamente.
echo.
pause
