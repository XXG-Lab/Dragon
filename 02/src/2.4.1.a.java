import java.io.*;

class Parser {
    static int lookahead;
    
    public Parser() throws IOException {
        lookahead = System.in.read();
    }
    
    public void S() throws Exception {
        switch (lookahead) {
        case '+':
            match('+'); S(); S(); break;
        case '-':
            match('-'); S(); S(); break;
        case 'a':
            match('a'); break;
        default:
            throw new Error("syntax error");
        }
    }
    
    void match(int t) throws IOException {
        if (lookahead == t) {
            lookahead = System.in.read();
        } else {
            throw new Error("syntax error");
        }
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        Parser parse = new Parser();
        try {
            parse.S();
        } catch (Exception e) {
            System.out.println(e.toString());
        }
    }
}
