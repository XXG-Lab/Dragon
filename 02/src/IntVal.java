package lexer;

public class IntVal extends Token {
    public final int value;

    public IntVal(int v) {
        super(Tag.INT);
        value = v;
    }
}
