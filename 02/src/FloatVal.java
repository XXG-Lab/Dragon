package lexer;

public class FloatVal extends Token {
    public final double value;

    public FloatVal(double v) {
        super(Tag.FLOAT);
        value = v;
    }
}
