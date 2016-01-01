import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

// NOTE: apache commons lang3 must be in classpath.
import org.apache.commons.lang3.StringUtils;


public class mMTranslator {

	public static void main(String[] args) {
		// opening the file and reading data
		File file = new File("src/KLSadd.tex");
		String data = "";
		BufferedReader reader = null;
		try {
		    reader = new BufferedReader(new FileReader(file));
		    String text = null;

		    while ((text = reader.readLine()) != null) {
		        data += text+'\n';
		    }
		} catch (FileNotFoundException e) {
		    e.printStackTrace();
		} catch (IOException e) {
		    e.printStackTrace();
		}
		// translating, printing
		System.out.println(StringUtils.replaceChars(data,"mM","Mm"));
	}

}
