/*
    Archivo: SelectionSort.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Implementación del método de ordenamiento por Selección Directa.
*/

namespace MetodosOrdenamiento
{
    public static class SelectionSort
    {
        // Método que ordena un arreglo de enteros usando Selección Directa
        public static void Sort(int[] a)
        {
            int n = a.Length; // Guardamos la cantidad de elementos del arreglo

            // Recorremos el arreglo hasta el penúltimo elemento
            for (int i = 0; i < n - 1; i++)
            {
                int minIndex = i; // Suponemos que el mínimo está en la posición i

                // Buscamos el índice del menor elemento en la parte no ordenada
                for (int j = i + 1; j < n; j++)
                {
                    // Si encontramos un elemento más pequeño, actualizamos minIndex
                    if (a[j] < a[minIndex])
                    {
                        minIndex = j;
                    }
                }

                // Si el mínimo no está en la posición i, intercambiamos
                if (minIndex != i)
                {
                    int aux = a[i];     // Guardamos temporalmente el valor en i
                    a[i] = a[minIndex]; // Ponemos el mínimo en la posición i
                    a[minIndex] = aux;  // El valor original de i lo movemos a minIndex
                }
            }
        }
    }
}
