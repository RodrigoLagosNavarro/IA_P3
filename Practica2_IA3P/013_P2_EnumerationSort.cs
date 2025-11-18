/*
    Archivo: EnumerationSort.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Implementación del método de ordenamiento por Enumeración.
*/

namespace MetodosOrdenamiento
{
    public static class EnumerationSort
    {
        public static void Sort(int[] a)
        {
            int n = a.Length;          // Tamaño del arreglo
            int[] resultado = new int[n]; // Arreglo auxiliar para el resultado

            // Recorremos cada elemento del arreglo
            for (int i = 0; i < n; i++)
            {
                int count = 0; // Contará cuántos elementos son menores que a[i]

                // Comparamos a[i] con todos los demás elementos
                for (int j = 0; j < n; j++)
                {
                    // Si a[j] es menor, o es igual pero su índice es menor, aumentamos count
                    if (a[j] < a[i] || (a[j] == a[i] && j < i))
                    {
                        count++;
                    }
                }

                // La posición final de a[i] es 'count'
                resultado[count] = a[i];
            }

            // Copiamos el resultado ordenado al arreglo original
            for (int i = 0; i < n; i++)
            {
                a[i] = resultado[i];
            }
        }
    }
}
