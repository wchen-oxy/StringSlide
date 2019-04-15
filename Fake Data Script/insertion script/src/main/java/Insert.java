/**
 * Created by Work on 3/20/19.
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import java.io.File;
import java.io.FileNotFoundException;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Insert {//establish connections to the database
    static final String JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
    static final String DB_URL = "jdbc:mysql://localhost/Test";
    static final String USER = "root";
    static final String PASSWORD = "";
    //sae these information into a dbparam.txt

    private static List<String> getDataFromLine(String line) {

        List<String> values = new ArrayList<String>();

        try (Scanner rowScanner = new Scanner(line)) {

            rowScanner.useDelimiter(",");

            while (rowScanner.hasNext()) {
                String temp;
                String strings = rowScanner.next();
                if (strings.contains("\"")) {
                    temp = strings.substring(1, strings.length() - 1);
                    values.add(temp);
                } else values.add(strings);
            }

        }

        return values;

    }

    public static void main(String[] args) {
        /*
        Players players.csv Teams Teams Members Members
        Tournaments Tournaments
        Matches Matches
        Earnings Earnings
        */


        for (int j = 0; j <= args.length; j = j + 2) {
            String table = args[j];
            String filename = "fake data/" + args[j+1];


            //establish connection
            Connection conn = null;
            //2 ways to format the string
            //1. use Statment and + to a string
            //2. preparedstatement
            PreparedStatement ps = null;

            //insert Pineapple green tea, fruit tea, 4.75
            //INSERT INTO Mennu (drink,category,price)
            // VALUES(Pineapple green tea, fruit tea, 4.75);
            //format a bunch of the insert statements
            //send to mysql to execute

            //open connection
            try {
                //try to regiester the jdbc Driver
                Class.forName(JDBC_DRIVER);
                //open connection
                conn = DriverManager.getConnection(DB_URL, USER, PASSWORD);

                //format the string from readin in data from csv
                //execute that

                //read in a csv
                List<List<String>> csvData = new ArrayList<>();
                System.out.println(System.getProperty("user.dir"));

                try (Scanner scan = new Scanner(new File(filename))) {
                    while (scan.hasNextLine()) {
                        csvData.add(getDataFromLine(scan.nextLine()));
                    }
                } catch (FileNotFoundException e) {
                    e.printStackTrace();
                }
                System.out.println("Insert into the " + table + " Table..");

                //loop through the recorrds
                //cfor each record
                //make a prepared statement

                //execute the statement
                String insertTableSql = "";

                if (table.equals("Guitar")) {
                    insertTableSql = "INSERT INTO Guitar(guitar_id, manufacturer_name, guitar_name, guitar_model," +
                            " serial_number)" +
                            "Values(?, ?, ?, ?, ?)";
                } else if (table.equals("Story")) {
                    insertTableSql = "INSERT INTO Story(story_id, guitar_id, story_text, where_purchased," +
                            " custom_built)" +
                            "Values(?, ?, ?, ?, ?)";
                } else if (table.equals("Photos")) {
                    insertTableSql = "INSERT INTO Photos(guitar_id, photo_number, photo_path)" +
                            "Values(?, ?, ?)";
                } else if (table.equals("Videos")) {
                    insertTableSql = "INSERT INTO Videos(guitar_id, video_number, video_path)" +
                            "Values(?, ?, ?)";
                } else if (table.equals("Specs")) {
                    insertTableSql = "INSERT INTO Specs(guitar_id, production_year, weight, finish, body_wood, " +
                            "neck_wood, fretboard_wood, cap_wood, neck_pickup, middle_pickup, bridge_pickup, repairs" +
                            "Values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";
                } else if (table.equals("Appearances")) {
                    insertTableSql = "INSERT INTO Appearances(guitar_id, tour_name, album_name)" +
                            "Values(?, ?, ?)";
                }


                for (int i = 0; i < csvData.size(); i++) {
                    //insert into Menu (drink, category, price)
                    //values (Pineapple green tea, fruit tea, 4.75
                    System.out.println(insertTableSql);
                    ps = conn.prepareStatement(insertTableSql);

                    if (table.equals("Guitar")) {
                        //guitar_id
                        ps.setInt(1, Integer.parseInt(csvData.get(i).get(0)));
                        //manufacturer name
                        try {
                            ps.setString(2, csvData.get(i).get(1));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(2, Types.VARCHAR);
                        }
                        //guitar name
                        try {
                            ps.setString(3, csvData.get(i).get(2));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(3, Types.VARCHAR);
                        }
                        //guitar_model
                        try {
                            ps.setString(4, csvData.get(i).get(3));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(4, Types.VARCHAR);
                        }
                        //serial_number
                        try {
                            ps.setLong(5, Integer.parseInt(csvData.get(i).get(4)));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(5, Types.INTEGER);
                        }

                    } else if (table.equals("Story")) {
//
                        ps.setInt(1, Integer.parseInt(csvData.get(i).get(0)));
                        ps.setInt(2, Integer.parseInt(csvData.get(i).get(1)));
                        //story_text
                        try {
                            ps.setString(3, csvData.get(i).get(2));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(3, Types.VARCHAR);
                        }
                        //where_purchased
                        try {
                            ps.setString(4, csvData.get(i).get(3));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(4, Types.VARCHAR);
                        }
                        //custom_built
                        try {
                            ps.setBoolean(5, Boolean.parseBoolean(csvData.get(i).get(4)));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(5, Types.BOOLEAN);
                        }

                    } else if (table.equals("Photos")) {
                        //guitar_id
                        ps.setInt(1, Integer.parseInt(csvData.get(i).get(0)));
                        //photo_num
                        ps.setInt(2, Integer.parseInt(csvData.get(i).get(1)));
                        //photo_path
                        ps.setString(3, csvData.get(i).get(2));


                    } else if (table.equals("Videos")) {
                        //guitar_id
                        ps.setInt(1, Integer.parseInt(csvData.get(i).get(0)));
                        //photo_num
                        ps.setInt(2, Integer.parseInt(csvData.get(i).get(1)));
                        //photo_path
                        ps.setString(3, csvData.get(i).get(2));


                    }  else if (table.equals("Specs")) {

                        ps.setInt(1, Integer.parseInt(csvData.get(i).get(0)));

                        try{
                        ps.setInt(2, Integer.parseInt(csvData.get(i).get(1)));}
                        catch (IndexOutOfBoundsException ie) {
                            ps.setNull(2, Types.INTEGER);
                        }
                        try{
                            ps.setDouble(3, Double.parseDouble(csvData.get(i).get(2)));
                        }
                        catch (IndexOutOfBoundsException ie) {
                            ps.setNull(3, Types.DOUBLE);
                        }
                        //finish
                        try {
                            ps.setString(4, csvData.get(i).get(3));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(4, Types.VARCHAR);
                        }
                        //body wood
                        try {
                            ps.setString(5, csvData.get(i).get(4));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(5, Types.VARCHAR);
                        }
                        //neck wood
                        try {
                            ps.setString(6, csvData.get(i).get(5));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(6, Types.VARCHAR);
                        }
                        //fretboard_wood
                        try {
                            ps.setString(7, csvData.get(i).get(6));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(7, Types.VARCHAR);
                        }
                        //cap_wood
                        try {
                            ps.setString(8, csvData.get(i).get(7));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(8, Types.VARCHAR);
                        }
                        //neck_pickup
                        try {
                            ps.setString(9, csvData.get(i).get(8));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(9, Types.VARCHAR);
                        }
                        //middle_pickup
                        try {
                            ps.setString(10, csvData.get(i).get(9));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(10, Types.VARCHAR);
                        }
                        //bridge_pickup
                        try {
                            ps.setString(11, csvData.get(i).get(10));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(11, Types.VARCHAR);
                        }
                        //repairs
                        try {
                            ps.setBoolean(12, Boolean.parseBoolean(csvData.get(i).get(4)));
                        } catch (IndexOutOfBoundsException ie) {
                            ps.setNull(12, Types.BOOLEAN);
                        }

                    } else if (table.equals("Appearances")) {
                        try{
                        ps.setInt(1, Integer.parseInt(csvData.get(i).get(0)));}
                        catch (IndexOutOfBoundsException ie) {
                            ps.setNull(1, Types.INTEGER);
                        }
                        try{
                            ps.setString(2, csvData.get(i).get(1));
                        }catch (IndexOutOfBoundsException ie){
                            ps.setNull(2, Types.VARCHAR);
                        }
                        try{
                            ps.setString(3, csvData.get(i).get(2));
                        }catch (IndexOutOfBoundsException ie){
                            ps.setNull(3, Types.VARCHAR);
                        }

                    }

                    System.out.println(ps);
                    ps.executeUpdate();
                }

                ps.close();

            } catch (SQLException e) {
                e.printStackTrace();
            } catch (ClassNotFoundException e) {
                e.printStackTrace();
            }

        }
    }
}
