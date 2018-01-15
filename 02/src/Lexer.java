package lexer;

import java.io.*;
import java.util.*;

public class Lexer {
    public int line = 1;
    private char peek = ' ';
    private Hashtable words = new Hashtable();

    void reserve(Word t) {
        words.put(t.lexeme, t);
    }

    public Lexer() {
        reserve(new Word(Tag.TRUE, "true"));
        reserve(new Word(Tag.FALSE, "false"));
    }

    public Token scan() throws IOException {
        if (peek == -1) {
            return null;
        }
        for (; ; peek = (char)System.in.read()) {
            if (peek == ' ' || peek == '\t') {
                continue;
            } else if (peek == '\n') {
                ++line;
            } else {
                break;
            }
        }
        if (peek == '/') {
            peek = (char)System.in.read();
            if (peek == '/') {
                do {
                    peek = (char)System.in.read();
                } while (peek != '\n');
                peek = (char)System.in.read();
            } else if (peek == '*') {
                do {
                    do {
                        peek = (char)System.in.read();
                    } while (peek != '*');
                    peek = (char)System.in.read();
                } while (peek != '/');
                peek = (char)System.in.read();
            }
        }
        if (Character.isDigit(peek) || peek == '.') {
            int intVal = 0;
            do {
                if (peek == '.') {
                    break;
                }
                intVal = intVal * 10 + Character.digit(peek, 10);
                peek = (char)System.in.read();
            } while (Character.isDigit(peek));
            if (peek != '.') {
                return new IntVal(intVal);
            }
            double doubleVal = intVal;
            double precision = 1.0;
            while (true) {
                peek = (char)System.in.read();
                if (!Character.isDigit(peek)) {
                    System.out.println(doubleVal);
                    return new FloatVal(doubleVal);
                }
                precision /= 10.0;
                doubleVal += Character.digit(peek, 10) * precision;
            }
        }
        if (Character.isLetter(peek)) {
            StringBuffer b = new StringBuffer();
            do {
                b.append(peek);
                peek = (char)System.in.read();
            } while (Character.isLetterOrDigit(peek));
            String s = b.toString();
            Word w = (Word)words.get(s);
            if (w != null) {
                return w;
            }
            w = new Word(Tag.ID, s);
            words.put(s, w);
            return w;
        }
        if (peek == '!' || peek == '<' || peek == '>' || peek == '=') {
            char first = peek;
            peek = (char)System.in.read();
            if (first == '!') {
                peek = (char)System.in.read();
                return new Word(Tag.OP, "!=");
            }
            if (peek == '=') {
                peek = (char)System.in.read();
                return new Word(Tag.OP, first + "=");
            }
            return new Word(Tag.OP, "" + first);
        }
        Token t = new Token(peek);
        peek = ' ';
        return t;
    }

    public static void main(String[] args) throws IOException {
        Token token;
        Lexer lexer = new Lexer();
        while ((token = lexer.scan()) != null) {
            System.out.println(token.tag);
        }
    }

}
