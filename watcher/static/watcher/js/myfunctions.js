$(document).ready(function(){
	
	var i=0;
	
	for( i=0 ; i < $("tbody tr td.per_buy").length ; i++ ){
		$("tbody tr td.per_buy")[i].classList.remove("green1","green2","green3","green4","green5");
		if(!($("tbody tr td.per_buy")[i].innerText==0.0)){
			if($("tbody tr td.per_buy")[i].innerText<0 ){			
				$("tbody tr td.per_buy")[i].classList.add("green1");
			}
			else if($("tbody tr td.per_buy")[i].innerText>=8 && $("tbody tr td.per_buy")[i].innerText<10){
				$("tbody tr td.per_buy")[i].classList.add("green2");
			}
			else if($("tbody tr td.per_buy")[i].innerText>=5 && $("tbody tr td.per_buy")[i].innerText<8){			
				$("tbody tr td.per_buy")[i].classList.add("green3");
			}
			else if($("tbody tr td.per_buy")[i].innerText>=3 && $("tbody tr td.per_buy")[i].innerText<5){
				$("tbody tr td.per_buy")[i].classList.add("green4");
			}
			else if($("tbody tr td.per_buy")[i].innerText<3){			
				$("tbody tr td.per_buy")[i].classList.add("green5");
			}
		}
	}
	for( i=0 ; i < $("tbody tr td.per_sell").length ; i++ ){
		$("tbody tr td.per_sell")[i].classList.remove("red1","red2","red3","red4","red5");
		if(!($("tbody tr td.per_sell")[i].innerText==0.0)){
			if($("tbody tr td.per_sell")[i].innerText>-10 && $("tbody tr td.per_sell")[i].innerText<-8 ){			
				$("tbody tr td.per_sell")[i].classList.add("red1");
			}
			else if($("tbody tr td.per_sell")[i].innerText>=-8 && $("tbody tr td.per_sell")[i].innerText<-5){			
				$("tbody tr td.per_sell")[i].classList.add("red2");
			}
			else if($("tbody tr td.per_sell")[i].innerText>=-5 && $("tbody tr td.per_sell")[i].innerText<-3){
				$("tbody tr td.per_sell")[i].classList.add("red3");
			}
			else if($("tbody tr td.per_sell")[i].innerText>=-3 && $("tbody tr td.per_sell")[i].innerText<0){			
				$("tbody tr td.per_sell")[i].classList.add("red4");
			}
			else if($("tbody tr td.per_sell")[i].innerText>=0){			
				$("tbody tr td.per_sell")[i].classList.add("red5");
			}
		}
	}
});
function AutoRefresh( t ){
		setTimeout("location.reload(true);", t);
	}
