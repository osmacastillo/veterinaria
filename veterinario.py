import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from typing import List, Dict

# Clases para gestión de información
class Propietario:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class Paciente:
    def __init__(self, nombre, especie, raza, edad, propietario):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.propietario = propietario
        self.historial_medico = []

    def actualizar_info(self, nombre, especie, raza, edad, propietario):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.propietario = propietario

    def agregar_registro_medico(self, registro):
        self.historial_medico.append(registro)

class Cita:
    def __init__(self, paciente, fecha, hora, motivo):
        self.paciente = paciente
        self.fecha = fecha
        self.hora = hora
        self.motivo = motivo
        self.detalles = {}

    def agregar_detalle(self, detalle, valor):
        self.detalles[detalle] = valor

class Consulta:
    def __init__(self, cita, diagnostico, tratamiento):
        self.cita = cita
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento

class Medicamento:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

class Inventario:
    def __init__(self):
        self.items = {}

    def agregar_item(self, medicamento):
        self.items[medicamento.nombre] = medicamento

    def actualizar_item(self, nombre, cantidad, precio):
        if nombre in self.items:
            self.items[nombre].cantidad = cantidad
            self.items[nombre].precio = precio

    def alerta_inventario_bajo(self):
        for item, detalles in self.items.items():
            if detalles.cantidad < 10:
                print(f"Alerta: El inventario de {item} está bajo.")

class Reporte:
    def __init__(self):
        self.reportes = []

    def generar_reporte(self, reporte):
        self.reportes.append(reporte)

class ClinicaVeterinaria:
    def __init__(self):
        self.mascotas = []
        self.citas = []
        self.medicamentos = []

    def registrar_mascota(self, nombre, especie, raza, edad, dueno):
        propietario = Propietario(dueno, "", "")  # La información del propietario se puede expandir según sea necesario
        mascota = Paciente(nombre, especie, raza, int(edad), propietario)
        self.mascotas.append(mascota)

    def agendar_cita(self, mascota, fecha, hora, motivo):
        cita = Cita(mascota, fecha, hora, motivo)
        self.citas.append(cita)

    def registrar_medicamento(self, nombre, cantidad, precio):
        medicamento = Medicamento(nombre, int(cantidad), float(precio))
        self.medicamentos.append(medicamento)

    def generar_informe_mascotas(self):
        informe = "Mascotas:\n"
        for mascota in self.mascotas:
            informe += f"Nombre: {mascota.nombre}, Especie: {mascota.especie}, Raza: {mascota.raza}, Edad: {mascota.edad}, Dueño: {mascota.propietario.nombre}\n"
        return informe

    def generar_informe_citas(self):
        informe = "Citas:\n"
        for cita in self.citas:
            informe += f"Mascota: {cita.paciente.nombre}, Fecha: {cita.fecha}, Hora: {cita.hora}, Motivo: {cita.motivo}\n"
        return informe

    def generar_informe_medicamentos(self):
        informe = "Medicamentos:\n"
        for medicamento in self.medicamentos:
            informe += f"Nombre: {medicamento.nombre}, Stock: {medicamento.cantidad}, Precio: {medicamento.precio}\n"
        return informe

