/* 
    Archivo: BubbleSort.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Implementación del método de ordenamiento Burbuja (BubbleSort)
    basado en el código presentado en la guía.
*/

using System;
public static class BubbleSort
{
    public static void Sort(int[] a)
    {
        int n = a.Length;               // Guardamos el tamaño del arreglo

        // Ciclo externo: recorre todo el arreglo
        for (int i = 0; i < n; i++)
        {
            // Ciclo interno: compara pares de elementos consecutivos
            for (int j = 0; j < n - 1; j++)
            {
                // Si el elemento actual es mayor que el siguiente, intercambia
                if (a[j] > a[j + 1])
                {
                    int aux = a[j];     // Guardamos temporalmente el valor actual
                    a[j] = a[j + 1];    // Movemos el menor hacia la izquierda
                    a[j + 1] = aux;     // Colocamos el mayor hacia la derecha
                }
            }
        }
    }
}
