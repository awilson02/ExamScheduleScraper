import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Main extends Application {

    public static Stage primaryStage = new Stage();

    @Override
    public void start(Stage temp) throws Exception{

        Parent root = FXMLLoader.load(getClass().getResource("resources/home.fxml"));
        Scene home = new Scene(root);

        home.getStylesheets().add(getClass().getResource("resources/button.css").toExternalForm());


        primaryStage.setTitle("To Do Manger");
        primaryStage.setScene(home);
        primaryStage.show();

    }

}
