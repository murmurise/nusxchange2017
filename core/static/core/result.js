$('.show-list').click(function(){
	$('.wrapper').addClass('list-mode');
	// setTimeout(function(),1000)
	document.getElementById('user-details-sam').style.visibility='visible';
	document.getElementById('user-details-jinyi').style.visibility='visible';
	document.getElementById('user-details-ben').style.visibility='visible';


});

$('.hide-list').click(function(){
	$('.wrapper').removeClass('list-mode');
	document.getElementById('user-details-sam').style.visibility='hidden';
	document.getElementById('user-details-jinyi').style.visibility='hidden';
	document.getElementById('user-details-ben').style.visibility='hidden';


});