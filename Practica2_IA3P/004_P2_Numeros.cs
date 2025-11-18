/*
    Archivo: Numeros.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Clase auxiliar usada para almacenar los números ingresados 
    y permitir acceder a ellos como si fuera un arreglo dinámico.
*/

using System.Collections.Generic;

namespace MetodosOrdenamiento
{
    public class Numeros
    {
        // Lista interna donde guardamos todos los números
        private readonly List<int> _valores = new List<int>();

        // Propiedad para saber cuántos números hay
        public int Count => _valores.Count;

        // Método para agregar un número a la lista
        public void Agregar(int valor)
        {
            _valores.Add(valor);
        }

        // Indexador para acceder a los números como arreglo: enteros[i]
        public int this[int index]
        {
            get => _valores[index];
            set => _valores[index] = value;
        }

        // Devuelve todos los valores como un arreglo normal int[]
        public int[] AArray()
        {
            return _valores.ToArray();
        }
    }
}
