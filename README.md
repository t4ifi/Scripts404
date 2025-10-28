# �️ Scripts404 - Herramientas de Optimización para Windows

Colección de herramientas avanzadas para optimizar y gestionar Windows de forma profesional.

## 📦 Programas Incluidos

### 1. 🗑️ Desinstalador Profundo de Windows
Escanea y desinstala programas de Windows de forma profunda, eliminando archivos residuales y entradas del registro.

**Características:**
- ✅ Escanea TODOS los programas instalados (incluyendo los internos de Windows)
- ✅ Muestra información detallada de cada programa
- ✅ Desinstalación estándar usando el desinstalador oficial
- ✅ **Limpieza profunda**: Elimina archivos residuales y entradas del registro
- ✅ Búsqueda rápida de programas
- ✅ Interfaz gráfica intuitiva

### 2. 👥 Clonador de Usuarios de Windows
Clona un usuario existente de Windows creando uno nuevo con EXACTAMENTE la misma configuración.

**Características:**
- ✅ Crea usuario nuevo (Normal o Administrador)
- ✅ Clona TODOS los archivos (Escritorio, Documentos, Descargas, Imágenes, Videos, Música)
- ✅ Clona configuraciones de programas (AppData completo)
- ✅ Clona navegadores completos (Firefox, Chrome, Edge) - Favoritos, contraseñas, extensiones
- ✅ Clona programas de inicio
- ✅ Clona configuraciones del registro (ODBC, variables de entorno, etc.)
- ✅ Interfaz gráfica intuitiva con selección personalizada

---

## 🚀 Características Generales

## 📋 Requisitos

- Windows 7 o superior
- Python 3.7+ (solo para desarrollo)

## 🔧 Compilar a .EXE

### Desinstalador de Windows

**Opción 1: Script automático (RECOMENDADO)**
```batch
build_exe.bat
```

**Opción 2: Manualmente**
```batch
pip install pyinstaller
python -m PyInstaller --onefile --windowed --name="DesinstaladorWindows" --noupx --clean uninstaller.py
```

### Clonador de Usuarios

**Opción 1: Script automático (RECOMENDADO)**
```batch
build_clone_exe.bat
```

**Opción 2: Manualmente**
```batch
pip install pyinstaller
python -m PyInstaller --onefile --windowed --name="ClonadorUsuarios" --noupx --clean clone_user.py
```

Los archivos .exe estarán en la carpeta `dist/`

## 💻 Uso

### 🗑️ Desinstalador de Windows

**Como script Python:**
```batch
python uninstaller.py
```

**Como ejecutable:**
1. Ejecuta `DesinstaladorWindows.exe` como **ADMINISTRADOR**
2. Haz clic en "🔍 Escanear Programas"
3. Selecciona un programa de la lista
4. Elige una opción:
   - **Desinstalar**: Ejecuta el desinstalador oficial
   - **Limpieza Profunda**: Elimina TODO (archivos + registro)

### 👥 Clonador de Usuarios

**Como script Python:**
```batch
python clone_user.py
```

**Como ejecutable:**
1. Ejecuta `ClonadorUsuarios.exe` como **ADMINISTRADOR**
2. Ingresa el nombre del nuevo usuario
3. Ingresa y confirma la contraseña
4. Elige el tipo: 👤 Usuario Normal o 👑 Administrador
5. Selecciona qué elementos clonar (archivos, configuraciones, navegadores, etc.)
6. Click en "🚀 CLONAR USUARIO"
7. Espera a que termine (verás el progreso en tiempo real)
8. Cierra sesión e inicia con el nuevo usuario
9. Ejecuta los scripts de importación del Escritorio Público si es necesario

## ⚠️ IMPORTANTE

- **SIEMPRE ejecuta el programa como ADMINISTRADOR**
- La opción "Limpieza Profunda" es **IRREVERSIBLE**
- Ten cuidado al desinstalar programas del sistema de Windows
- Crea un punto de restauración antes de usar la limpieza profunda

## 🎯 Funciones Detalladas

### 🗑️ Desinstalador de Windows

**Escaneo de Programas:**
- `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`
- `HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\...\Uninstall` (programas de 32 bits)
- `HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`

**Desinstalación Estándar:**
- Ejecuta el comando de desinstalación oficial del programa

**Limpieza Profunda:**
1. Elimina la carpeta de instalación
2. Elimina la entrada del registro
3. Busca y elimina carpetas residuales en:
   - `%PROGRAMDATA%`
   - `%APPDATA%`
   - `%LOCALAPPDATA%`

