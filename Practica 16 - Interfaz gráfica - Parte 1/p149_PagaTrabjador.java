import javax.swing.*;
import java.awt.event.*;
import java.util.Locale;

public class p149_PagaTrabjador extends JFrame implements ActionListener {
    private JLabel lblHoras, lblPagaHora, lblTasa, lblBruta, lblImpuesto, lblNeta;
    private JTextField txtHoras, txtPagaHora, txtTasa, txtBruta, txtImpuesto, txtNeta;
    private JButton btnCalcular, btnSalir;

    public p149_PagaTrabjador() {
        super("Calcular Paga de Trabajador");
        setLayout(null);

        lblHoras = new JLabel("Horas Trabajadas:", SwingConstants.RIGHT);
        lblHoras.setBounds(20, 20, 140, 25);
        add(lblHoras);

        lblPagaHora = new JLabel("Paga por Hora:", SwingConstants.RIGHT);
        lblPagaHora.setBounds(20, 55, 140, 25);
        add(lblPagaHora);

        lblTasa = new JLabel("Tasa de Impuestos (%):", SwingConstants.RIGHT);
        lblTasa.setBounds(20, 90, 140, 25);
        add(lblTasa);

        lblBruta = new JLabel("Paga Bruta:", SwingConstants.RIGHT);
        lblBruta.setBounds(20, 125, 140, 25);
        add(lblBruta);

        lblImpuesto = new JLabel("Impuesto:", SwingConstants.RIGHT);
        lblImpuesto.setBounds(20, 160, 140, 25);
        add(lblImpuesto);

        lblNeta = new JLabel("Paga Neta:", SwingConstants.RIGHT);
        lblNeta.setBounds(20, 195, 140, 25);
        add(lblNeta);

        txtHoras = new JTextField();
        txtHoras.setBounds(170, 20, 120, 25);
        add(txtHoras);

        txtPagaHora = new JTextField();
        txtPagaHora.setBounds(170, 55, 120, 25);
        add(txtPagaHora);

        txtTasa = new JTextField();
        txtTasa.setBounds(170, 90, 120, 25);
        add(txtTasa);

        txtBruta = new JTextField();
        txtBruta.setBounds(170, 125, 120, 25);
        txtBruta.setEditable(false);
        add(txtBruta);

        txtImpuesto = new JTextField();
        txtImpuesto.setBounds(170, 160, 120, 25);
        txtImpuesto.setEditable(false);
        add(txtImpuesto);

        txtNeta = new JTextField();
        txtNeta.setBounds(170, 195, 120, 25);
        txtNeta.setEditable(false);
        add(txtNeta);

        btnCalcular = new JButton("Calcular");
        btnCalcular.setBounds(70, 235, 90, 28);
        btnCalcular.addActionListener(this);
        add(btnCalcular);

        btnSalir = new JButton("Salir");
        btnSalir.setBounds(170, 235, 90, 28);
        btnSalir.addActionListener(this);
        add(btnSalir);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == btnCalcular) {
            try {
                double horas = Double.parseDouble(txtHoras.getText());
                double pagaHora = Double.parseDouble(txtPagaHora.getText());
                double tasa = Double.parseDouble(txtTasa.getText());

                double pagaBruta = horas * pagaHora;
                double impuesto = pagaBruta * (tasa / 100.0);
                double pagaNeta = pagaBruta - impuesto;

                txtBruta.setText(String.format(Locale.US, "%.2f", pagaBruta));
                txtImpuesto.setText(String.format(Locale.US, "%.2f", impuesto));
                txtNeta.setText(String.format(Locale.US, "%.2f", pagaNeta));
            } catch (NumberFormatException ex) {
                JOptionPane.showMessageDialog(this, "Por favor, ingresa valores numéricos válidos.", "Error", JOptionPane.ERROR_MESSAGE);
            }
        } else if (e.getSource() == btnSalir) {
            dispose();
        }
    }

    public static void main(String[] args) {
        p149_PagaTrabjador ventana = new p149_PagaTrabjador();
        ventana.setSize(330, 320);
        ventana.setLocationRelativeTo(null);
        ventana.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        ventana.setVisible(true);
    }
}
