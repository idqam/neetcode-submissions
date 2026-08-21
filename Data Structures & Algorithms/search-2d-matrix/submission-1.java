class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        

        for(int i = 0; i < matrix.length ; i++){
            int l = 0; 
            int r = matrix[i].length - 1; 

            
            

            while(l <= r){
                int middle = l + (r- l)/2; 
                if(matrix[i][middle] < target){
                    l = middle + 1;

                }else if(matrix[i][middle] > target){
                    r = middle - 1;
                }else {
                    return true; 
                }
            }
        }
        return false ;
        
    }
}
