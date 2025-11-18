/*
    Archivo: ShellSort.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Implementación del método de ordenamiento ShellSort,
    que es una mejora del método de Inserción.
*/

namespace MetodosOrdenamiento
{
    public static class ShellSort
    {
        public static void Sort(int[] a)
        {
            int n = a.Length;   // Tamaño del arreglo
            int gap = n / 2;    // Distancia inicial (gap) entre elementos a comparar

            // Repetimos mientras el gap sea mayor que 0
            while (gap > 0)
            {
                // Recorremos desde gap hasta el final del arreglo
                for (int i = gap; i < n; i++)
                {
                    int temp = a[i]; // Guardamos el valor actual
                    int j = i;       // Empezamos a comparar hacia atrás con saltos de "gap"

                    // Desplazamos hacia adelante los elementos mayores que temp,
                    // usando saltos de "gap"
                    while (j >= gap && a[j - gap] > temp)
                    {
                        a[j] = a[j - gap]; // Corremos el elemento hacia la derecha
                        j -= gap;          // Movemos el índice hacia atrás
                    }

                    // Insertamos el valor en la posición correcta
                    a[j] = temp;
                }

                gap /= 2; // Reducimos el gap a la mitad
            }
        }
    }
}