### 👥 Clonador de Usuarios

**Clonación de Archivos:**
- Escritorio, Documentos, Descargas, Imágenes, Videos, Música
- Copia bit a bit preservando permisos

**Clonación de Configuraciones:**
- AppData completo (Roaming + Local)
- Configuraciones de todos los programas instalados

**Clonación de Navegadores:**
- **Firefox**: Favoritos, contraseñas, extensiones, historial, sesiones
- **Chrome**: Favoritos, contraseñas, extensiones, historial, configuración
- **Edge**: Favoritos, contraseñas, extensiones, historial, configuración

**Clonación de Inicio:**
- Programas del menú Startup
- Scripts que se ejecutan al iniciar Windows

**Clonación del Registro:**
- Configuraciones ODBC (conexiones a bases de datos)
- Variables de entorno del usuario
- Preferencias de aplicaciones
- Todo HKEY_CURRENT_USER

## 🛡️ Seguridad

- El programa NO es un virus ni malware
- Todo el código fuente está disponible
- Requiere permisos de administrador porque modifica el sistema
- Úsalo bajo tu propia responsabilidad

## 📝 Licencia

Este proyecto es de código abierto. Úsalo y modifícalo libremente.

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de mejorar el código.

## ⚡ Consejos de Uso

### Para el Desinstalador:

1. **Antes de desinstalar**, cierra todos los programas
2. **Crea un punto de restauración** del sistema
3. **No desinstales** programas críticos de Windows como:
   - Microsoft Visual C++ Redistributables
   - .NET Framework
   - DirectX
   - Controladores de hardware
4. **Usa la limpieza profunda** solo para programas que ya desinstalaste pero dejaron residuos

### Para el Clonador de Usuarios:

1. **Cierra todos los programas** antes de clonar
2. **Crea un punto de restauración** del sistema
3. **Asegúrate de tener espacio suficiente** en disco (el doble del tamaño de tu carpeta de usuario)
4. **Después del primer inicio del nuevo usuario**, ejecuta los scripts de importación del Escritorio Público
5. **Algunas licencias de software** pueden requerir reactivación
6. **Las contraseñas guardadas en navegadores** se copiarán completamente

## 🐛 Solución de Problemas

### Problemas Comunes - Desinstalador

**"Acceso denegado"**
➡️ Ejecuta el programa como Administrador

**"No se puede eliminar la carpeta"**
➡️ Cierra el programa que estás intentando desinstalar

**"Error al leer el registro"**
➡️ Algunos programas pueden tener permisos especiales, esto es normal

### Problemas Comunes - Clonador

**"No se pudo crear el usuario"**
➡️ Ejecuta el programa como Administrador
➡️ Verifica que el nombre de usuario no exista ya

**"Error al copiar archivos"**
➡️ Asegúrate de tener espacio suficiente en disco
➡️ Cierra todos los programas antes de clonar

**"El perfil del usuario no se crea"**
➡️ Es normal, se creará en el primer inicio de sesión
➡️ Ejecuta el script de copia después del primer inicio

**"Las configuraciones no se aplican"**
➡️ Ejecuta el script `ImportarConfiguraciones_[usuario].bat` del Escritorio Público
➡️ Reinicia Windows después de importar el registro

### Antivirus - Ambos Programas

**"El antivirus lo detecta como malicioso"**
➡️ Es un falso positivo
➡️ Agrega el .exe a las excepciones del antivirus
➡️ El código fuente está completamente disponible
➡️ Sube el .exe a VirusTotal para verificar

## 📞 Soporte

Si encuentras algún error o tienes sugerencias, por favor reporta el issue.

## 📊 Estructura del Proyecto

```
Scripts404/
├── uninstaller.py           # Desinstalador profundo de Windows
├── clone_user.py            # Clonador de usuarios
├── build_exe.bat            # Compilar desinstalador a .exe
├── build_clone_exe.bat      # Compilar clonador a .exe
├── README.md                # Este archivo
└── .gitignore              # Archivos ignorados por Git
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si tienes ideas para mejorar estos scripts:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

---

**⚠️ DISCLAIMER**: Estos programas modifican el sistema operativo. Úsalos con precaución y siempre haz copias de seguridad antes de realizar cambios importantes. El autor no se hace responsable por daños causados por el mal uso de estas herramientas.

Creado por: Andrés Nuñez - t4ifi