from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt
from config.app import App
from controller.function import GenerateCustomReport, Gestionpostal, GetDataSourceProductos, IngestDataProducts
from controller.report import GenerateReportVentas
from modelos.model import *



def menu(app: App):
    console = Console()
    
    while True:
        try:
            menu_text = Text()
            menu_text.append("\n📊 [bold cyan]Proyecto Datux[/bold cyan]\n", style="underline bold")
            menu_text.append("\n[1] 🟢 Cargar Información\n", style="green")
            menu_text.append("[2] 📈 Informe de Ventas\n", style="blue")
            menu_text.append("[3] 📝 Generar Reporte\n", style="magenta")
            menu_text.append("[4] 📊 Adminstración del Postall\n", style="cyan")
            menu_text.append("[5] 📦 Cargar Productos\n", style="yellow")
            menu_text.append("[6] ❌ Salir\n", style="red")

            console.print(Panel(menu_text, title="🚀 [bold magenta]Menú Principal[/bold magenta]", expand=False, border_style="yellow"))

            opcion = Prompt.ask("[bold yellow]Selecciona una opción[/bold yellow]", choices=["1", "2", "3", "4", "5", "6"])

            if opcion == "1":
                console.print("[green]⏳ Iniciando la ingesta de datos...[/green]")
                IngestDataProducts(app)
                console.print("[green]✅ Ingesta de datos completada.....[/green]")
            elif opcion == "2":
                console.print("[blue]📊 Generando reporte de ventas...[/blue]")
                GenerateReportVentas(app)
                console.print("[blue]✅ Reporte de ventas generado con éxito....[/blue]")
            elif opcion == "3":
                console.print("[magenta]📝Generando Reporte Personalizado...[/magenta]")
                GenerateCustomReport(app)
            elif opcion == "4":
                console.print("[cyan]📊 Ingesta Datos del Postal....[/cyan]")
                Gestionpostal(app)
            elif opcion == "5":
                console.print("[yellow]📦 Generando Productos.......[/yellow]")
                GetDataSourceProductos(app)
            elif opcion == "6":
                console.print("[red]❌ Saliendo del programa..... ¡Hasta luego![/red]")
                break
        except Exception as e:
            console.print(f"[red]❌ Error inesperado: {e}[/red]")
            if opcion == "1":
                console.print("[green]⏳ Iniciando la carga de información...[/green]")
                IngestDataProducts(app)
                console.print("[green]✅ Carga de información completada.....[/green]")
            elif opcion == "2":
                console.print("[blue]📊 Generando informe de ventas...[/blue]")
                GenerateReportVentas(app)
                console.print("[blue]✅ Informe de ventas generado con éxito....[/blue]")
            elif opcion == "3":
                console.print("[magenta]📝 Generando Reporte...[/magenta]")
                GenerateCustomReport(app)
            elif opcion == "4":
                console.print("[cyan]📊 Administración de datos postales....[/cyan]")
                Gestionpostal(app)
            elif opcion == "5":
                console.print("[yellow]📦 Cargando información de productos.......[/yellow]")
                GetDataSourceProductos(app)
            elif opcion == "6":
                console.print("[red]❌ Saliendo del programa..... ¡Hasta luego![/red]")
                break
        except Exception as e:
            console.print(f"[red]❌ Error inesperado: {e}[/red]")