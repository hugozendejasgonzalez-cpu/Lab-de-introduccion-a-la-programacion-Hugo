import java.io.File;

public class p136_Archivos1 {
    public static void main(String[] args) {
        File arch = new File("datos.txt");
        if(arch.exists()) {
            System.out.println("Nombre archivo : " + arch.getName() );
            System.out.println("Es directorio : " + arch.isDirectory() );
            System.out.println("Ruta relativa : " + arch.getPath() );
            System.out.println("Ruta absoluta : " + arch.getAbsolutePath() );
            System.out.println("El archivo existe !!");
            System.out.println("Se puede leer : " + arch.canRead() );
            System.out.println("Se puede escribir : " + arch.canWrite() );
            System.out.println("Longitud archivo : " + arch.length() );
            System.out.println("Última modificación (ms) : " + arch.lastModified() );
        } else {
            System.out.println("El archivo no existe !!");
        }
    }
}
