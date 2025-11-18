/*
    Archivo: BinaryInsertionSort.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Implementación del método de ordenamiento por Inserción Binaria.
*/

namespace MetodosOrdenamiento
{
    public static class BinaryInsertionSort
    {
        public static void Sort(int[] a)
        {
            // Empezamos desde el segundo elemento
            for (int i = 1; i < a.Length; i++)
            {
                int x = a[i];        // Elemento que vamos a insertar
                int izq = 0;         // Límite izquierdo de la búsqueda binaria
                int der = i - 1;     // Límite derecho de la búsqueda binaria

                // Búsqueda binaria para encontrar la posición correcta de x
                while (izq <= der)
                {
                    int mid = (izq + der) / 2; // Punto medio

                    if (a[mid] > x)
                        der = mid - 1; // Buscamos en la mitad izquierda
                    else
                        izq = mid + 1; // Buscamos en la mitad derecha
                }

                // Movemos los elementos a la derecha para hacer espacio a x
                for (int j = i - 1; j >= izq; j--)
                {
                    a[j + 1] = a[j];
                }

                // Insertamos x en la posición encontrada
                a[izq] = x;
            }
        }
    }
}
