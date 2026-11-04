import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class p141_Archivo6 {
    static Scanner sc = new Scanner(System.in);
    static ArrayList<String> datos = new ArrayList<>();
    static String archivo = "nombres.dat";

    // Método para capturar datos en la lista en memoria
    static void capturar() {
        System.out.println("\nEscribe datos (<Enter> vacío para terminar):");
        String linea;
        while (!(linea = sc.nextLine()).isEmpty()) {
            datos.add(linea);
        }
    }

    // Método para guardar el tamaño de la lista y luego sus elementos
    static void grabar() {
        if (datos.isEmpty()) {
            System.out.println("\nNo hay datos para grabar.");
            return;
        }
        try (DataOutputStream dos = new DataOutputStream(new FileOutputStream(archivo))) {
            dos.writeInt(datos.size()); // Primero guardamos cuántos elementos son
            for (String d : datos) {
                dos.writeUTF(d);        // Guardamos cada cadena
            }
            System.out.println("\nDatos grabados con éxito.");
        } catch (IOException e) {
            System.out.println("\nError al grabar: " + e.getMessage());
        }
    }

    // Método para leer la cantidad exacta de registros y reconstruir la lista
    static void leer() {
        try (DataInputStream dis = new DataInputStream(new FileInputStream(archivo))) {
            datos.clear();
            int total = dis.readInt(); // Leemos la cantidad inicial
            for (int i = 0; i < total; i++) {
                datos.add(dis.readUTF());
            }
            System.out.println("\nDatos cargados con éxito.");
        } catch (IOException e) {
            System.out.println("\nError al leer archivo: " + e.getMessage());
        }
    }

    // Método para mostrar lo que hay actualmente en la lista en memoria
    static void mostrar() {
        if (datos.isEmpty()) {
            System.out.println("\nNo hay datos para mostrar.");
            return;
        }
        System.out.println("\nDatos registrados:");
        for (String d : datos) {
            System.out.println("- " + d);
        }
    }

    public static void main(String[] args) {
        int op;
        do {
            // Limpieza de pantalla en consolas compatibles (ANSI)
            System.out.print("\033[H\033[2J");
            System.out.print("""
                \n--- Procesamiento de datos ---
                [1] Capturar datos
                [2] Grabar en archivo
                [3] Leer de archivo
                [4] Mostrar datos
                [5] Salir
                Elige una opción:\s""");
            
            op = sc.nextInt();
            sc.nextLine(); // Limpiar el buffer del Scanner
            
            switch (op) {
                case 1 -> capturar();
                case 2 -> grabar();
                case 3 -> leer();
                case 4 -> mostrar();
                case 5 -> System.out.println("\nSaliendo...");
                default -> System.out.println("\nOpción no válida.");
            }
            
            System.out.print("\nPresione <Enter> para continuar...");
            sc.nextLine();
            
        } while (op != 5);
    }
}
