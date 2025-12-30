import java.util.Arrays;

public class InsertIntoArray {
    public static void main(String[] args) {
        int[] original = {27, 33, 36, 45, 44, 21, 82, 11};
        int[] result = new int[original.length + 1];

        int insertIndex = 2;
        int insertValue = 10;

        for (int i = 0; i < insertIndex; i++) {
            result[i] = original[i]; // 기존의 배열을 새로운 배열로 옮겨줍니다.
        }

        result[insertIndex] = insertValue;
        
        System.out.println(Arrays.toString(result));
        // 8
        for (int i = insertIndex; i < result.length - 1; i++) {
            result[i + 1] = original[i];
        }

        System.out.println(Arrays.toString(result));

    }
    
}
