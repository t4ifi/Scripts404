# 🗑️ Desinstalador Profundo de Windows

Programa para escanear y desinstalar programas de Windows de forma profunda, eliminando archivos residuales y entradas del registro.

## 🚀 Características

- ✅ Escanea TODOS los programas instalados (incluyendo los internos de Windows)
- ✅ Muestra información detallada de cada programa
- ✅ Desinstalación estándar usando el desinstalador oficial
- ✅ **Limpieza profunda**: Elimina archivos residuales y entradas del registro
- ✅ Búsqueda rápida de programas
- ✅ Interfaz gráfica intuitiva

## 📋 Requisitos

- Windows 7 o superior
- Python 3.7+ (solo para desarrollo)

## 🔧 Compilar a .EXE

### Opción 1: Usando el script automático (RECOMENDADO)

1. Abre PowerShell o CMD como **Administrador**
2. Navega a la carpeta del proyecto
3. Ejecuta:
   ```batch
   build_exe.bat
   ```

### Opción 2: Manualmente

1. Instala PyInstaller:
   ```batch
   pip install pyinstaller
   ```

2. Compila el programa:
   ```batch
   pyinstaller --onefile --windowed --name="DesinstaladorWindows" uninstaller.py
   ```

3. El archivo .exe estará en la carpeta `dist/`

## 💻 Uso

### Como script Python
```batch
python uninstaller.py
```

### Como ejecutable
1. Ejecuta `DesinstaladorWindows.exe` como **ADMINISTRADOR**
2. Haz clic en "🔍 Escanear Programas"
3. Selecciona un programa de la lista
4. Elige una opción:
   - **Desinstalar**: Ejecuta el desinstalador oficial
   - **Limpieza Profunda**: Elimina TODO (archivos + registro)

## ⚠️ IMPORTANTE

- **SIEMPRE ejecuta el programa como ADMINISTRADOR**
- La opción "Limpieza Profunda" es **IRREVERSIBLE**
- Ten cuidado al desinstalar programas del sistema de Windows
- Crea un punto de restauración antes de usar la limpieza profunda

## 🎯 Funciones

### Escaneo de Programas
Escanea estas ubicaciones del registro:
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`
- `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\...\Uninstall` (programas de 32 bits)
- `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`

### Desinstalación Estándar
Ejecuta el comando de desinstalación oficial del programa.

### Limpieza Profunda
1. Elimina la carpeta de instalación
2. Elimina la entrada del registro
3. Busca y elimina carpetas residuales en:
   - `%PROGRAMDATA%`
   - `%APPDATA%`
   - `%LOCALAPPDATA%`

## 🛡️ Seguridad

- El programa NO es un virus ni malware
- Todo el código fuente está disponible
- Requiere permisos de administrador porque modifica el sistema
- Úsalo bajo tu propia responsabilidad

## 📝 Licencia

Este proyecto es de código abierto. Úsalo y modifícalo libremente.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de mejorar el código.

## ⚡ Consejos de Optimización

1. **Antes de desinstalar**, cierra todos los programas
2. **Crea un punto de restauración** del sistema
3. **No desinstales** programas críticos de Windows como:
   - Microsoft Visual C++ Redistributables
   - .NET Framework
   - DirectX
   - Controladores de hardware

4. **Usa la limpieza profunda** solo para programas que ya desinstalaste pero dejaron residuos

## 🐛 Solución de Problemas

### "Acceso denegado"
➡️ Ejecuta el programa como Administrador

### "No se puede eliminar la carpeta"
➡️ Cierra el programa que estás intentando desinstalar

### "Error al leer el registro"
➡️ Algunos programas pueden tener permisos especiales, esto es normal

## 📞 Soporte

Si encuentras algún error o tienes sugerencias, por favor reporta el issue.

---

**⚠️ DISCLAIMER**: Este programa modifica el sistema operativo. Úsalo con precaución y siempre haz copias de seguridad antes de realizar cambios importantes.
