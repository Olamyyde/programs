<?php
    for($i = 1; $i <= 1000; ++$i){
        $no10 = $i % 10;
        $no3 = $i % 3;
        
        
        
        if(!$no10){
            print "Every 10th number are: <b>" .$i. "</b><br>";
        }
        if(!$no3){
            print "Every 3rd number are: <i>" .$i. "</i><br>";
        }


        for($j=2; $j<=$i; $j++){
            for($k=2; $k < $j; $k++){
               if($j % $k==0){
                break;
               } 

           }

        }
        if($k == $j){
                print " Prime numbers from 1 to 1000000 are: <u>".$j."</u> <br/>";

            }

       break;
         
        
    }
                
?>