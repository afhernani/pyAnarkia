#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage
from tkinter.filedialog import askopenfilename
from tkinter.font import Font, nametofont
from ctypes import byref, memset, sizeof, windll, Structure
from ctypes import create_string_buffer, create_unicode_buffer
from ctypes import c_int, c_void_p
from ctypes.wintypes import WORD, DWORD, BYTE, BOOL, LONG, HBITMAP
from traceback import print_exc
from base64 import b64decode
from PIL import Image, ImageDraw, ImageTk
from injector import (OpenProcess, CloseHandle, get_processes_list,
                      inject_library)

# Funciones, constantes y estructuras de la API de Windows.
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
BI_RGB = 0
DIB_RGB_COLORS = 0
QueryFullProcessImageName = windll.kernel32.QueryFullProcessImageNameW
ExtractIconEx = windll.shell32.ExtractIconExW
DestroyIcon = windll.user32.DestroyIcon
GetIconInfo = windll.user32.GetIconInfo
GetDC = windll.user32.GetDC
ReleaseDC = windll.user32.ReleaseDC
DeleteDC = windll.gdi32.DeleteDC
SelectObject = windll.gdi32.SelectObject
CreateCompatibleDC = windll.gdi32.CreateCompatibleDC
GetPixel = windll.gdi32.GetPixel
GetDIBits = windll.gdi32.GetDIBits
# Imagen por defecto para procesos sin íconos, codificada vía base64
# para distribuir sin dependencias.
PROCESS_DEFAULT_ICON = b64decode(b'''\
iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAGXRFWHRTb2Z0d2FyZQBBZG9\
iZSBJbWFnZVJlYWR5ccllPAAAAsVJREFUeNpcU91LFFEU/83Ox864u64flfaBlFGgCRERYQ\
k+WBFERdZDf0AQQmAf70Fvvkg9BIIg9BAUZEqIESVCL0KiiA89GJUgGoruurgzO1937u3cc\
XexBn7Mvff8fuece+45ihACL8Z+47+vi9BH6CQcI6wQZglDhOmHva1VoiIdPH9fddBAeGpa\
Rn/D/iz0pAFVV8FZhNAPkN/cgVvyXxJn4NHt1rWqg8HRX3KdVRQUGg/UwcpkUHI5uFCgJAD\
BiagIpCwVvl3E5kYBpGt9cuf4ckIqORcSz+obs0gYaRSKERyPw3YZLuz7A7vEUKJ9wWYQWg\
oyCPEfS23sIOLoonT7VTNN5AhnG7dQp7mIGIdlWoiIkKV9RzZHjhmgp5C0zAcDb3/e2s1Ai\
L7a+lrsUGTPZ1jKp3HxaICmFINu6PG/s8XH0lYKnhsRj0HypU7bzUB0R9ARhBEYRVvdVjAj\
TPS0KbAMA90nGD59t5BzFBlO3h9hUpe6zoqDw2FIBRMMd0/bMEhkmmYMVVWh6wy9Zzz4voc\
gCPBmIQ0/0CCAdOyAR1gPQ9bs+gKv52ri9zzSwHHzXAIZQ4MfAhOLAqt5SdfiLKJIgIXCLR\
dRTIeBT6nRm9MVmjMRLrUreDdTpOqHGPtWxJVTCTSleWznPAEWeLGu4mDYsW2oWiKueMfBC\
B/mAqzlQiqqh+WNAJMLPjoOsdiuahpKjiN1I5VX+Oo47ghnJSQ0C5OLCta3ZTQqVhDG/5VN\
jo90Lu3gHopFZ3zgXtt4pQ8khvK5bTK60JI1UFQ9rvbQZ486kcd7eS7F+Vwu5lcbqdyJ85T\
eeTK+cu0ctS49rFkDjZpLt9JQqHCekyfx1ihjvGfwfvuX6ixMTU39M4oTP5qvlafxMsGQSR\
KkYPj6yfXxvVxtz7q9AiK1l8fYKNtUwlVCC+EGYb483rN/BRgAM8iDXy98gZ8AAAAASUVOR\
K5CYII=''')


class ICONINFO(Structure):
    _fields_ = [
        ("fIcon", BOOL),
        ("xHotspot", DWORD),
        ("yHotspot", DWORD),
        ("hbmMask", HBITMAP),
        ("hbmColor", HBITMAP)
    ]


class RGBQUAD(Structure):
    _fields_ = [
        ("rgbBlue", BYTE),
        ("rgbGreen", BYTE),
        ("rgbRed", BYTE),
        ("rgbReserved", BYTE),
    ]


