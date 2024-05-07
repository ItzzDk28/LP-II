public class LinearSearch {
      public static Integer search(Integer[] arr, Integer target) {
        for(Integer i = 0; i < arr.size(); i++) {
            if(arr[i] == target) {
                return i;
            }
        }
        return -1; // If target not found
    }
}


Debug Code


Integer[] numbers = new Integer[]{10, 20, 30, 40, 50};
Integer targetIndex = LinearSearch.search(numbers, 30);
if(targetIndex != -1) {
   System.debug('Target found at index: ' + targetIndex);
} else {
   System.debug('Target not found');
}
