/*
Henry Johnson
The function of this program is to send a prerecorded tweet when its tag is called
date created:10/27/20
last edited:11/2/20
 */
import twitter4j.Status;
import twitter4j.Twitter;
import twitter4j.TwitterException;
import twitter4j.TwitterFactory;
import java.io.*;
import java.nio.charset.Charset;

public class TwitterAutoBot {

    public static void main(String[] args) {
        tweetLines();
    }

    private static void tweetLines() {
        String line;
        try {
            try (
                    InputStream fis = new FileInputStream("/Users/hjohnson22/IdeaProjects/TwitterAutoBot/src/main/resources/tweets.txt");
                    InputStreamReader isr = new InputStreamReader(fis, Charset.forName("Cp1252"));
                    BufferedReader br = new BufferedReader(isr);
            ) {
                while ((line = br.readLine()) != null) {
                    // Deal with the line
                    sendTweet(line);
                    System.out.println("Tweeting: " + line + "...");

                    try {
                        System.out.println("Sleeping for 30 minutes...");
                        Thread.sleep(1800000); // every 30 minutes
                        // Thread.sleep(10000); // every 10 seconds
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }

                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    private static void sendTweet(String line) {
        Twitter twitter = TwitterFactory.getSingleton();
        Status status;
        try {
            status = twitter.updateStatus(line);
            System.out.println(status);
        } catch (TwitterException e) {;
            e.printStackTrace();
        }
    }

}
