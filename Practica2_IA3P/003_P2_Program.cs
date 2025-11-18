/*
    Archivo: Program.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Archivo principal del proyecto. Aquí inicia la aplicación
    y se abre el formulario Burbuja.
*/

using System;
using System.Windows.Forms;

namespace MetodosOrdenamiento
{
    internal static class Program
    {
        [STAThread] // Indica que la app usa el modelo de un solo hilo para Windows Forms
        static void Main()
        {
            Application.EnableVisualStyles();               // Activa estilos visuales modernos
            Application.SetCompatibleTextRenderingDefault(false); 
            Application.Run(new Burbuja());                // Inicia el formulario principal
        }
    }
}
