import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class p137_Archivo2 {
    public static void main(String[] args) {
        String[] nombres = { "Juan", "Pedro", "Luis", "Jose", "Reynaldo", "Maria", "Teresa", "Rocio" };
        File arch = new File("nombres.txt");
        if(arch.exists()) {
            System.out.println("El archivo ya existe !");
        } else {
            try (BufferedWriter fnombres = new BufferedWriter(new FileWriter(arch))) {
                for (String nombre : nombres) {
                    fnombres.write(nombre);
                    fnombres.newLine(); // Corrección: Salto de línea nativo y multiplataforma
                }
            } catch (IOException e) {
                System.out.println("Problemas al procesar el archivo..");
                System.out.println(e);
            }
        }
        System.out.println("Longitud del archivo escrito (bytes) " + arch.length());
    }
}
