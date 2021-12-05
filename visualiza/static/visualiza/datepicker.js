const startDateElement = document.getElementById('startDate');
const linked1 = new tempusDominus.TempusDominus(startDateElement, {
	restrictions: {
		daysOfWeekDisabled: [0, 6]
	},
	localization: {
		locale: "pt-BR"
	}
});

const linked2 = new tempusDominus.TempusDominus(document.getElementById('endDate'), {
	useCurrent: false,
	restrictions: {
		daysOfWeekDisabled: [0, 6]
	},
	localization: {
		locale: "pt-BR"
	}
});


//when the start date is selected, allows only 5 work days ahead to be selected
startDateElement.addEventListener(tempusDominus.Namespace.events.change, (e) => {
	let currentDate = e.detail.date
	let num = 4
	if (currentDate.weekDay != 1) num = 6
	newDate = currentDate.manipulate(num, 'date')
	linked2.updateOptions({
		restrictions: {
			enabledDates: [newDate]
		},
		defaultDate: newDate
	});
});


