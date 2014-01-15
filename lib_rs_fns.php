    function sd_square($x, $mean) { return pow($x - $mean,2); }

    // Function to calculate sd + mean
    function sd_mean($array) {
        $count = count($array);
        $mean = array_sum($array) / $count;
        $sum_sd_square = array_sum(array_map("sd_square", $array, array_fill(0,$count, $mean ) ) );
        // square root of sum of squares devided by N-1
        $sd = sqrt($sum_sd_square)/($count-1);  
        
        //Limit is mean + one sd
        return $mean + $sd ;
    }