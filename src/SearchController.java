import javafx.fxml.FXML;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class SearchController {


    @FXML
    TextField faculty;
    @FXML
    TextField courseNums;
    @FXML
    ListView exams;

    ArrayList<String> response = new ArrayList<>();
    public void search() throws IOException, InterruptedException {

        Process out = Runtime.getRuntime().exec("py ExamScheduleScraper.py   " + faculty.getText()+" " + courseNums.getText());

        BufferedReader input = new BufferedReader(new InputStreamReader(out.getInputStream()));
        String text = null;
         while ((text = input.readLine()) != null) {
             System.out.println(text);
             response.add(text);
         }
        out.waitFor();

         setExams();
    }

    public void setExams() throws IOException {


        exams.getItems().clear();
        exams.refresh();

        for(int x =0; x < response.size(); x++)
        {
            if(response.get(x).equals( "Place: �") ||response.get(x).equals( "Place: ") )
            {
                exams.getItems().add("Place: Not Listed");
            }
            else {
                exams.getItems().add(response.get(x));
            }
            if(response.get(x).contains("Exam"))
            {
                exams.getItems().add(" ");
            }
            response.remove(x);
            x--;
        }

    }

}
