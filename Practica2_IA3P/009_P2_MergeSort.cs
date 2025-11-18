/*
    Archivo: MergeSort.cs
    Autor: Rodrigo Lagos Navarro
    Cuenta: 23110148
    Grupo: 6E

    Descripción:
    Implementación del método de ordenamiento MergeSort (Ordenación por mezcla).
*/

using System;

namespace MetodosOrdenamiento
{
    public static class MergeSort
    {
        // Método público que inicia el MergeSort
        public static void Sort(int[] a)
        {
            if (a.Length <= 1) return;       // Si el arreglo tiene 0 o 1 elemento, ya está ordenado
            MergeSortRec(a, 0, a.Length - 1); // Llamamos al método recursivo
        }

        // Método recursivo que divide el arreglo y luego mezcla ordenadamente
        private static void MergeSortRec(int[] a, int izquierda, int derecha)
        {
            if (izquierda >= derecha) return; // Caso base

            int medio = (izquierda + derecha) / 2; // Calculamos el punto medio

            // Ordenamos recursivamente la mitad izquierda
            MergeSortRec(a, izquierda, medio);

            // Ordenamos recursivamente la mitad derecha
            MergeSortRec(a, medio + 1, derecha);

            // Mezclamos las dos mitades ya ordenadas
            Merge(a, izquierda, medio, derecha);
        }

        // Mezcla ordenadamente los subarreglos [izquierda..medio] y [medio+1..derecha]
        private static void Merge(int[] a, int izquierda, int medio, int derecha)
        {
            int n1 = medio - izquierda + 1; // Tamaño del subarreglo izquierdo
            int n2 = derecha - medio;       // Tamaño del subarreglo derecho

            int[] L = new int[n1];          // Arreglo temporal izquierdo
            int[] R = new int[n2];          // Arreglo temporal derecho

            // Copiamos los datos al arreglo izquierdo L
            Array.Copy(a, izquierda, L, 0, n1);

            // Copiamos los datos al arreglo derecho R
            Array.Copy(a, medio + 1, R, 0, n2);

            int i = 0, j = 0, k = izquierda; // i -> índice L, j -> índice R, k -> índice a

            // Mezclamos mientras haya elementos en ambos arreglos
            while (i < n1 && j < n2)
            {
                if (L[i] <= R[j])
                {
                    a[k] = L[i]; // El menor va a la posición k del arreglo original
                    i++;
                }
                else
                {
                    a[k] = R[j];
                    j++;
                }

                k++; // Avanzamos en el arreglo original
            }

            // Copiamos los elementos restantes de L, si los hay
            while (i < n1)
            {
                a[k] = L[i];
                i++;
                k++;
            }

            // Copiamos los elementos restantes de R, si los hay
            while (j < n2)
            {
                a[k] = R[j];
                j++;
                k++;
            }
        }
    }
}
