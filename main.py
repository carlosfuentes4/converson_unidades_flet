import flet as ft

class Conversor:
    def __init__(self,page:ft.Page):
        self.page=page

        self.conversion={
            "kilometro": 1000,
            "metros": 1,
            "centimetro": 0.01,
            "milimetro": 0.001,
            "milla": 1609.34,
            "pulgada": 0.0254,
            "pie": 0.3048,
        }

        self._page_setup()
        self._create_component()
        self._build_ui()
        self.page.update()
    
    def _page_setup(self):
       self.page.title="Conversor de unidades"
       self.page.window.width=500
       self.page.window.height=400
       self.page.bgcolor=ft.colors.BLUE_GREY_900
       self.page.update()

    def _create_component(self):
        self.main_label=ft.Row([
            ft.Icon(ft.icons.DESIGN_SERVICES,size=38,color="#ffffff"),
            ft.Text("Convierte las unidades",color="#ffffff",
                    weight=ft.FontWeight.BOLD,
                    size=28)
        ],alignment=ft.MainAxisAlignment.CENTER)

        self.textfield_1=ft.TextField(
            width=140,
            height=40,
            bgcolor="#3B3E3F",
            color=ft.colors.WHITE,
            hint_text="ej. 40",
            border_color="#ffffff",
        )

        self.textfield_2=ft.TextField(
            width=140,
            height=40,
            bgcolor="#3B3E3F",
            color=ft.colors.WHITE,
            hint_text="resultado ",
            border_color="#ffffff"
        )

        self.switch_button=ft.IconButton(
            icon=ft.icons.SWAP_HORIZ,
            on_click=self.switch,
            icon_size=34,
            icon_color="#9EA0E3",
        )
        self.unidades_1=ft.Dropdown(
            label="Unidades iniciales",
            width=140,
            value="metros",
            options=[
                ft.dropdown.Option("kilometro"),
                ft.dropdown.Option("metros"),
                ft.dropdown.Option("centimetro"),
                ft.dropdown.Option("milimetro"),
                ft.dropdown.Option("milla"),
                ft.dropdown.Option("pulgada"),
                ft.dropdown.Option("pie"),
            ]
        )
        self.unidades_2=ft.Dropdown(
            label="Unidade finales",
            width=140,
            value="pulgada",
            options=[
                ft.dropdown.Option("kilometro"),
                ft.dropdown.Option("metros"),
                ft.dropdown.Option("centimetro"),
                ft.dropdown.Option("milimetro"),
                ft.dropdown.Option("milla"),
                ft.dropdown.Option("pulgada"),
                ft.dropdown.Option("pie"),
            ]
        )

        self.convert_button=ft.ElevatedButton(
            content=ft.Row([
                ft.Icon(ft.icons.CALCULATE_OUTLINED,
                size=25,
                color=ft.colors.BLACK
                ),
                ft.Text("Convertir",
                        color=ft.colors.BLACK,
                        size=20
                        )
            ],alignment=ft.MainAxisAlignment.CENTER),
            on_click=self.convertir,
            width=200,
            elevation=7,
            height=50,
            bgcolor=ft.colors.AMBER_700,
            
        )

        self.clean_button=ft.IconButton(
            content=ft.Icon(ft.icons.CLEAR_OUTLINED),
            width=54,
            height=54,
            icon_color=ft.colors.AMBER_900,
            on_click=self.clear,
            alignment=ft.alignment.center,
            icon_size=30
        )
        #prueba
       
    def _build_ui(self):
        card=ft.Column(
            spacing=10,
            controls=[
                self.main_label,
                ft.Container(height=35),
                ft.Row([self.textfield_1,
                        ft.Icon(ft.icons.ARROW_RIGHT_ALT_SHARP,size=40),
                        self.textfield_2],
                       alignment=ft.MainAxisAlignment.CENTER,spacing=4),
                ft.Container(height=10),
                ft.Row([
                    self.unidades_1,
                    self.switch_button,
                    self.unidades_2,
                ],alignment=ft.MainAxisAlignment.CENTER),
                ft.Container(height=28),
                ft.Container(
                    content=ft.Row([self.convert_button,self.clean_button],
                                   alignment=ft.MainAxisAlignment.CENTER),
                    alignment=ft.alignment.center
                )
            ],

        )
        self.page.add(card)
    
    def show_message(self,message):
        dlg=ft.AlertDialog(
            title=ft.Text("Alerta",color="#ffffff"),
            content=ft.Text(message,color="#ffffff"),
            bgcolor=ft.colors.BLACK26,
            actions=[ft.TextButton("OK",on_click=lambda _:self.page.close(dlg))]
        )
        self.page.open(dlg)

    def is_number(self,val1):
        try:
            float(val1)
            return True
        except:
            self.show_message("Solo se aceptan valores numericos")
            return False
        
    def to_inch(self,val,unidad):
        return val*self.conversion[unidad]
    
    def convertir(self,_):
        val1=self.textfield_1.value
        # val2=self.textfield_2.value
        unidad1=self.unidades_1.value
        unidad2=self.unidades_2.value

        if not val1:
            self.show_message("Debes llenar el primer campo")
            return
        
        if self.is_number(val1):
            if float(val1)<=0:
                self.show_message("Los valores deben ser mayores a 0")
                return
            
            try:
                val1= float(val1)
                #procedimiento luego de validaciones
                val1_metros=self.to_inch(val1,unidad1)
                result=val1_metros/self.conversion[unidad2]
                self.textfield_2.value=f"{result:.4f}"
                self.page.update()

            except Exception as e:
                self.show_message(f"error: {e}")

    def switch(self,_):
        # val1=self.textfield_1.value 
        val2=self.textfield_2.value
        unidad1=self.unidades_1.value
        unidad2=self.unidades_2.value

        if not val2:
            self.unidades_1.value=unidad2
            self.unidades_2.value=unidad1
            self.page.update()
            return
        else:
            try:
                self.unidades_1.value=unidad2
                self.unidades_2.value=unidad1
                self.convertir(_=_)
            except Exception as e:
                print(f"error: {e}")

    def clear(self,_):
        self.textfield_1.value=""
        self.textfield_2.value=""
        self.page.update()
        


        

def main(page:ft.Page):
    app=Conversor(page)

if __name__ == "__main__":
    ft.app(target=main)
  
