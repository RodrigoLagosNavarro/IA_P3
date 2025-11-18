/*
    Archivo: Burbuja.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Formulario Windows Forms que implementa visualmente el método Burbuja:
    dibuja los números como botones y anima cada intercambio.
*/

using System;
using System.Drawing;
using System.Threading;
using System.Windows.Forms;

namespace MetodosOrdenamiento
{
    public partial class Burbuja : Form
    {
        // Objeto donde almacenamos los números que va ingresando el usuario
        private Numeros enteros = new Numeros();

        public Burbuja()
        {
            InitializeComponent();       // Inicializa controles del formulario
            this.Text = "Método Burbuja";
        }

        private void Burbuja_Load(object sender, EventArgs e)
        {
            // Aquí no necesitamos poner nada, pero el evento debe existir.
        }

        // Evento del botón "Agregar"
        private void btnAgregar_Click(object sender, EventArgs e)
        {
            // Intentamos convertir el texto a entero
            if (int.TryParse(txtNumero.Text, out int valor))
            {
                enteros.Agregar(valor); // Agregamos el número
                txtNumero.Clear();      // Borramos el textbox
                txtNumero.Focus();      // Regresamos el foco
                Dibujar_Arreglo();      // Dibujamos los números
            }
            else
            {
                MessageBox.Show("Ingrese un número entero válido.");
            }
        }

        // Evento del botón "Ordenar"
        private void btnOrdenar_Click(object sender, EventArgs e)
        {
            if (enteros.Count <= 1)
            {
                MessageBox.Show("Ingrese al menos dos números.");
                return;
            }

            BubbleSortVisual(); // Llamamos al método visual
        }

        // Dibuja los números como botones en la pantalla
        private void Dibujar_Arreglo()
        {
            tabPage1.Controls.Clear(); // Limpia los controles previos

            int x = 10;
            int y = 20;
            int ancho = 50;
            int alto = 40;
            int espacio = 10;

            // Creamos un botón por cada número
            for (int i = 0; i < enteros.Count; i++)
            {
                Button btn = new Button();
                btn.Width = ancho;
                btn.Height = alto;
                btn.Location = new Point(x, y);
                btn.Text = enteros[i].ToString();
                btn.Enabled = false; // Son solo decorativos
                tabPage1.Controls.Add(btn);

                x += ancho + espacio; // Movemos la posición para el siguiente botón
            }
        }

        // Método burbuja junto con la animación
        private void BubbleSortVisual()
        {
            int n = enteros.Count;

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n - 1; j++)
                {
                    if (enteros[j] > enteros[j + 1])
                    {
                        // Intercambio normal
                        int aux = enteros[j];
                        enteros[j] = enteros[j + 1];
                        enteros[j + 1] = aux;

                        Intercambio(j, j + 1); // Animación del cambio
                    }
                }
            }
        }

        // Muestra el intercambio visualmente
        private void Intercambio(int x, int y)
        {
            Thread.Sleep(200);      // Pausa para ver el cambio
            Dibujar_Arreglo();      // Redibuja los botones
            tabPage1.Refresh();     // Refresca la interfaz
            Application.DoEvents(); // Procesa eventos pendientes
        }
    }
}
