import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import winreg
import subprocess
import os
import shutil
import threading

class WindowsUninstaller:
    def __init__(self, root):
        self.root = root
        self.root.title("Desinstalador Profundo de Windows")
        self.root.geometry("900x600")
        self.root.configure(bg='#2b2b2b')
        
        # Variables
        self.programs = []
        self.selected_program = None
        
        # Crear interfaz
        self.create_widgets()
        
    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#2b2b2b')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Título
        title_label = tk.Label(
            main_frame, 
            text="🗑️ Desinstalador Profundo de Windows",
            font=("Arial", 18, "bold"),
            bg='#2b2b2b',
            fg='#00ff00'
        )
        title_label.pack(pady=(0, 10))
        
        # Frame de botones superiores
        button_frame = tk.Frame(main_frame, bg='#2b2b2b')
        button_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.scan_button = tk.Button(
            button_frame,
            text="🔍 Escanear Programas",
            command=self.scan_programs,
            bg='#0078d4',
            fg='white',
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2"
        )
        self.scan_button.pack(side=tk.LEFT, padx=5)
        
        self.uninstall_button = tk.Button(
            button_frame,
            text="🗑️ Desinstalar Seleccionado",
            command=self.uninstall_program,
            bg='#d13438',
            fg='white',
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.uninstall_button.pack(side=tk.LEFT, padx=5)
        
        self.deep_clean_button = tk.Button(
            button_frame,
            text="🧹 Limpieza Profunda",
            command=self.deep_clean,
            bg='#ff6b00',
            fg='white',
            font=("Arial", 11, "bold"),
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2",
            state=tk.DISABLED
        )
        self.deep_clean_button.pack(side=tk.LEFT, padx=5)
        
        # Barra de búsqueda
        search_frame = tk.Frame(main_frame, bg='#2b2b2b')
        search_frame.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(
            search_frame,
            text="Buscar:",
            bg='#2b2b2b',
            fg='white',
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        self.search_var = tk.StringVar()
        self.search_var.trace('w', self.filter_programs)
        
        search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Arial", 10),
            bg='#3c3c3c',
            fg='white',
            insertbackground='white',
            relief=tk.FLAT
        )
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=5)
        
        # Frame para la lista de programas
        list_frame = tk.Frame(main_frame, bg='#2b2b2b')
        list_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Scrollbar
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Listbox para programas
        self.program_listbox = tk.Listbox(
            list_frame,
            yscrollcommand=scrollbar.set,
            font=("Consolas", 9),
            bg='#1e1e1e',
            fg='#ffffff',
            selectbackground='#0078d4',
            selectforeground='white',
            relief=tk.FLAT,
            highlightthickness=0
        )
        self.program_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.program_listbox.yview)
        
        self.program_listbox.bind('<<ListboxSelect>>', self.on_program_select)
        
        # Frame de información
        info_frame = tk.LabelFrame(
            main_frame,
            text="Información del Programa",
            bg='#2b2b2b',
            fg='white',
            font=("Arial", 10, "bold")
        )
        info_frame.pack(fill=tk.BOTH, expand=True)
        
        self.info_text = scrolledtext.ScrolledText(
            info_frame,
            height=8,
            font=("Consolas", 9),
            bg='#1e1e1e',
            fg='#00ff00',
            relief=tk.FLAT,
            wrap=tk.WORD
        )
        self.info_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Barra de estado
        self.status_label = tk.Label(
            self.root,
            text="Listo. Presiona 'Escanear Programas' para comenzar.",
            bg='#1e1e1e',
            fg='#00ff00',
            font=("Arial", 9),
            anchor=tk.W,
            padx=10,
            pady=5
        )
        self.status_label.pack(side=tk.BOTTOM, fill=tk.X)
        
    def scan_programs(self):
        """Escanea todos los programas instalados en Windows"""
        self.status_label.config(text="Escaneando programas instalados...")
        self.scan_button.config(state=tk.DISABLED)
        self.program_listbox.delete(0, tk.END)
        self.programs = []
        
        def scan_thread():
            try:
                # Rutas del registro donde se almacenan programas instalados
                registry_paths = [
                    (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
                    (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
                    (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
                ]
                
                for hkey, path in registry_paths:
                    try:
                        key = winreg.OpenKey(hkey, path)
                        i = 0
                        while True:
                            try:
                                subkey_name = winreg.EnumKey(key, i)
                                subkey = winreg.OpenKey(key, subkey_name)
                                
                                try:
                                    name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                                    
                                    # Obtener información adicional
                                    try:
                                        version = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                                    except:
                                        version = "N/A"
                                    
                                    try:
                                        publisher = winreg.QueryValueEx(subkey, "Publisher")[0]
                                    except:
                                        publisher = "N/A"
                                    
                                    try:
                                        install_location = winreg.QueryValueEx(subkey, "InstallLocation")[0]
                                    except:
                                        install_location = "N/A"
                                    
                                    try:
                                        uninstall_string = winreg.QueryValueEx(subkey, "UninstallString")[0]
                                    except:
                                        uninstall_string = "N/A"
                                    
                                    program_info = {
                                        'name': name,
                                        'version': version,
                                        'publisher': publisher,
                                        'install_location': install_location,
                                        'uninstall_string': uninstall_string,
                                        'registry_key': f"{path}\\{subkey_name}",
                                        'hkey': hkey
                                    }
                                    
                                    self.programs.append(program_info)
                                    
                                except:
                                    pass
                                finally:
                                    winreg.CloseKey(subkey)
                                
                                i += 1
                            except OSError:
                                break
                        
                        winreg.CloseKey(key)
                    except:
                        pass
                
                # Ordenar programas alfabéticamente
                self.programs.sort(key=lambda x: x['name'].lower())
                
                # Mostrar en la lista
                self.root.after(0, self.display_programs)
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    "Error",
                    f"Error al escanear programas: {str(e)}"
                ))
            finally:
                self.root.after(0, lambda: self.scan_button.config(state=tk.NORMAL))
                self.root.after(0, lambda: self.status_label.config(
                    text=f"Escaneo completado. {len(self.programs)} programas encontrados."
                ))
        
        thread = threading.Thread(target=scan_thread, daemon=True)
        thread.start()
    
    def display_programs(self):
        """Muestra los programas en el listbox"""
        self.program_listbox.delete(0, tk.END)
        search_term = self.search_var.get().lower()
        
        for program in self.programs:
            if search_term in program['name'].lower():
                display_text = f"{program['name']} - v{program['version']} ({program['publisher']})"
                self.program_listbox.insert(tk.END, display_text)
    
    def filter_programs(self, *args):
        """Filtra programas según la búsqueda"""
        self.display_programs()
    
    def on_program_select(self, event):
        """Cuando se selecciona un programa"""
        selection = self.program_listbox.curselection()
        if selection:
            index = selection[0]
            search_term = self.search_var.get().lower()
            
            # Encontrar el programa correcto
            filtered_programs = [p for p in self.programs if search_term in p['name'].lower()]
            
            if index < len(filtered_programs):
                self.selected_program = filtered_programs[index]
                self.show_program_info()
                self.uninstall_button.config(state=tk.NORMAL)
                self.deep_clean_button.config(state=tk.NORMAL)
    
    def show_program_info(self):
        """Muestra información del programa seleccionado"""
        if not self.selected_program:
            return
        
        self.info_text.delete(1.0, tk.END)
        
        info = f"""
╔══════════════════════════════════════════════════════════════════════════════╗
  INFORMACIÓN DEL PROGRAMA
╚══════════════════════════════════════════════════════════════════════════════╝

📦 Nombre:           {self.selected_program['name']}
📌 Versión:          {self.selected_program['version']}
🏢 Editor:           {self.selected_program['publisher']}
📂 Ubicación:        {self.selected_program['install_location']}
🔧 Desinstalador:    {self.selected_program['uninstall_string']}
🗝️  Registro:         {self.selected_program['registry_key']}

╔══════════════════════════════════════════════════════════════════════════════╗
  ACCIONES DISPONIBLES
╚══════════════════════════════════════════════════════════════════════════════╝

🗑️  Desinstalar:      Ejecuta el desinstalador oficial del programa
🧹 Limpieza Profunda: Elimina archivos residuales y entradas del registro
        """
        
        self.info_text.insert(1.0, info)
    
    def uninstall_program(self):
        """Desinstala el programa seleccionado"""
        if not self.selected_program:
            messagebox.showwarning("Advertencia", "Por favor selecciona un programa primero.")
            return
        
        program_name = self.selected_program['name']
        
        response = messagebox.askyesno(
            "Confirmar Desinstalación",
            f"¿Estás seguro de que deseas desinstalar '{program_name}'?\n\n"
            "Esta acción ejecutará el desinstalador oficial del programa."
        )
        
        if not response:
            return
        
        self.status_label.config(text=f"Desinstalando {program_name}...")
        
        def uninstall_thread():
            try:
                uninstall_string = self.selected_program['uninstall_string']
                
                if uninstall_string and uninstall_string != "N/A":
                    # Ejecutar el desinstalador
                    subprocess.run(uninstall_string, shell=True)
                    
                    self.root.after(0, lambda: messagebox.showinfo(
                        "Desinstalación Iniciada",
                        f"Se ha iniciado el desinstalador de '{program_name}'.\n\n"
                        "Sigue las instrucciones del asistente de desinstalación."
                    ))
                else:
                    self.root.after(0, lambda: messagebox.showwarning(
                        "No Disponible",
                        f"No se encontró un desinstalador para '{program_name}'.\n\n"
                        "Prueba con la opción de 'Limpieza Profunda'."
                    ))
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    "Error",
                    f"Error al desinstalar: {str(e)}"
                ))
            finally:
                self.root.after(0, lambda: self.status_label.config(text="Listo."))
        
        thread = threading.Thread(target=uninstall_thread, daemon=True)
        thread.start()
    
    def deep_clean(self):
        """Limpieza profunda: elimina archivos y entradas de registro"""
        if not self.selected_program:
            messagebox.showwarning("Advertencia", "Por favor selecciona un programa primero.")
            return
        
        program_name = self.selected_program['name']
        install_location = self.selected_program['install_location']
        
        response = messagebox.askyesno(
            "⚠️ ADVERTENCIA - Limpieza Profunda",
            f"¿Estás seguro de realizar una LIMPIEZA PROFUNDA de '{program_name}'?\n\n"
            "Esta acción:\n"
            "✓ Eliminará TODOS los archivos del programa\n"
            "✓ Eliminará entradas del registro\n"
            "✓ Borrará carpetas residuales\n\n"
            "⚠️ ESTA ACCIÓN NO SE PUEDE DESHACER ⚠️\n\n"
            "¿Continuar?",
            icon='warning'
        )
        
        if not response:
            return
        
        self.status_label.config(text=f"Realizando limpieza profunda de {program_name}...")
        
        def deep_clean_thread():
            results = []
            
            try:
                # 1. Eliminar carpeta de instalación
                if install_location and install_location != "N/A" and os.path.exists(install_location):
                    try:
                        shutil.rmtree(install_location)
                        results.append(f"✓ Carpeta eliminada: {install_location}")
                    except Exception as e:
                        results.append(f"✗ Error al eliminar carpeta: {str(e)}")
                
                # 2. Eliminar entrada del registro
                try:
                    hkey = self.selected_program['hkey']
                    registry_key = self.selected_program['registry_key']
                    
                    # Extraer la ruta base y el subkey
                    parts = registry_key.split('\\')
                    base_path = '\\'.join(parts[:-1])
                    subkey_name = parts[-1]
                    
                    key = winreg.OpenKey(hkey, base_path, 0, winreg.KEY_ALL_ACCESS)
                    winreg.DeleteKey(key, subkey_name)
                    winreg.CloseKey(key)
                    results.append(f"✓ Entrada de registro eliminada")
                except Exception as e:
                    results.append(f"✗ Error al eliminar registro: {str(e)}")
                
                # 3. Buscar y eliminar carpetas residuales comunes
                common_paths = [
                    os.path.join(os.getenv('PROGRAMDATA'), program_name),
                    os.path.join(os.getenv('APPDATA'), program_name),
                    os.path.join(os.getenv('LOCALAPPDATA'), program_name),
                ]
                
                for path in common_paths:
                    if os.path.exists(path):
                        try:
                            shutil.rmtree(path)
                            results.append(f"✓ Carpeta residual eliminada: {path}")
                        except Exception as e:
                            results.append(f"✗ Error en {path}: {str(e)}")
                
                # Mostrar resultados
                result_text = "\n".join(results)
                self.root.after(0, lambda: messagebox.showinfo(
                    "Limpieza Profunda Completada",
                    f"Resultados de la limpieza de '{program_name}':\n\n{result_text}"
                ))
                
                # Actualizar lista
                self.root.after(0, self.scan_programs)
                
            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror(
                    "Error",
                    f"Error durante la limpieza profunda: {str(e)}"
                ))
            finally:
                self.root.after(0, lambda: self.status_label.config(text="Limpieza completada."))
        
        thread = threading.Thread(target=deep_clean_thread, daemon=True)
        thread.start()

def main():
    root = tk.Tk()
    app = WindowsUninstaller(root)
    root.mainloop()

if __name__ == "__main__":
    main()