class InterfazGrafica:
    def __init__(self, clinica_veterinaria):
        self.clinica_veterinaria = clinica_veterinaria
        self.ventana = tk.Tk()
        self.ventana.title("Sistema de Gestión Clínica Veterinaria")
        self.ventana.configure(bg='lightblue')

        # Crear frame central
        self.frame_central = tk.Frame(self.ventana, bg='lightblue')
        self.frame_central.pack(expand=True)

        # Botones de menú en el centro
        tk.Button(self.frame_central, text="Mascotas", command=self.registrar_mascota, width=20).pack(pady=10)
        tk.Button(self.frame_central, text="Citas", command=self.agendar_cita, width=20).pack(pady=10)
        tk.Button(self.frame_central, text="Medicamentos", command=self.registrar_medicamento, width=20).pack(pady=10)
        tk.Button(self.frame_central, text="Informes", command=self.mostrar_informes, width=20).pack(pady=10)

    def registrar_mascota(self):
        ventana_registro = tk.Toplevel(self.ventana)
        ventana_registro.title("Registrar mascota")
        ventana_registro.configure(bg='lightblue')

        tk.Label(ventana_registro, text="Nombre:", bg='lightblue').grid(row=0, column=0, sticky='e')
        tk.Label(ventana_registro, text="Especie:", bg='lightblue').grid(row=1, column=0, sticky='e')
        tk.Label(ventana_registro, text="Raza:", bg='lightblue').grid(row=2, column=0, sticky='e')
        tk.Label(ventana_registro, text="Edad:", bg='lightblue').grid(row=3, column=0, sticky='e')
        tk.Label(ventana_registro, text="Dueño:", bg='lightblue').grid(row=4, column=0, sticky='e')

        nombre = tk.Entry(ventana_registro)
        especie = tk.Entry(ventana_registro)
        raza = tk.Entry(ventana_registro)
        edad = tk.Entry(ventana_registro)
        dueno = tk.Entry(ventana_registro)

        nombre.grid(row=0, column=1, padx=10, pady=5)
        especie.grid(row=1, column=1, padx=10, pady=5)
        raza.grid(row=2, column=1, padx=10, pady=5)
        edad.grid(row=3, column=1, padx=10, pady=5)
        dueno.grid(row=4, column=1, padx=10, pady=5)

        tk.Button(ventana_registro, text="Registrar", command=lambda: self.clinica_veterinaria.registrar_mascota(nombre.get(), especie.get(), raza.get(), edad.get(), dueno.get())).grid(row=5, column=0, columnspan=2, pady=10)

    def agendar_cita(self):
        ventana_cita = tk.Toplevel(self.ventana)
        ventana_cita.title("Agendar cita")
        ventana_cita.configure(bg='lightblue')

        tk.Label(ventana_cita, text="Mascota:", bg='lightblue').grid(row=0, column=0, sticky='e')
        tk.Label(ventana_cita, text="Fecha (YYYY-MM-DD):", bg='lightblue').grid(row=1, column=0, sticky='e')
        tk.Label(ventana_cita, text="Hora (HH:MM):", bg='lightblue').grid(row=2, column=0, sticky='e')
        tk.Label(ventana_cita, text="Motivo:", bg='lightblue').grid(row=3, column=0, sticky='e')

        nombre_mascota = tk.Entry(ventana_cita)
        fecha = tk.Entry(ventana_cita)
        hora = tk.Entry(ventana_cita)
        motivo = tk.Entry(ventana_cita)

        nombre_mascota.grid(row=0, column=1, padx=10, pady=5)
        fecha.grid(row=1, column=1, padx=10, pady=5)
        hora.grid(row=2, column=1, padx=10, pady=5)
        motivo.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(ventana_cita, text="Agendar", command=lambda: self.agendar_cita_action(nombre_mascota.get(), fecha.get(), hora.get(), motivo.get())).grid(row=4, column=0, columnspan=2, pady=10)

    def agendar_cita_action(self, nombre_mascota, fecha, hora, motivo):
        mascota_encontrada = None
        for mascota in self.clinica_veterinaria.mascotas:
            if mascota.nombre == nombre_mascota:
                mascota_encontrada = mascota
                break
        if mascota_encontrada:
            self.clinica_veterinaria.agendar_cita(mascota_encontrada, fecha, hora, motivo)
            messagebox.showinfo("Éxito", "Cita agendada correctamente.")
        else:
            messagebox.showerror("Error", "Mascota no encontrada.")

    def registrar_medicamento(self):
        ventana_medicamento = tk.Toplevel(self.ventana)
        ventana_medicamento.title("Registrar medicamento")
        ventana_medicamento.configure(bg='lightblue')

        tk.Label(ventana_medicamento, text="Nombre:", bg='lightblue').grid(row=0, column=0, sticky='e')
        tk.Label(ventana_medicamento, text="Cantidad:", bg='lightblue').grid(row=1, column=0, sticky='e')
        tk.Label(ventana_medicamento, text="Precio:", bg='lightblue').grid(row=2, column=0, sticky='e')

        nombre = tk.Entry(ventana_medicamento)
        cantidad = tk.Entry(ventana_medicamento)
        precio = tk.Entry(ventana_medicamento)

        nombre.grid(row=0, column=1, padx=10, pady=5)
        cantidad.grid(row=1, column=1, padx=10, pady=5)
        precio.grid(row=2, column=1, padx=10, pady=5)

        tk.Button(ventana_medicamento, text="Registrar", command=lambda: self.clinica_veterinaria.registrar_medicamento(nombre.get(), cantidad.get(), precio.get())).grid(row=3, column=0, columnspan=2, pady=10)

    def mostrar_informes(self):
        ventana_informes = tk.Toplevel(self.ventana)
        ventana_informes.title("Informes")
        ventana_informes.configure(bg='lightblue')

        tk.Button(ventana_informes, text="Informe de Mascotas", command=lambda: messagebox.showinfo("Informe mascotas", self.clinica_veterinaria.generar_informe_mascotas()), width=40).pack(pady=10)
        tk.Button(ventana_informes, text="Informe de Citas", command=lambda: messagebox.showinfo("Informe citas", self.clinica_veterinaria.generar_informe_citas()), width=40).pack(pady=10)
        tk.Button(ventana_informes, text="Informe de Medicamentos", command=lambda: messagebox.showinfo("Informe medicamentos", self.clinica_veterinaria.generar_informe_medicamentos()), width=40).pack(pady=10)

def main():
    clinica = ClinicaVeterinaria()
    interfaz = InterfazGrafica(clinica)
    interfaz.ventana.mainloop()

if __name__ == "__main__":
    main()
