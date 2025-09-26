import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.popup import Popup

from src.model.calculadora_impuestos import CalculadoraImpuestos, CategoriaProducto


class ImpuestosLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 10

        self.add_widget(Label(text="Ingrese el precio del producto:"))
        self.precio_input = TextInput(multiline=False, input_filter="float")
        self.add_widget(self.precio_input)

        self.add_widget(Label(text="Seleccione la categoría del producto:"))
        self.categoria_spinner = Spinner(
            text="Seleccione",
            values=(
                "Alimentos Básicos",
                "Licores",
                "Bolsas Plásticas",
                "Combustibles",
                "Servicios Públicos",
                "Otros",
            ),
        )
        self.add_widget(self.categoria_spinner)

        calcular_btn = Button(text="Calcular impuestos")
        calcular_btn.bind(on_press=self.calcular_impuestos)
        self.add_widget(calcular_btn)

    def calcular_impuestos(self, instance):
        try:
            precio = float(self.precio_input.text)
            categoria_text = self.categoria_spinner.text

            if categoria_text == "Seleccione":
                raise ValueError("Debe seleccionar una categoría")

            categoria = None
            for cat in CategoriaProducto:
                if cat.value == categoria_text:
                    categoria = cat
                    break

            if categoria is None:
                raise ValueError(f"Categoría inválida: {categoria_text}")

            calculadora = CalculadoraImpuestos()
            resultado = calculadora.calcular_impuestos(precio, categoria)

            mensaje = f"Precio base: {resultado['valor_base']}\n"
            for imp, valor in resultado["impuestos"].items():
                mensaje += f"{imp}: {valor}\n"
            mensaje += f"\nTotal a pagar: {resultado['valor_total']}"

            popup = Popup(
                title="Resultado",
                content=Label(text=mensaje),
                size_hint=(0.8, 0.6)
            )
            popup.open()

        except Exception as e:
            popup = Popup(
                title="Error",
                content=Label(text=str(e)),
                size_hint=(0.8, 0.4)
            )
            popup.open()


class ImpuestosApp(App):
    def build(self):
        return ImpuestosLayout()


if __name__ == "__main__":
    ImpuestosApp().run()
