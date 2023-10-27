package Ex1;

public class Rectangle extends Shape {
    private final double length;
    private final double width;

    public Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    @Override
    public double calculateArea() {
        return length * width;
    }

    @Override
    public double calculatePerimeter() {
        return 2 * (length + width);
    }

    public void setAreaSuper() {
        super.area = calculateArea();
    }
    public void setPerimeterSuper() {
        super.perimeter = calculatePerimeter();
    }

    public String getName() {
        return this.getClass().getSimpleName();
    }
}
