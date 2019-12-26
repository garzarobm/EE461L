package observer3;

import javax.swing.*;
import java.awt.*;

public class ComplementaryColorPanel extends ColorPanel implements Observer {

    public ComplementaryColorPanel(Color initialColor) {
    	super(initialColor);
    }

    @Override
    public void Update(Color color) {
    	
    	float[] floats = new float[3];
    	color.RGBtoHSB(color.getRed(), color.getGreen(), color.getBlue(), floats);
    	float complementaryHue = floats[0] - (float) 0.5;
    	
        if (complementaryHue < 0) {
            complementaryHue = complementaryHue + 1;
        }
        Color complementaryColor = Color.getHSBColor(complementaryHue, floats[1], floats[2]);

    	super.setColor(complementaryColor);
    }

 
}