import java.util.Arrays;

public class DynamicArray {
    private int[] data = new int[8];
    private int size = 0;

    public void add(int value){
        data[size++] = value;
    }

    



    public String toString() {
        return Arrays.toString(data);
    }

    
}