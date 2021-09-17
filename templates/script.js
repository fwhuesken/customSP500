const sectors = ["Industrials", "Health Care", "Information Technology", "Communication Services", "Consumer Staples", "Consumer Discretionary", "Utilities", "Financials", "Materials", "Real Estate", "Energy"]

const sectorDropDown = document.querySelectorAll('select.form-field__full')


//Populate dropdown menus
sectorDropDown.innerHTML = sectors.map(player => `<option value="${player}">${sectors}</option>`).join(''));