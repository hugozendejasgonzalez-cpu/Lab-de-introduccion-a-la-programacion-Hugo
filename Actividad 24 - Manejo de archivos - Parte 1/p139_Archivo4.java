import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class p139_Archivo4 {
    public static void main(String[] args) {
        File arch = new File("nombres.txt");
        String[] nombres = { "Juan", "Pedro", "Luis", "María" };
        Scanner entrada = new Scanner(System.in);
        System.out.println("1. Crear archivo");
        System.out.println("2. Leer y mostrar archivo");
        System.out.print("Elige una opción: ");
        int opcion = entrada.nextInt();
        switch (opcion) {
            case 1:
                if (arch.exists()) {
                    System.out.println("El archivo ya existe. No se modifica.");
                } else {
                    try (BufferedWriter salida = new BufferedWriter(new FileWriter(arch))) {
                        for (String nombre : nombres) {
                            salida.write(nombre);
                            salida.newLine(); // Corrección: Salto de línea nativo y multiplataforma
                        }
                        System.out.println("Archivo creado.");
                    } catch (IOException e) {
                        System.out.println(e);
                    }
                }
                break;
            case 2:
                if (!arch.exists()) {
                    System.out.println("Error: el archivo no existe.");
                    break;
                }
                System.out.println("Contenido del archivo:");
                try (BufferedReader entradaArchivo = new BufferedReader(new FileReader(arch))) {
                    String linea;
                    while ((linea = entradaArchivo.readLine()) != null) {
                        System.out.println(linea);
                    }
                } catch (IOException e) {
                    System.out.println(e);
                }
                break;
            default:
                System.out.println("Opción inválida.");
        }
        entrada.close();
    }
}
