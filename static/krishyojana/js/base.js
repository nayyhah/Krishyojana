function startOver() {
	document.loan_form.loan_amt.value="";
	document.loan_form.months.value="";
	document.loan_form.rate.value="";
	document.loan_form.extra.value="0";

	document.getElementById("loan-info").innerHTML="";
	document.getElementById("table").innerHTML="";

	if (matchMedia("(min-width: 768px)").matches){
			document.getElementById("form").classList.add('center');
			document.getElementById("form").classList.remove('col-md-8');
	}

	li = document.getElementById("loan-info");
	ta = document.getElementById("table");
	tain = document.getElementById("info-table");
	th = document.getElementById("table-header");
	li.style.display = "none";
	ta.style.display = "none";
	th.style.display = "none";
	tain.style.display = "none";
}

function validate() {
	var loan_amt = document.loan_form.loan_amt.value;
	var months = document.loan_form.months.value;
	var rate = document.loan_form.rate.value;
	var extra = document.loan_form.extra.value;

	document.getElementById("loan-details").classList.add('col-md-4');
	document.getElementById("form").classList.remove('center');
	document.getElementById("form").classList.add('col-md-8');
	li = document.getElementById("loan-info");
	ta = document.getElementById("table");
	tain = document.getElementById("info-table");
	th = document.getElementById("table-header");
	li.style.display = "inline-block";
	ta.style.display = "block";
	th.style.display = "block";
	tain.style.display = "block";

	//sNaN(Number(loan_amt)) checks to see is user enters a float
	if (loan_amt <= 0 || isNaN(Number(loan_amt))) {
		alert("Please enter a valid laon amount.");
		document.loan_form.loan_amt.value="";
	}

	else if (months <= 0 || parseInt(months) != months) {
		alert("Please enter a valid number of months.");
		document.loan_form.months.value="";
	}

	else if (rate <= 0 || isNaN(Number(rate))) {
		alert("Please enter a valid interest rate.");
		document.loan_form.rate.value="";
	}

	else if (extra < 0 || isNaN(Number(extra))) {
		alert("Please enter a valid amount of extra money to be paid.");
		document.loan_form.extra.value="0";
	}

	else {
		calculate(parseFloat(loan_amt), parseInt(months), parseFloat(rate), parseFloat(extra));
	}
}

function calculate(loan_amt, months, rate, extra) {
	i = rate/100;

	var monthly_payment = loan_amt*(i/12)*Math.pow((1+i/12), months) / (Math.pow((1+i/12), months) - 1);

	var info = "";
	info += "<table width='250'>";
	info += "<tr><td>Loan Amount: </td>";
	info += "<td align='right'>&#8377; "+loan_amt+"</td></tr>";

	info += "<tr><td>Number of Months: </td>";
	info += "<td align='right'>"+months+"</td></tr>";

	info += "<tr><td>Interest Rate: </td>";
	info += "<td align='right'>"+rate+" &#37;</td></tr>";

	info += "<tr><td>Monthly Payment: </td>";
	info += "<td align='right'>&#8377; "+round(monthly_payment, 2)+"</td></tr>";

	info += "<tr><td>Extra: </td>";
	info += "<td align='right'>&#8377; "+extra+"</td></tr>";

	info += "<tr><td>Total Payment:<br>(per month) </td>";
	info += "<td align='right'>&#8377; "+round(monthly_payment + extra, 2)+"</td></tr>";

	info += "</table>";

	document.getElementById("loan-info").innerHTML = info;

	// -------------------------------------------------------------------------------

	var table="";

	table += "<table class='table table-striped table-responsive-sm'>";

	table += "<tr>";
		table += "<td>0</td>";
		table += "<td>&nbsp;</td>";
		table += "<td>&nbsp;</td>";
		table += "<td>&nbsp;</td>";
		table += "<td>&nbsp;</td>";
		table += "<td>"+round(loan_amt, 2)+"</td>";
	table += "</tr>";

	var current_balance = loan_amt;
	var payment_counter = 1;
	var total_interest = 0;
	monthly_payment = monthly_payment + extra;

	while(current_balance > 0) {

		towards_interest = (i/12)*current_balance; //Calculates the portion of interest that is in monthly payment.
		
		if (monthly_payment > current_balance) {
			monthly_payment = current_balance + towards_interest;
		}

		towards_balance = monthly_payment - towards_interest;
		total_interest = total_interest + towards_interest;
		current_balance = current_balance - towards_balance;

		//display row
		table += "<tr>";
			table += "<td>"+payment_counter+"</td>"
			table += "<td>"+round(monthly_payment, 2)+"</td>"
			table += "<td>"+round(towards_balance, 2)+"</td>"
			table += "<td>"+round(towards_interest, 2)+"</td>"
			table += "<td>"+round(total_interest, 2)+"</td>"
			table += "<td>"+round(current_balance, 2)+"</td>"
		table += "</tr>"

		payment_counter++;
	}

	table += "</table>"

	document.getElementById("table").innerHTML = table;
}

function round(num, dec) {
	return (Math.round(num*Math.pow(10,dec))/ Math.pow(10,dec)).toFixed(dec);
}