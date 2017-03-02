/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package practica2_edd;

import javax.swing.JOptionPane;
import javax.swing.UIManager;
import de.javasoft.plaf.synthetica.SyntheticaBlueLightLookAndFeel;

/**
 *
 * @author TOSHIBA P55
 */
public class Practica2_EDD {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
            try
            {     UIManager.setLookAndFeel (new SyntheticaBlueLightLookAndFeel ());
        }
        catch (Exception ex)
                {
                JOptionPane.showMessageDialog(null, "Error en Look And Feel", 
                        "Error:" + ex.getMessage(), JOptionPane.ERROR_MESSAGE);
                        
        }
      
      
        
    }
}
