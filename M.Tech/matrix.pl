#!/usr/bin/perl

@var = (2,3,5,4,1,3,2,1);

addition(@var);
multiplication(@var);

sub addition{
	my @list=@_;
	my @mat1=([$list[0],$list[1]],[$list[2],$list[3]]);
	my @mat2=([$list[4],$list[5]],[$list[6],$list[7]]);
	
	my @mat3 =([0,0],[0,0]);
	$mat3[0][0] = $mat1[0][0] + $mat2[0][0];
	$mat3[1][1] = $mat1[1][1] + $mat2[1][1];
	$mat3[0][1] = $mat1[0][1] + $mat2[0][1];
	$mat3[1][0] = $mat1[1][0] + $mat2[1][0];
	print "\n Addition Result \n \t";
	for(my $i=0;$i<= $#mat3; $i++){
		for(my $m = 0; $m <= $#mat3; $m++){
			print $mat3[$i][$m], "\t";
		}
		print "\n \t";
	}
	print "\n Output Matrix : \n";
	print "\n \t Diagonal results of addition \t", $mat3[0][0],"\t", $mat3[1][1];
}
sub multiplication{
	my @list=@_;
	my @mat1=([$list[0],$list[1]],[$list[2],$list[3]]);
	my @mat2=([$list[4],$list[5]],[$list[6],$list[7]]);
	
	my @mat4 =([0,0],[0,0]);
	
	for(my $i =0; $i<= $#mat1; $i++){
		for(my $m=0; $m <= $#mat2; $m++){
			$a = $mat1[$i][0]*$mat2[0][$m];
			$b = $mat1[$i][1]*$mat2[1][$m];
			$mat4[$i][$m] = $a + $b;
			chomp($mat3[$i][$m]);
		}
	}
	print "\n Multiplication Result \n \t ";
	for(my $i=0;$i<= $#mat4; $i++){
		for(my $m = 0; $m <= $#mat4; $m++){
			print $mat4[$i][$m], "\t";
		}
		print "\n \t";
	}
	print "\n Output Matrix : \n";
	print "\n \t Diagonal results of multiplication \t", $mat4[0][0],"\t", $mat4[1][1];
}

print "\n \n";
