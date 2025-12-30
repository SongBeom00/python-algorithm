import java.util.Arrays;

public class ArrayModify{

    public static void main(String[] args) {
        Integer[] arr = {27, 36, 45, 44, 21, 16, 82, 11};
        // arr.length = 8

        // 6번째 제거 arr[5]
        for (int i = 5; i < arr.length - 1; i++) { // 7번까지 for문
            arr[i] = arr[i + 1];
        }

        arr[arr.length -1] = null;

        System.out.println(Arrays.toString(arr));

        // 1번째 자리에 33 삽입
        for (int i = arr.length - 1; i > 1; i--){
            arr[i] = arr[i - 1];
        }
        arr[1] = 33;

        System.out.println(Arrays.toString(arr));
    }
}