class BITMAPINFOHEADER(Structure):
    _fields_ = [
        ("biSize", DWORD),
        ("biWidth", LONG),
        ("biHeight", LONG),
        ("biPlanes", WORD),
        ("biBitCount", WORD),
        ("biCompression", DWORD),
        ("biSizeImage", DWORD),
        ("biXPelsPerMeter", LONG),
        ("biYPelsPerMeter", LONG),
        ("biClrUsed", DWORD),
        ("biClrImportant", DWORD)
    ]


class BITMAPINFO(Structure):
    _fields_ = [
        ("bmiHeader", BITMAPINFOHEADER),
        ("bmiColors", RGBQUAD * 1),
    ]


class Checkbox(ttk.Checkbutton):
    """
    Una implementación más agradable alrededor de ttk.Checkbutton.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.variable = tk.IntVar(self)
        self.configure(variable=self.variable)

    def checked(self):
        return bool(self.variable.get())

    def check(self):
        self.variable.set(1)

    def uncheck(self):
        self.variable.set(0)


class Linkbutton(ttk.Button):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Obtener el nombre de la fuente utilizada para ttk.Label.
        label_font = nametofont("TkDefaultFont").cget("family")
        self.font = Font(family=label_font, size=9)

        # Crear un nuevo estilo.
        style = ttk.Style()
        style.configure(
            "Link.TLabel", foreground="#357fde", font=self.font)

        # Aplicarlo al enlace.
        self.configure(style="Link.TLabel", cursor="hand2")

        # Configurar eventos.
        self.bind("<Enter>", self.on_mouse_enter)
        self.bind("<Leave>", self.on_mouse_leave)

    def on_mouse_enter(self, event):
        # Aplicar subrayado.
        self.font.configure(underline=True)

    def on_mouse_leave(self, event):
        # Quitar subrayado.
        self.font.configure(underline=False)


def bgra_to_rgba(data):
    """Convertir de formato BGRA (Windows) a RGBA (Pillow)."""
    mutable_data = bytearray(data)
    for i in range(0, len(data), 4):
        # Obtener los valores originales de rojo y azul.
        b = data[i]
        r = data[i + 2]
        # Intercambiarlos.
        mutable_data[i] = ord(r)
        mutable_data[i + 2] = ord(b)
    # Convertir nuevamente a un tipo inmutable.
    return bytes(mutable_data)


class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Inyector de DLL")

        self.filename = None
        self.processes = {}
        self.icons = {}

        # Expandir automáticamente los controles.
        main_window.rowconfigure(0, weight=1, minsize=310)
        main_window.columnconfigure(0, weight=1, minsize=455)
        self.grid(row=0, column=0, sticky="nsew")

        self.create_widgets()

    def create_widgets(self):
        """Crear todos los controles."""
        self.lbl_filename = ttk.Label(
            self, text="No se ha seleccionado ningún archivo.")
        self.lbl_filename.grid(
            row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.default_icon = tk.PhotoImage(data=PROCESS_DEFAULT_ICON)

        self.btn_browse = ttk.Button(
            self, text="Examinar", command=self.browse)
        self.btn_browse.grid(
            row=0, column=1, padx=5, pady=5, sticky="nsew")

        self.tree_processes = ttk.Treeview(
            self, columns=("pid",), selectmode=tk.BROWSE)
        self.tree_processes.heading("#0", text="Nombre")
        self.tree_processes.heading("pid", text="PID")
        self.tree_processes.column("pid", width=70, stretch=False)
        self.tree_processes.grid(
            row=1, column=0, columnspan=2, padx=5, sticky="nsew")

        # Crear una barra de deslizamiento para la lista de procesos.
        scrollbar = ttk.Scrollbar(
            self.tree_processes, orient=tk.VERTICAL)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Añadirla.
        self.tree_processes.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tree_processes.yview)

        self.chk_fullpath = Checkbox(self,
                                     text="Ruta completa", command=self.populate_processes_list)
        self.chk_fullpath.check()
        self.chk_fullpath.grid(
            row=2, column=0, padx=5, pady=5, sticky="ew")

        self.lnk_refresh = Linkbutton(self,
                                      text="Actualizar lista", command=self.refresh_processes)
        self.lnk_refresh.grid(
            row=2, column=1, padx=5)

        self.btn_inject = ttk.Button(self,
                                     text="Inyectar", command=self.inject)
        self.btn_inject.grid(
            row=3, column=0, columnspan=2, sticky="ew", pady=5, padx=5)

        # Expansión automática.
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # Obtener los procesos por primera vez.
        self.refresh_processes()

    def inject(self):
        """Determinar que el archivo y el proceso seleccionados sean
        correctos y, en caso afirmativo, proceder con la inyección.
        """
        if not self.filename:
            messagebox.showinfo("Inyector de DLL",
                                "Debes seleccionar un archivo.")
            return

        selection = self.tree_processes.selection()
        if not selection:
            messagebox.showinfo("Inyector de DLL",
                                "Debes seleccionar un proceso de la lista.")
        else:
            item = self.tree_processes.item(selection[0])
            pid = item["values"][0]
            try:
                inject_library(bytes(self.filename, "utf-8"), pid)
            except RuntimeError:
                messagebox.showerror("Operación fallida",
                                     "No se ha podido inyectar el archivo.")
                # Registrar el error completo en un archivo.
                with open("dllinjector.log", "a") as f:
                    print_exc(file=f)
            else:
                messagebox.showinfo("Operación exitosa",
                                    "El archivo ha sido inyectado correctamente.")

    def load_processes(self):
        """Obtener información de los procesos."""
        self.processes = {}

        dc = CreateCompatibleDC(0)
        if dc == 0:
            raise RuntimeError("Failed while creating DC.")

        for proc_name, pid in get_processes_list():
            # Obtener acceso al proceso.
            proc_handle = OpenProcess(
                PROCESS_QUERY_LIMITED_INFORMATION, False, pid
            )

            # Almacenar un objeto para guardar la ruta completa del
            # proceso.
            wbuffer = create_unicode_buffer(500)
            size = c_int(500)

            full_path = QueryFullProcessImageName(
                proc_handle, 0, byref(wbuffer), byref(size)
            )
            # Los archivos del sistema no tienen una ruta completa.
            if full_path:
                proc_name = wbuffer.value
            else:
                proc_name = proc_name.decode("utf-8")

            CloseHandle(proc_handle)

            # Obtener el ícono del proceso.
            icon = c_int(0)
            ExtractIconEx(proc_name, 0, None, byref(icon), 1)

            if icon.value > 0:
                icon_info = ICONINFO(0, 0, 0, 0, 0)

                if GetIconInfo(icon, byref(icon_info)):
                    # Tamaño.
                    w, h = 16, 16

                    bmi = BITMAPINFO()
                    memset(byref(bmi), 0, sizeof(bmi))
                    bmi.bmiHeader.biSize = sizeof(BITMAPINFOHEADER)
                    bmi.bmiHeader.biWidth = w;
                    bmi.bmiHeader.biHeight = -h;
                    bmi.bmiHeader.biPlanes = 1;
                    bmi.bmiHeader.biBitCount = 32;
                    bmi.bmiHeader.biCompression = BI_RGB;
                    bmi.bmiHeader.biSizeImage = w * h * 4;

                    data = create_string_buffer(bmi.bmiHeader.biSizeImage)

                    # ImageTk es utilizado para soportar la transparencia
                    # (el canal Alpha) de los íconos.
                    if GetDIBits(dc, icon_info.hbmColor, 0, h, data,
                                 byref(bmi), DIB_RGB_COLORS):
                        data = bgra_to_rgba(data)
                        image = ImageTk.PhotoImage(
                            Image.frombytes("RGBA", (w, h), data),
                            (w, h)
                        )

                    self.icons[pid] = image

            DestroyIcon(icon)

            self.processes[pid] = proc_name

        DeleteDC(dc)

    def populate_processes_list(self):
        """Cargar los procesos en la lista."""
        # Eliminar los procesos anteriores.
        self.tree_processes.delete(*self.tree_processes.get_children())
        for pid, proc_name in self.processes.items():
            if not self.chk_fullpath.checked():
                backslash = proc_name.rfind("\\")
                if backslash > -1:
                    proc_name = proc_name[backslash + 1:]
            self.tree_processes.insert(
                "",
                tk.END,
                text=proc_name,
                values=(pid,),
                image=self.icons.get(pid, self.default_icon)
            )

    def refresh_processes(self):
        """Actualizar la lista de procesos."""
        self.load_processes()
        self.populate_processes_list()

    def browse(self):
        """Abrir el diálogo para buscar un archivo."""
        filename = askopenfilename(
            filetypes=(("Windows DLL", "*.dll"),))
        if filename:
            self.lbl_filename["text"] = filename
            self.filename = filename


def main():
    main_window = tk.Tk()
    app = Application(main_window)
    app.mainloop()


if __name__ == '__main__':
    main()
