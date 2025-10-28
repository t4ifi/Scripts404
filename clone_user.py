import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import subprocess
import os
import shutil
import getpass
import threading

class UserCloner:
    def __init__(self, root):
        self.root = root
        self.root.title("Clonador de Usuarios de Windows")
        self.root.geometry("700x650")
        self.root.configure(bg='#2b2b2b')
        
        self.current_user = getpass.getuser()
        self.create_widgets()
        
    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#2b2b2b')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título
        title_label = tk.Label(
            main_frame,
            text="👥 Clonador de Usuarios de Windows",
            font=("Arial", 18, "bold"),
            bg='#2b2b2b',
            fg='#00ff00'
        )
        title_label.pack(pady=(0, 20))
        
        # Info del usuario actual
        current_user_frame = tk.LabelFrame(
            main_frame,
            text="Usuario Actual (Origen)",
            bg='#2b2b2b',
            fg='white',
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10
        )
        current_user_frame.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(
            current_user_frame,
            text=f"📂 {self.current_user}",
            font=("Arial", 14),
            bg='#2b2b2b',
            fg='#00d4ff'
        ).pack(anchor=tk.W)
        
        tk.Label(
            current_user_frame,
            text=f"Ruta: C:\\Users\\{self.current_user}",
            font=("Arial", 9),
            bg='#2b2b2b',
            fg='#888888'
        ).pack(anchor=tk.W, pady=(5, 0))
        
        # Nuevo usuario
        new_user_frame = tk.LabelFrame(
            main_frame,
            text="Nuevo Usuario (Destino)",
            bg='#2b2b2b',
            fg='white',
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10
        )
        new_user_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Nombre de usuario
        username_frame = tk.Frame(new_user_frame, bg='#2b2b2b')
        username_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(
            username_frame,
            text="Nombre de usuario:",
            bg='#2b2b2b',
            fg='white',
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.username_entry = tk.Entry(
            username_frame,
            font=("Arial", 11),
            bg='#3c3c3c',
            fg='white',
            insertbackground='white',
            relief=tk.FLAT,
            width=30
        )
        self.username_entry.pack(side=tk.LEFT, ipady=5)
        
        # Contraseña
        password_frame = tk.Frame(new_user_frame, bg='#2b2b2b')
        password_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(
            password_frame,
            text="Contraseña:           ",
            bg='#2b2b2b',
            fg='white',
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.password_entry = tk.Entry(
            password_frame,
            font=("Arial", 11),
            bg='#3c3c3c',
            fg='white',
            insertbackground='white',
            relief=tk.FLAT,
            width=30,
            show='●'
        )
        self.password_entry.pack(side=tk.LEFT, ipady=5)
        
        # Mostrar contraseña
        self.show_password_var = tk.BooleanVar()
        show_password_check = tk.Checkbutton(
            password_frame,
            text="Mostrar",
            variable=self.show_password_var,
            command=self.toggle_password,
            bg='#2b2b2b',
            fg='white',
            selectcolor='#3c3c3c',
            activebackground='#2b2b2b',
            activeforeground='white',
            font=("Arial", 9)
        )
        show_password_check.pack(side=tk.LEFT, padx=(10, 0))
        
        # Confirmar contraseña
        confirm_frame = tk.Frame(new_user_frame, bg='#2b2b2b')
        confirm_frame.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(
            confirm_frame,
            text="Confirmar contraseña:",
            bg='#2b2b2b',
            fg='white',
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=(0, 10))
        
        self.confirm_entry = tk.Entry(
            confirm_frame,
            font=("Arial", 11),
            bg='#3c3c3c',
            fg='white',
            insertbackground='white',
            relief=tk.FLAT,
            width=30,
            show='●'
        )
        self.confirm_entry.pack(side=tk.LEFT, ipady=5)
        
        # Tipo de usuario
        type_frame = tk.Frame(new_user_frame, bg='#2b2b2b')
        type_frame.pack(fill=tk.X)
        
        tk.Label(
            type_frame,
            text="Tipo de usuario:",
            bg='#2b2b2b',
            fg='white',
            font=("Arial", 10, "bold")
        ).pack(side=tk.LEFT, padx=(0, 20))
        
        self.user_type = tk.StringVar(value="normal")
        
        tk.Radiobutton(
            type_frame,
            text="👤 Usuario Normal",
            variable=self.user_type,
            value="normal",
            bg='#2b2b2b',
            fg='white',
            selectcolor='#3c3c3c',
            activebackground='#2b2b2b',
            activeforeground='white',
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=(0, 20))
        
        tk.Radiobutton(
            type_frame,
            text="👑 Administrador",
            variable=self.user_type,
            value="admin",
            bg='#2b2b2b',
            fg='white',
            selectcolor='#3c3c3c',
            activebackground='#2b2b2b',
            activeforeground='white',
            font=("Arial", 10)
        ).pack(side=tk.LEFT)
        
        # Opciones de clonado
        clone_options_frame = tk.LabelFrame(
            main_frame,
            text="Opciones de Clonado",
            bg='#2b2b2b',
            fg='white',
            font=("Arial", 11, "bold"),
            padx=15,
            pady=10
        )
        clone_options_frame.pack(fill=tk.X, pady=(0, 20))
        
        self.clone_files = tk.BooleanVar(value=True)
        self.clone_desktop = tk.BooleanVar(value=True)
        self.clone_documents = tk.BooleanVar(value=True)
        self.clone_downloads = tk.BooleanVar(value=True)
        self.clone_pictures = tk.BooleanVar(value=True)
        self.clone_videos = tk.BooleanVar(value=True)
        self.clone_music = tk.BooleanVar(value=True)
        self.clone_appdata = tk.BooleanVar(value=True)
        self.clone_browsers = tk.BooleanVar(value=True)
        self.clone_startup = tk.BooleanVar(value=True)
        self.clone_registry = tk.BooleanVar(value=True)
        
        options = [
            (self.clone_desktop, "📋 Escritorio (Desktop)"),
            (self.clone_documents, "📄 Documentos (Documents)"),
            (self.clone_downloads, "📥 Descargas (Downloads)"),
            (self.clone_pictures, "🖼️ Imágenes (Pictures)"),
            (self.clone_videos, "🎬 Videos"),
            (self.clone_music, "🎵 Música"),
            (self.clone_appdata, "⚙️ Configuraciones de Programas (AppData)"),
            (self.clone_browsers, "🌐 Navegadores (Firefox, Chrome, Edge)"),
            (self.clone_startup, "🚀 Programas al Inicio (Startup)"),
            (self.clone_registry, "🗝️ Configuraciones del Registro (ODBC, etc.)"),
        ]
        
        for var, text in options:
            tk.Checkbutton(
                clone_options_frame,
                text=text,
                variable=var,
                bg='#2b2b2b',
                fg='white',
                selectcolor='#3c3c3c',
                activebackground='#2b2b2b',
                activeforeground='white',
                font=("Arial", 10)
            ).pack(anchor=tk.W, pady=2)
        
        # Botón de clonar
        self.clone_button = tk.Button(
            main_frame,
            text="🚀 CLONAR USUARIO",
            command=self.clone_user,
            bg='#0078d4',
            fg='white',
            font=("Arial", 12, "bold"),
            relief=tk.FLAT,
            padx=30,
            pady=12,
            cursor="hand2"
        )
        self.clone_button.pack(pady=(0, 15))
        
        # Log de progreso
        log_frame = tk.LabelFrame(
            main_frame,
            text="Progreso",
            bg='#2b2b2b',
            fg='white',
            font=("Arial", 10, "bold")
        )
        log_frame.pack(fill=tk.BOTH, expand=True)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=8,
            font=("Consolas", 9),
            bg='#1e1e1e',
            fg='#00ff00',
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
    def toggle_password(self):
        """Mostrar/ocultar contraseña"""
        if self.show_password_var.get():
            self.password_entry.config(show='')
            self.confirm_entry.config(show='')
        else:
            self.password_entry.config(show='●')
            self.confirm_entry.config(show='●')
    
    def log(self, message):
        """Agregar mensaje al log"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update()
    
    def clone_user(self):
        """Clonar usuario actual a uno nuevo"""
        # Validaciones
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()
        
        if not username:
            messagebox.showerror("Error", "Debes ingresar un nombre de usuario.")
            return
        
        if not password:
            messagebox.showerror("Error", "Debes ingresar una contraseña.")
            return
        
        if password != confirm:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return
        
        # Validar nombre de usuario
        if len(username) > 20 or ' ' in username:
            messagebox.showerror("Error", "El nombre de usuario no puede contener espacios ni tener más de 20 caracteres.")
            return
        
        # Confirmación
        user_type_text = "ADMINISTRADOR" if self.user_type.get() == "admin" else "NORMAL"
        
        response = messagebox.askyesno(
            "Confirmar Clonado",
            f"¿Estás seguro de clonar el usuario?\n\n"
            f"Usuario origen: {self.current_user}\n"
            f"Usuario nuevo: {username}\n"
            f"Tipo: {user_type_text}\n\n"
            f"Este proceso puede tomar varios minutos.\n"
            f"¿Continuar?"
        )
        
        if not response:
            return
        
        # Deshabilitar botón
        self.clone_button.config(state=tk.DISABLED)
        self.log_text.delete(1.0, tk.END)
        
        def clone_thread():
            try:
                self.log("=" * 60)
                self.log("🚀 INICIANDO CLONADO DE USUARIO")
                self.log("=" * 60)
                self.log("")
                
                # 1. Crear usuario
                self.log(f"[1/4] Creando usuario '{username}'...")
                try:
                    cmd = f'net user {username} {password} /add'
                    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        self.log(f"✓ Usuario '{username}' creado exitosamente")
                    else:
                        raise Exception(result.stderr)
                except Exception as e:
                    self.log(f"✗ Error al crear usuario: {str(e)}")
                    raise
                
                # 2. Agregar a grupo de administradores si es necesario
                if self.user_type.get() == "admin":
                    self.log(f"[2/4] Agregando '{username}' al grupo de Administradores...")
                    try:
                        cmd = f'net localgroup Administradores {username} /add'
                        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                        
                        if result.returncode == 0:
                            self.log(f"✓ Usuario agregado al grupo de Administradores")
                        else:
                            # Intentar en inglés
                            cmd = f'net localgroup Administrators {username} /add'
                            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                            if result.returncode == 0:
                                self.log(f"✓ Usuario agregado al grupo de Administrators")
                            else:
                                self.log(f"⚠ No se pudo agregar al grupo de administradores")
                    except Exception as e:
                        self.log(f"⚠ Advertencia: {str(e)}")
                else:
                    self.log(f"[2/4] Usuario tipo normal, no se agregará a Administradores")
                
                # 3. Copiar archivos
                self.log("")
                self.log(f"[3/4] Copiando archivos y configuraciones...")
                
                source_path = f"C:\\Users\\{self.current_user}"
                dest_path = f"C:\\Users\\{username}"
                
                # Esperar a que se cree la carpeta del usuario
                self.log("Esperando a que Windows cree el perfil del usuario...")
                
                # Forzar la creación del perfil iniciando sesión (simulado)
                # Nota: El perfil se creará realmente cuando el usuario inicie sesión por primera vez
                # Pero podemos preparar la estructura
                
                if not os.path.exists(dest_path):
                    self.log(f"⚠ La carpeta del usuario aún no existe. Se creará en el primer inicio de sesión.")
                    self.log(f"⚠ Los archivos se copiarán cuando el usuario inicie sesión por primera vez.")
                    
                    # Crear script de copia para ejecutar en el primer inicio
                    startup_script = f"""@echo off
echo Copiando archivos del usuario {self.current_user}...
"""
                    
                    folders_to_copy = []
                    if self.clone_desktop.get():
                        folders_to_copy.append(("Desktop", "Escritorio"))
                    if self.clone_documents.get():
                        folders_to_copy.append(("Documents", "Documentos"))
                    if self.clone_downloads.get():
                        folders_to_copy.append(("Downloads", "Descargas"))
                    if self.clone_pictures.get():
                        folders_to_copy.append(("Pictures", "Imágenes"))
                    if self.clone_videos.get():
                        folders_to_copy.append(("Videos", "Videos"))
                    if self.clone_music.get():
                        folders_to_copy.append(("Music", "Música"))
                    
                    for folder, name in folders_to_copy:
                        src = f"{source_path}\\{folder}"
                        dst = f"{dest_path}\\{folder}"
                        startup_script += f'echo Copiando {name}...\n'
                        startup_script += f'xcopy "{src}" "{dst}" /E /I /H /Y\n'
                    
                    if self.clone_appdata.get():
                        startup_script += f'echo Copiando configuraciones (AppData)...\n'
                        startup_script += f'xcopy "{source_path}\\AppData\\Roaming" "{dest_path}\\AppData\\Roaming" /E /I /H /Y\n'
                        startup_script += f'xcopy "{source_path}\\AppData\\Local" "{dest_path}\\AppData\\Local" /E /I /H /Y\n'
                    
                    startup_script += 'echo.\necho Copia completada!\npause\n'
                    
                    # Guardar script en el escritorio público
                    public_desktop = "C:\\Users\\Public\\Desktop"
                    script_path = f"{public_desktop}\\CopiarArchivos_{username}.bat"
                    
                    with open(script_path, 'w', encoding='utf-8') as f:
                        f.write(startup_script)
                    
                    self.log(f"✓ Script de copia creado en: {script_path}")
                    self.log(f"  Ejecuta este script después del primer inicio de sesión del usuario.")
                
                else:
                    # Si la carpeta existe, copiar directamente
                    folders_to_copy = []
                    if self.clone_desktop.get():
                        folders_to_copy.append(("Desktop", "Escritorio"))
                    if self.clone_documents.get():
                        folders_to_copy.append(("Documents", "Documentos"))
                    if self.clone_downloads.get():
                        folders_to_copy.append(("Downloads", "Descargas"))
                    if self.clone_pictures.get():
                        folders_to_copy.append(("Pictures", "Imágenes"))
                    if self.clone_videos.get():
                        folders_to_copy.append(("Videos", "Videos"))
                    if self.clone_music.get():
                        folders_to_copy.append(("Music", "Música"))
                    
                    for folder, name in folders_to_copy:
                        src = os.path.join(source_path, folder)
                        dst = os.path.join(dest_path, folder)
                        
                        if os.path.exists(src):
                            try:
                                self.log(f"  Copiando {name}...")
                                if os.path.exists(dst):
                                    shutil.rmtree(dst)
                                shutil.copytree(src, dst)
                                self.log(f"  ✓ {name} copiado")
                            except Exception as e:
                                self.log(f"  ✗ Error copiando {name}: {str(e)}")
                    
                    # Copiar AppData (configuraciones de programas)
                    if self.clone_appdata.get():
                        self.log(f"  Copiando configuraciones (AppData)...")
                        appdata_folders = ['Roaming', 'Local']
                        
                        for appdata_folder in appdata_folders:
                            src = os.path.join(source_path, 'AppData', appdata_folder)
                            dst = os.path.join(dest_path, 'AppData', appdata_folder)
                            
                            if os.path.exists(src):
                                try:
                                    self.log(f"    Copiando AppData\\{appdata_folder}...")
                                    
                                    # Usar xcopy para mejor manejo de permisos
                                    cmd = f'xcopy "{src}" "{dst}" /E /I /H /Y'
                                    subprocess.run(cmd, shell=True, capture_output=True)
                                    
                                    self.log(f"    ✓ AppData\\{appdata_folder} copiado")
                                except Exception as e:
                                    self.log(f"    ⚠ Error en AppData\\{appdata_folder}: {str(e)}")
                    
                    # Copiar configuraciones de navegadores específicamente
                    if self.clone_browsers.get():
                        self.log(f"  Copiando configuraciones de navegadores...")
                        
                        browsers = [
                            ("Firefox", os.path.join(source_path, "AppData", "Roaming", "Mozilla", "Firefox")),
                            ("Chrome", os.path.join(source_path, "AppData", "Local", "Google", "Chrome", "User Data")),
                            ("Edge", os.path.join(source_path, "AppData", "Local", "Microsoft", "Edge", "User Data")),
                        ]
                        
                        for browser_name, browser_src in browsers:
                            if os.path.exists(browser_src):
                                try:
                                    browser_dst = browser_src.replace(self.current_user, username)
                                    self.log(f"    Copiando {browser_name}...")
                                    
                                    # Crear directorio padre si no existe
                                    os.makedirs(os.path.dirname(browser_dst), exist_ok=True)
                                    
                                    # Usar xcopy para copiar
                                    cmd = f'xcopy "{browser_src}" "{browser_dst}" /E /I /H /Y'
                                    subprocess.run(cmd, shell=True, capture_output=True)
                                    
                                    self.log(f"    ✓ {browser_name} copiado")
                                except Exception as e:
                                    self.log(f"    ⚠ Error en {browser_name}: {str(e)}")
                    
                    # Copiar programas de inicio
                    if self.clone_startup.get():
                        self.log(f"  Copiando programas de inicio...")
                        
                        startup_locations = [
                            ("Startup", os.path.join(source_path, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")),
                        ]
                        
                        for startup_name, startup_src in startup_locations:
                            if os.path.exists(startup_src):
                                try:
                                    startup_dst = startup_src.replace(self.current_user, username)
                                    self.log(f"    Copiando {startup_name}...")
                                    
                                    os.makedirs(os.path.dirname(startup_dst), exist_ok=True)
                                    
                                    cmd = f'xcopy "{startup_src}" "{startup_dst}" /E /I /H /Y'
                                    subprocess.run(cmd, shell=True, capture_output=True)
                                    
                                    self.log(f"    ✓ {startup_name} copiado")
                                except Exception as e:
                                    self.log(f"    ⚠ Error en {startup_name}: {str(e)}")
                    
                    # Copiar configuraciones del registro (ODBC, variables de entorno, etc.)
                    if self.clone_registry.get():
                        self.log(f"  Exportando configuraciones del registro...")
                        
                        try:
                            import winreg
                            
                            # Exportar configuraciones de usuario actual
                            reg_export_file = f"C:\\Users\\Public\\{self.current_user}_registry.reg"
                            
                            # Exportar el registro del usuario actual
                            self.log(f"    Exportando HKEY_CURRENT_USER...")
                            cmd = f'reg export HKCU "{reg_export_file}" /y'
                            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                            
                            if result.returncode == 0:
                                self.log(f"    ✓ Registro exportado a: {reg_export_file}")
                                self.log(f"    ⚠ IMPORTANTE: Después del primer inicio de sesión del nuevo usuario,")
                                self.log(f"       ejecuta: reg import \"{reg_export_file}\"")
                                self.log(f"       o haz doble clic en el archivo .reg")
                            else:
                                self.log(f"    ⚠ No se pudo exportar el registro completo")
                            
                            # Copiar configuraciones ODBC específicamente
                            self.log(f"    Exportando configuraciones ODBC...")
                            odbc_export_file = f"C:\\Users\\Public\\{self.current_user}_odbc.reg"
                            
                            # ODBC está en HKEY_CURRENT_USER\Software\ODBC
                            cmd = f'reg export "HKCU\\Software\\ODBC" "{odbc_export_file}" /y'
                            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
                            
                            if result.returncode == 0:
                                self.log(f"    ✓ Configuraciones ODBC exportadas")
                                
                                # Crear un script para importar en el nuevo usuario
                                import_script = f"""@echo off
echo Importando configuraciones del registro para {username}...
echo.
echo [1/2] Importando configuraciones ODBC...
reg import "{odbc_export_file}"
echo.
echo [2/2] Importando configuraciones del usuario...
reg import "{reg_export_file}"
echo.
echo Configuraciones importadas!
echo Reinicia la sesión para aplicar todos los cambios.
pause
"""
                                import_script_path = f"C:\\Users\\Public\\Desktop\\ImportarConfiguraciones_{username}.bat"
                                with open(import_script_path, 'w', encoding='utf-8') as f:
                                    f.write(import_script)
                                
                                self.log(f"    ✓ Script de importación creado: {import_script_path}")
                            else:
                                self.log(f"    ⚠ No se pudieron exportar configuraciones ODBC")
                            
                        except Exception as e:
                            self.log(f"    ⚠ Error exportando registro: {str(e)}")
                
                # 4. Finalizar
                self.log("")
                self.log("[4/4] Finalizando...")
                self.log("")
                self.log("=" * 60)
                self.log("✓ CLONADO COMPLETADO EXITOSAMENTE")
                self.log("=" * 60)
                self.log("")
                self.log(f"Usuario: {username}")
                self.log(f"Tipo: {user_type_text}")
                self.log(f"Contraseña: {'*' * len(password)}")
                self.log("")
                self.log("INSTRUCCIONES:")
                self.log("1. Cierra sesión de tu usuario actual")
                self.log("2. Inicia sesión con el nuevo usuario")
                self.log(f"3. Usuario: {username}")
                self.log(f"4. Contraseña: (la que configuraste)")
                
                if not os.path.exists(dest_path):
                    self.log("")
                    self.log("⚠ IMPORTANTE:")
                    self.log(f"  Ejecuta el script 'CopiarArchivos_{username}.bat'")
                    self.log(f"  desde el Escritorio Público después del primer inicio.")
                
                self.root.after(0, lambda: messagebox.showinfo(
                    "Clonado Completado",
                    f"Usuario '{username}' clonado exitosamente.\n\n"
                    f"Ahora puedes cerrar sesión e iniciar con el nuevo usuario.\n\n"
                    f"Usuario: {username}\n"
                    f"Tipo: {user_type_text}"
                ))
                
            except Exception as e:
                self.log("")
                self.log(f"✗ ERROR: {str(e)}")
                self.root.after(0, lambda: messagebox.showerror(
                    "Error",
                    f"Error durante el clonado: {str(e)}\n\n"
                    "Asegúrate de ejecutar el programa como Administrador."
                ))
            finally:
                self.root.after(0, lambda: self.clone_button.config(state=tk.NORMAL))
        
        thread = threading.Thread(target=clone_thread, daemon=True)
        thread.start()

def main():
    root = tk.Tk()
    app = UserCloner(root)
    root.mainloop()

if __name__ == "__main__":
    main()
