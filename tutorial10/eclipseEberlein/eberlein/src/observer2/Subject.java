package observer2;

import java.awt.Color;
import java.util.ArrayList;

public interface  Subject {
	
	public void Attach(Observer o);
	public void Detach(Observer o);
	
	void Notify(Color newCol, Color comtempCol);
	
}
