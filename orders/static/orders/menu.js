document.addEventListener('DOMContentLoaded', function(){
		
	// setting up templates as handelbars html elements
	const selection__main = Handlebars.compile(document.querySelector("#selection__main").innerHTML);
	const selection__specific__menu = Handlebars.compile(document.querySelector("#selection__specific__menu").innerHTML);

	document.querySelectorAll('.category__button').forEach((item) =>{

		item.onclick = function(){
			const request = new XMLHttpRequest();
			const category = item.dataset.category;
			request.open('GET', `/API/${category}`);


			request.onload = () =>{

				const data = JSON.parse(request.responseText);
				//check for 200
				const selection = selection__main({ 'items': data });
				document.querySelector('#cont__specific').innerHTML = '';
				document.querySelector('#cont__specific').innerHTML += selection;

				buttons = document.querySelector('#cont__specific').children;
				array = Array.from(buttons);

				array.forEach((item) => {
					item.onclick = function(){
						index = item.querySelector('.meal__button').dataset.index
						
						if (data[index]['price_l'] > 0){
							const  plate = selection__specific__menu(data[index]);
							document.querySelector(".selection__specific").innerHTML = '';
							document.querySelector(".selection__specific").innerHTML += plate;

							document.querySelectAll('.size_button').forEach((button) =>{

								button.onclick => {
									size = button.dataset.size

									if (size === 'small'){
										let context = {
											'category':data['category'],
											'id':data['id'],
											'extra':data['extras'],
											'name':data['name'],
											'price':data['price'],
										}
									}
									else{
										let context = {
											'category':data['category'],
											'id':data['id'],
											'extra':data['extras'],
											'name':data['name'],
											'price':data['price_l'],}
									}
									console.log('working')
								}
							});
						}
							
						if (data[index]['extras'] > 0)
							loadWithToppings(data[index]['id'], data[index])
						else{
							const  plate = selection__specific__menu(context);
							document.querySelector(".selection__specific").innerHTML = '';
							document.querySelector(".selection__specific").innerHTML += plate;
						}
							
						return false;
					}
				});
			}
			request.send();
		};
	});
	function loadWithToppings(pk, data){
		const toppings_request = new XMLHttpRequest();
		toppings_request.open('GET', `/API/toppings/${pk}`);

		toppings_request.onload = () =>{

			const topping_list = JSON.parse(toppings_request.responseText);
			console.log(topping_list)
			context = {
			'category':data['category'],
			'id':data['id'],
			'extra':data['extras'],
			'name':data['name'],
			'price':data['price'],
			'price_l':data['price_l'],
			'toppings':topping_list,
			}
		const  plate = selection__specific__menu(context);
		document.querySelector(".selection__specific").innerHTML = '';
		document.querySelector(".selection__specific").innerHTML += plate;

		}
		toppings_request.send()
	}
});
Handlebars.registerHelper("check",  function(value, options) {
	if (value > 0)
  		return options.fn(this);
  	else
  		return options.inverse(this);
});
Handlebars.registerHelper("times", function(n, options) {
    var result = '';
    for(var i = 0; i < n; ++i)
        result += options.fn(this);
    console.log(result)
    return result;
});