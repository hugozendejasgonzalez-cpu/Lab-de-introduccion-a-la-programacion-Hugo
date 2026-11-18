import javax.swing.*;
import java.awt.event.*;
import java.util.Locale;

public class p150_Temperaturas extends JFrame implements ActionListener {
    private JLabel lblFahrenheit, lblCentigrados;
    private JTextField txtFahrenheit, txtCentigrados;
    private JRadioButton rbtCentigrados, rbtFahrenheit;
    private ButtonGroup grupoOpciones;
    private JButton btnCalcular, btnSalir;

    public p150_Temperaturas() {
        super("Convertir Temperaturas");
        setLayout(null);

        lblFahrenheit = new JLabel("Fahrenheit:", SwingConstants.RIGHT);
        lblFahrenheit.setBounds(40, 20, 100, 25);
        add(lblFahrenheit);

        lblCentigrados = new JLabel("Centígrados:", SwingConstants.RIGHT);
        lblCentigrados.setBounds(40, 55, 100, 25);
        add(lblCentigrados);

        txtFahrenheit = new JTextField();
        txtFahrenheit.setBounds(150, 20, 130, 25);
        add(txtFahrenheit);

        txtCentigrados = new JTextField();
        txtCentigrados.setBounds(150, 55, 130, 25);
        txtCentigrados.setEditable(false);
        add(txtCentigrados);

        rbtCentigrados = new JRadioButton("Calcular Centígrados", true);
        rbtCentigrados.setBounds(20, 95, 160, 25);
        rbtCentigrados.addActionListener(this);
        add(rbtCentigrados);

        rbtFahrenheit = new JRadioButton("Calcular Fahrenheit", false);
        rbtFahrenheit.setBounds(185, 95, 160, 25);
        rbtFahrenheit.addActionListener(this);
        add(rbtFahrenheit);

        grupoOpciones = new ButtonGroup();
        grupoOpciones.add(rbtCentigrados);
        grupoOpciones.add(rbtFahrenheit);

        btnCalcular = new JButton("Calcular");
        btnCalcular.setBounds(80, 135, 95, 28);
        btnCalcular.addActionListener(this);
        add(btnCalcular);

        btnSalir = new JButton("Salir");
        btnSalir.setBounds(185, 135, 95, 28);
        btnSalir.addActionListener(this);
        add(btnSalir);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == rbtCentigrados) {
            txtFahrenheit.setEditable(true);
            txtCentigrados.setEditable(false);
            txtFahrenheit.setText("");
            txtCentigrados.setText("");
            txtFahrenheit.requestFocus();
        } else if (e.getSource() == rbtFahrenheit) {
            txtFahrenheit.setEditable(false);
            txtCentigrados.setEditable(true);
            txtFahrenheit.setText("");
            txtCentigrados.setText("");
            txtCentigrados.requestFocus();
        } else if (e.getSource() == btnCalcular) {
            try {
                if (rbtCentigrados.isSelected()) {
                    double f = Double.parseDouble(txtFahrenheit.getText());
                    double c = (f - 32.0) * 5.0 / 9.0;
                    txtCentigrados.setText(String.format(Locale.US, "%.2f", c));
                } else {
                    double c = Double.parseDouble(txtCentigrados.getText());
                    double f = (c * 9.0 / 5.0) + 32.0;
                    txtFahrenheit.setText(String.format(Locale.US, "%.2f", f));
                }
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Por favor, ingresa una temperatura válida.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        } else if (e.getSource() == btnSalir) {
            dispose();
        }
    }

    public static void main(String[] args) {
        p150_Temperaturas ventana = new p150_Temperaturas();
        ventana.setSize(365, 220);
        ventana.setLocationRelativeTo(null);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setVisible(true);
    }
}
